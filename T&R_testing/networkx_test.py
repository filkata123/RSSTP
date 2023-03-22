import networkx as nx
import matplotlib.pyplot as plt

transition_matrix = [[[0],[0,1],[],[]],
                     [[1],[0],[0,1],[]],
                     [[1],[],[0,1],[0]],
                     [[1],[0],[0,1],[]]]

G = nx.DiGraph()

'''Check if the matrix index [i][j] is empty. If the index is empty, that means that
    there is no link from i to j. If the index is not empty, 
    there is a link from i to j -> add edge [i, j] to Graph.'''
for i in range(len(transition_matrix)):     #for every row
    #print("i: {}".format(i))

    for j in range(len(transition_matrix[i])):     #for every column
        #print("j: {}".format(j))

        if transition_matrix[i][j]:     #if index is not empty
            G.add_edge(i, j, a="    "+str(transition_matrix[i][j]))     #add edge: index (i, j) and actions (a) 

#initialize position to use edge_labels
pos = nx.spring_layout(G)
#edge_label=actions
edge_labels = nx.get_edge_attributes(G, "a")
print (edge_labels)

nx.draw(G, pos, with_labels=1)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.7, horizontalalignment="left")
plt.show
plt.pause(10)
