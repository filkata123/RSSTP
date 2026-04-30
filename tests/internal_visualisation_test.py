import numpy as np
import pytest
from internal import Internal
from visualization import Visualizer

def test_build_transition_graph_edges():
    obj = Internal(np.array([[[0,1],[2,5]], [[2,4],[1,3]]], dtype=object))
    G = Visualizer.build_transition_graph(obj.get_transition_matrix())
    
    source = G.source
    assert "0 -> 1" in source
    assert "1 -> 0" in source

def test_build_transition_graph_edge_labels():
    obj = Internal(np.array([[[0,1],[2,5]], [[2,4],[1,3]]], dtype=object))
    G = Visualizer.build_transition_graph(obj.get_transition_matrix())
    
    source = G.source
    assert "[2, 5]" in source  # label on edge 0->1
    assert "[2, 4]" in source  # label on edge 1->0

def test_build_transition_graph_empty_cell_no_edge():
    # tm[0][0] is empty, so no self-loop on node 0 should exist
    obj = Internal(np.array([[[], [1]], [[2], []]], dtype=object))
    G = Visualizer.build_transition_graph(obj.get_transition_matrix())
    
    source = G.source
    assert "0 -> 0" not in source
    assert "1 -> 1" not in source

def test_plot_transition_graph_calls_render(mocker):
    # test that plot_transition_graph triggers a render
    mock_render = mocker.patch("graphviz.Digraph.render")
    mocker.patch("matplotlib.image.imread", return_value=np.zeros((10, 10, 3)))
    
    obj = Internal(np.array([[[0,1],[2,5]], [[2,4],[1,3]]], dtype=object))
    Visualizer.plot_transition_graph(obj.get_transition_matrix())
    
    mock_render.assert_called_once()
