import matplotlib.pyplot as plt
from matplotlib import image as mpimg
import graphviz


class Visualizer:
    """Centralized visualization management for robot arm and transition graphs.
    
    Manages matplotlib figures and graphviz rendering to avoid figure number conflicts
    and coordinate visualization state across Internal and External components.
    """

    _figure = None
    _ax_arm = None
    _ax_graph = None
    _interactive_initialized = False
    
    @staticmethod
    def _initialize_figure():
        """Create the combined figure with subplots once."""
        if Visualizer._figure is None:
            Visualizer._figure, (Visualizer._ax_arm, Visualizer._ax_graph) = plt.subplots(1, 2, figsize=(14, 5))
            Visualizer._figure.suptitle('Robot Arm Control', fontsize=16)
            plt.ion()
            Visualizer._interactive_initialized = True
    
    @staticmethod
    def plot_arm(coordinates, obstacles):
        """Visualize the robot arm and obstacles.
        
        Args:
            coordinates (list): List of (x, y) tuples for each joint
            obstacles (list): Obstacle list in form [[x1,y1], radius_1, [x2,y2], radius_2, ...]
        """
        # Initialize interactive mode once
        
        Visualizer._initialize_figure()
        
        Visualizer._ax_arm.clear()
        
        x_coordinates = [0]
        y_coordinates = [0]
        
        for coordinate in coordinates:
            x_coordinates.append(coordinate[0])
            y_coordinates.append(coordinate[1])
        
        Visualizer._ax_arm.plot(x_coordinates, y_coordinates)
        Visualizer._ax_arm.set_xlim([-5, 5.5])
        Visualizer._ax_arm.set_ylim([-5, 5.5])
        Visualizer._ax_arm.set_title('Arm Position')
        
        # Draw obstacles
        for i in range(0, len(obstacles), 2):
            circle = plt.Circle(obstacles[i], obstacles[i+1], color='#e2e2e2')
            Visualizer._ax_arm.add_patch(circle)
        
        Visualizer._ax_arm.grid()
        Visualizer._figure.canvas.draw_idle()
        plt.pause(0.01)

    @staticmethod
    def build_transition_graph(tm):
        """Build and return a graphviz Digraph from a transition matrix.
            Check if the matrix index [i][j] is empty. If the index is empty, that means that
            there is no link from i to j. If the index is not empty, 
            there is a link from i to j -> add edge [i, j] to Graph labeled with the action(s).
        
        Args:
            tm (NDArray): Transition matrix with shape (n, n) containing action lists
        
        Returns:
            graphviz.Digraph: The constructed graph
        """
        G = graphviz.Digraph('transition_matrix_graph', filename='tm_graph', format="png")
        G.attr(rankdir='LR', size='20')
        
        for i in range(len(tm)):
            for j in range(len(tm[i])):
                if tm[i][j]:
                    G.edge(str(i), str(j), label=str(tm[i][j]))
        
        return G
    
    @staticmethod
    def plot_transition_graph(tm):
        """Visualize the transition matrix as a directed graph.
            
            Note: if a node has no links to or from any other nodes, then the node will not be drawn!
        
        Args:
            tm (NDArray): Transition matrix with shape (n, n) containing action lists
        """
        Visualizer._initialize_figure()
        
        Visualizer._ax_graph.clear()
        
        G = Visualizer.build_transition_graph(tm)
        G.render()  # creates tm_graph.png
        
        image = mpimg.imread("tm_graph.png")
        Visualizer._ax_graph.imshow(image)
        Visualizer._ax_graph.set_title('Transition Matrix')
        Visualizer._ax_graph.axis('off')
        Visualizer._figure.canvas.draw_idle()
        plt.pause(0.01)