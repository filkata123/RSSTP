# Example file for testing suite

# Get the current working directory
import os
cwd = os.getcwd()

import sys
sys.path.append(cwd+'/src/')

import external
obj = external.External()

def test_sensory_data():
    
    assert obj.getSensoryData() == '229'

