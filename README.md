# RSSTP
Repository for the Robotic Sensorimotor System Testing Platform (RSSTP) project, carried out in the University of Oulu.


## Installation
Python 3.10 is necessary for this library to work.

``` shell
python -m venv venv
source ./venv/bin/activate OR .\venv\Scripts\Activate.ps1 FOR WINDOWS
pip install -r requirements.txt
```
Check [requirements.txt](requirements.txt) for libraries needed by the developer.

Check [setup.py](setup.py) for libraries needed for the software to run.

Ensure that installation has been succesfull by navigating to ```src/demos/``` and running the ```msrgym.py``` demo with python:

```shell
python msrgym.py
```


## How to use
Demos located in ```src/demos``` provide a practical explanation of the library usage.
## Testing
Testing is done using ```pytest```. 
To run the tests navigate to the ```tests``` folder and run pytest (after installation step):
``` shell
pytest
```