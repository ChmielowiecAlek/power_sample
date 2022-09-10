# Introduction

The aim of this code is to repeat the simulation results according to the following article:

"IMPEDANCE MATCHING CONTROLLER FOR AN INDUCTIVELY COUPLED PLASMA CHAMBER, L-type Matching Network Automatic Controller"

by Giorgio Bacelli, John V. Ringwood and Petar Iordanov.

**This code sample is shared for the purpose of a recruitment process only. It has neither scientific nor practical value.**

## Details

By this exercise I've tried:

  - to refresh knowledge on electrical engineering,

  - to learn something about plasma power controllers,

  - to prove general command of python by writing a sample code basing on the abovementioned article,

  - to provide some tests cases using pytest,

  - to show examples of using common libraries (numpy, matplotlib),

  - to practice (complex-number) computations in python,

  - to prove my expertise in PyCharm, venv, jupyter notebook and git.

# Before committing to git

  - all tests should pass

  - update requirements.txt

  - clean all jupyter notebook outputs

  - update this README.md

  - update the project structure below

# Current project structure
```
./
├── imc/
│   ├── impedance_tuner.py
│   ├── matching_network.py
│   └── tests/
│     ├── test_impedance_tuner.py
│     └── test_matching_network.py
└── notebook/
    └── reflection_function.ipynb
```
command: ```power_sample$ tree -F -P '*.py|*.ipynb' -I 'venv|jupyterenv|__pycache__|__init__.py|conftest.py'```


# How to run tests

Tests are written using the pytest framework.

## in the terminal

  (venv has to be activated)

  py.test

  or a single test suite (e.g.):

  power_sample$ py.test imc/tests/test_impedance_tuner.py

## in PyCharm

  select the test configuration and press the ▶ button

  (a single test suite can also be run by right-clicking on the test file)

# How to set-up the virtual environment

## for pycharm

  python -m venv venv

  source venv/bin/activate

  pip install -r requirements.txt

  deactivate

## for jupyter notebook

  cd notebook/

  python -m venv jupyterenv

  source jupyterenv/bin/activate

  pip install -r requirements.txt

  deactivate

  cd ..

# How to update requirements.txt

  within a given virtual env

  pip freeze > requirements.txt

  and add it to git

# How to run jupyter notebook

  cd notebook/

  source jupyterenv/bin/activate

  jupyter notebook

  deactivate

  cd ..
