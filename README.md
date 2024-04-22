# OPG-CNN-Northern-Utah-CIROH-Workshop
### Problem Statement
Operational models predicting precipitation often lack the grid spacing to resolve fine-scale precipitation variations within complex terrain. To improve forecasts, precipitation in complex terrain is often downscaled using orographic precipitation gradients (OPGs), which are the relationships between precipitation and elevation. The scripts offered here describe the process of predicting these OPGs using a convolutional neural network from ECMWF's ERA5 for the Northern Utah region. 

### Project Description
This workshop offers participants an introduction to convolutional neural networks (CNNs) for their application in hydro-meteorology. Core concepts to be covered include the layers within a CNN, the learning process of the CNN, and techniques related to Explainable AI (XAI). The hands-on portion of the workshop focuses on customizing a CNN through hyperparameter exploration, adjusting CNN layers, and manipulating inputs. Participants will gain an understanding of CNN architecture, practical skills in customizing a CNN, and the apply the models in Northern Utah for downscaling ERA5 data for the quantity of liquid precipitation. Participants will use GitHub to fork the repository and clone to their machine using the CIROH Cloud Computing environment.

#### Datasets
The datasets used are:
* [Bohne et al. 2020](https://doi.org/10.1175/JHM-D-19-0229.1) - Climatology of orographic precipitation gradients of the western United States, subsetted to the Northern Utah region of winter (DJF) events from 1988 to 2017.
* [ECMWF ERA5](https://doi.org/10.1002/qj.3803) - Hourly data on pressure levels and single levels from 1940 to present, subsetted to latitudes 36°N – 45°N, longitudes -119°W – -106°W, of winter (DJF) events from 1988 to 2017. This dataset was accessed through the publicly available Copernicus Climate Change Service (C3S) Climate Data Store (CDS). The ERA5 predictor variables were processed from hourly data on [pressure levels](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-pressure-levels?tab=overview) and hourly data on [single levels](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=form).


## Getting Started:
### Clone Repository
First, identify a location where you would like to work in a development environment. Using the command prompt, change your working directory to this folder and git clone [OPG-CNN-Northern-Utah-CIROH-Workshop](https://github.com/s-wolvin/OPG-CNN-Northern-Utah-CIROH-Workshop). Or clone using GitHub Desktop -> File -> Clone Repository, and paste the link listed below under the URL tab.
```
git clone https://github.com/s-wolvin/OPG-CNN-Northern-Utah-CIROH-Workshop
```
### Create Your Virtual Environment From The Command Line
From your command prompt, go to the home directory.
```
cd ~
```
Create an envs directory to hold your Python environments if you have not done so previously.
```
mkdir envs
```
The command below creates the needed environment, specifically with Python version 3.11.2. Here, the environment is named `CNN_env`, name the environment how you see fit.
```
conda create -n CNN_env python=3.11.2
```
Once Anaconda sets up your environment, activate it using the activate function.
```
conda activate CNN_env
```
Finally, download the list of Python Libraries needed for the workshop using the `requirement.txt` file.
```
pip install -r requirements.txt
```

### Create Your Virtual Environment From The YML File
From your command prompt, go to the home directory.
```
cd ~
```
Create an envs directory to hold your Python environments if you have not done so previously.
```
mkdir envs
```
The command below creates the needed environment and downloads all required Python libraries. The environment will be named `CNN_env`.
```
conda env create -f environment.yml
```
Once Anaconda sets up your environment, activate it using the activate function.
```
conda activate CNN_env
```
To check if the environment was installed correctly, run the following line.
```
conda env list
```








