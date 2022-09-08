# power_sample

It is a code sample based on the article "IMPEDANCE MATCHING CONTROLLER FOR AN INDUCTIVELY COUPLED PLASMA CHAMBER, L-type Matching Network Automatic Controller" by Giorgio Bacelli, John V. Ringwood and Petar Iordanov.

It's purpose is to practice complex-number computations in python.


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

