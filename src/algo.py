import numpy as np
from msrgym import robot_arm

def reset(number_of_states):
    labeling = dict(zip(range(number_of_states), [[]]*number_of_states))
    state_hist = []
    sense_hist = []
    action_hist = []
    return labeling, state_hist, sense_hist, action_hist

def check_for_contradiction(SM_hists):
    action_seqs = [tuple(SM_hists[i]['actions']) for i in range(len(SM_hists))]
    action_seqs = list(set(action_seqs))
    arg_max_action_seq = action_seqs[0]
    max_len = 0
    for action_seq in action_seqs:
        a_len = len(action_seq)
        sense_set = set([tuple(SM_hists[i]['sensations'][:a_len])
                         for i in range(len(SM_hists))
                         if tuple(SM_hists[i]['actions'][:a_len])==action_seq])
        if len(sense_set)>max_len:
            arg_max_action_seq = action_seq
            max_len = len(sense_set)
    if max_len > 1:
        a_len = len(arg_max_action_seq)
        return [SM_hists[i] for i in range(len(SM_hists)) if tuple(SM_hists[i]['actions'][:a_len])==arg_max_action_seq], arg_max_action_seq
    else:
        return None

def consistent(SM_hists):
    return check_for_contradiction(SM_hists) is None

def consistent_succ(SM_hists1, SM_hists2, action):
    for h1 in SM_hists1:
        if h1['actions'][0]==action:
            h11 = h1.copy()
            h11['sensations'] = h11['sensations'][1:]
            h11['actions'] = h11['actions'][1:]
            for h2 in SM_hists2:
                if not consistent([h11,h2]):
                    return False
    return True

def split_node(arm, node, labeling,
               contradicting_hists,
               witness_action_seq):
    N = len(contradicting_hists)
    M = len(labeling)
    labeling[node] = [contradicting_hists[0]]
    for i in range(M,M+N-1):
        labeling[i] = [contradicting_hists[i-M+1]]
        arm.split_node(node)    
    return arm, labeling

def trim_transition_matrix(arm, labeling, new_nodes):
    assert len(arm.int.get_transition_matrix) == len(labeling)
    for action in [0,1]:
        for i in range(len(arm.int.get_transition_matrix)):
            for j in new_nodes:
                if not consistent_succ(labeling[i],labeling[j],action):
                    arm.delete_conection_between_nodes(i, j, action)
    return arm

def untrim_transition_matrix(arm):
    for i in range(len(arm.int.get_transition_matrix)):
        actns = set(np.concatenate(arm.int.get_transition_matrix[i]))
        for action in [0,1]:
            if action not in actns:
                for j in range(len(arm.int.get_transition_matrix[i])):
                    arm.add_connection_between_nodes(i,j,action)
    return arm

def step(arm, labeling, state_hist, sense_hist, action_hist, action):
    state_hist.append(arm.get_current_internal_state())
    sense_hist.append(arm.is_desired_position_reached())
    labeling[state_hist[-1]].append(dict({'sensations': list([]),
                                          'actions':list([])}))
    number_of_states = len(arm.int.get_transition_matrix)
    for i in range(number_of_states):
        for SM_seq in labeling[i]:
            SM_seq['sensations'].append(sense_hist[-1])
    for i in range(number_of_states):
        for SM_seq in labeling[i]:
            SM_seq['actions'].append(action)
    action_hist.append(action)
    arm.update_position(action)
    arm = trim_transition_matrix(arm, labeling, range(number_of_states))
    arm = untrim_transition_matrix(arm)
    for i in range(number_of_states):
        Z=check_for_contradiction(labeling[i])
        if Z is not None:
            contradicting_hists, witness_action_seq = Z
            arm, labeling = split_node(arm, i, labeling,
                                       contradicting_hists,
                                       witness_action_seq)
            new_nodes = [i] + list(range(number_of_states,
                                         number_of_states+len(contradicting_hists)-1))
            arm = trim_transition_matrix(arm, labeling, new_nodes)
            arm = untrim_transition_matrix(arm)
            number_of_states = len(arm.int.get_transition_matrix)
            labeling, state_hist, sense_hist, action_hist=reset(1)
            return arm, labeling, state_hist, sense_hist, action_hist
    return arm, labeling, state_hist, sense_hist, action_hist




n = 1
l = 2
o = [[1000,1000],1,[1000,-1000],1]#[[1,2],1,[-1,-2],1]
# Does the external initialization assume that there are 2 obstacles?
p = 95
feedback = (-0.35, 1.97)
left = 0
right = 1
ACTIONS = list([left,right])
arm = robot_arm(n, l, o, p, feedback, ACTIONS)
labeling, state_hist, sense_hist, action_hist = reset(1)


# RUNNING THE ALGO:

# First 20 actions 'left':

for i in range(20):
    ACTIONS = list([left,right])
    arm, labeling, state_hist, sense_hist, action_hist = step(arm,
                                                              labeling,
                                                              state_hist,
                                                              sense_hist,
                                                              action_hist, 0)
# Then 30 actions 'right':

for i in range(30):
    ACTIONS = list([left,right])
    arm, labeling, state_hist, sense_hist, action_hist = step(arm,
                                                              labeling,
                                                              state_hist,
                                                              sense_hist,
                                                              action_hist, 1)

# Then 40 actions 'left':

for i in range(40):
    ACTIONS = list([left,right])
    arm, labeling, state_hist, sense_hist, action_hist = step(arm,
                                                              labeling,
                                                              state_hist,
                                                              sense_hist,
                                                              action_hist, 0)

# I don't know if this works!! But it is an algorithm :P
