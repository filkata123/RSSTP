import graphviz
import matplotlib.pyplot as plt
from matplotlib import image as mpimg

# transition_matrix = [[[0],[0,1],[],[]],
#                      [[1],[0],[0,1],[]],
#                      [[1],[],[],[0]],
#                      [[1],[0],[0,1],[]]]

transition_matrix = [[[],[1],[],[]],
                     [[],[],[1],[]],
                     [[],[],[],[1]],
                     [[],[],[],[1]]]

G = graphviz.Digraph('transition_matrix_graph', filename='tm_graph', format="png")
G.attr(rankdir='LR', size='8,5')

'''Check if the matrix index [i][j] is empty. If the index is empty, that means that
    there is no link from i to j. If the index is not empty, 
    there is a link from i to j -> add edge [i, j] to Graph with a label of the actions.'''
for i in range(len(transition_matrix)):     #for every row
    #print("i: {}".format(i))

    for j in range(len(transition_matrix[i])):     #for every column
        #print("j: {}".format(j))

        if transition_matrix[i][j]:     #if index is not empty
            G.edge(str(i), str(j), label=str(transition_matrix[i][j]))     #add edge: index (i, j) with label=actions 


G.render()  #this makes the png file
image = mpimg.imread("tm_graph.png")
plt.imshow(image)
plt.show()