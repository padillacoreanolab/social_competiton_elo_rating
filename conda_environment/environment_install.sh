#!/usr/bin/env bash

# Moving to the root directory of the Github repo
cd $(git rev-parse --show-toplevel)

# Turning off the Conda Environment 
# so that you don't add anything onto an existing environment
conda deactivate

# Creating the Conda environment
# Doing it in the root directory to simplify
conda create --prefix ./elo_rating_env python=3.9 --yes
# Turning on the Conda environment
conda activate ./elo_rating_env

# Installing general data processing libraries
conda install -c conda-forge notebook --yes
conda install -c conda-forge pandas --yes
conda install -c conda-forge openpyxl --yes
conda install -c conda-forge matplotlib --yes
