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

# How to run tests

Tests are written using the pytest framework.

## in the terminal

  (venv has to be activated)

  py.test

## in PyCharm

  select the test configuration and press the ▶ button

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
