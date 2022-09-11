# Introduction

The aim of this code is to repeat the simulation results according to the following article:

Bacelli, Giorgio & Ringwood, John & Iordanov, Petar. (2007). Impedance matching controller for an inductively coupled plasma chamber - L-type matching network automatic controller.. ICINCO 2007 - 4th International Conference on Informatics in Control, Automation and Robotics, Proceedings. 202-207. 

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

# Project structure
```
./
├── imc/
│ ├── coarse_tuner.py
│ ├── controller.py
│ ├── fine_tuner.py
│ ├── impedance_tuner.py
│ ├── matching_network.py
│ └── tests/
│     ├── test_coarse_tuner.py
│     ├── test_controller.py
│     ├── test_fine_tuner.py
│     ├── test_impedance_tuner.py
│     └── test_matching_network.py
├── main.py
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

# TODO

## matching_network.gamma()
  - verify usages, it is used for both coarse and fine tuning
  - check (4) against the formula from notebook exercises

## coarse_tuner._trigger_impl()
  - check whether it is triggered every fifth tick
  - verify whether it is ok to take the gamma basing on the load capacitor, or a sensor simulator is needed

## fine_tuner._trigger_impl()
  - in my opinion the formula (4) from the article is valid only for a coarse tuning, but it is also used here

## main()
  - currently it does not correctly simulate the circuit from Fig. (8) in the article

# Misc

## How to use octave (e.g.)
```
octave:1> output_precision(8)
octave:2> omega = 2 * pi * 13.56e6
omega = 8.5199993e+07
octave:3> c = 150e-12
c = 1.5000000e-10
octave:4> term = i * omega * c
term =            0 + 0.012779999i
octave:5> z = 1 / term
z =           0 - 78.2472680i
```

## How to push to git
```git push --tags origin main```

## Experimental results from notebook

ZPL values that give something like Fig. 6 (coarse tuning, e.g.)

ZPL=(5.0, 109.0)  min(|Γ|)=0.01  Cl=700pF  Ct=125pF

