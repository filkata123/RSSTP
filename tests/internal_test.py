import os
cwd = os.getcwd()

import sys
sys.path.append(cwd+'/src/')


import internal
obj = internal.Internal()

n = 0

def test_split():
    assert (obj.split(n) == [[['A','B','C','D'],['A','B','C','D']],[['A','B','C','D'],['A','B','C','D']]]).all

def test_merge():
    assert (obj.merge(n,n) == [[['A','B','C','D'],['A','B','C','D']],[['A','B','C','D'],['A','B','C','D']]]).all

def test_add():
    assert (obj.add(n,n,n) == [[['A','B','C','D'],['A','B','C','D']],[['A','B','C','D'],['A','B','C','D']]]).all

def test_delete():
    assert (obj.delete(n,n,n) == [[['A','B','C','D'],['A','B','C','D']],[['A','B','C','D'],['A','B','C','D']]]).all

def test_transition():
    assert (obj.transition(n) == [[['A','B','C','D'],['A','B','C','D']],[['A','B','C','D'],['A','B','C','D']]]).all