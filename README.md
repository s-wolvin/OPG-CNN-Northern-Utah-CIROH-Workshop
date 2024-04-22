# OPG-CNN-Northern-Utah-CIROH-Workshop
## Problem Statement
Operational models predicting precipitation often lack the grid spacing to resolve fine-scale precipitation variations within complex terrain. To improve forecasts, precipitation in complex terrain is often downscaled using orographic precipitation gradients (OPGs), which are the relationships between precipitation and elevation. The scripts offered here describe the process of predicting these OPGs using a convolutional neural network from ECMWF's ERA5 for the Northern Utah region. 

## Project Description
This workshop offers participants an introduction to convolutional neural networks (CNNs) for their application in hydro-meteorology. Core concepts to be covered include the layers within a CNN, the learning process of the CNN, and techniques related to Explainable AI (XAI). The hands-on portion of the workshop focuses on customizing a CNN through hyperparameter exploration, adjusting CNN layers, and manipulating inputs. Participants will gain an understanding of CNN architecture, practical skills in customizing a CNN, and the apply the models in Northern Utah for downscaling ERA5 data for the quantity of liquid precipitation. Participants will use GitHub to fork the repository and clone to their machine using the CIROH Cloud Computing environment.

### Datasets
The datasets used are:
* [Bohne et al. 2020](https://doi.org/10.1175/JHM-D-19-0229.1) - Climatology of orographic precipitation gradients of the western United States, subsetted to the Northern Utah region of winter (DJF) events from 1988 to 2017.
* [ECMWF ERA5](https://doi.org/10.1002/qj.3803) - Hourly data on pressure levels and single levels from 1940 to present, subsetted to latitudes 36N-45N, longitudes -119W -106W, of winter (DJF) events from 1988 to 2017.


# Creating a Stable CONDA Environment
- Go to your home directory

cd ~

- Create an envs directory

mkdir envs




