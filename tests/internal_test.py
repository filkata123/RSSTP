import os
import sys
cwd = os.getcwd()
sys.path.append(cwd+'/src/')
import internal

obj = internal.Internal()

def test_split():
    n = 0
    assert (obj.split(n) == [[['A','B','C','D'],['A','B','C','D']],[['A','B','C','D'],['A','B','C','D']]]).all

def test_merge():
    n = 0
    m = 0
    assert (obj.merge(n,m) == [[['A','B','C','D'],['A','B','C','D']],[['A','B','C','D'],['A','B','C','D']]]).all

def test_add():
    n = 0
    m = 0
    k = 0
    assert (obj.add(n,m,k) == [[['A','B','C','D'],['A','B','C','D']],[['A','B','C','D'],['A','B','C','D']]]).all

def test_delete():
    n = 0
    m = 0
    k = 0
    assert (obj.delete(n,m,k) == [[['A','B','C','D'],['A','B','C','D']],[['A','B','C','D'],['A','B','C','D']]]).all

def test_transition():
    k = 0
    assert (obj.transition(k) == [[['A','B','C','D'],['A','B','C','D']],[['A','B','C','D'],['A','B','C','D']]]).all
