# OPG-CNN-Northern-Utah-CIROH-Workshop
### Problem Statement
Operational models predicting precipitation often lack the grid spacing to resolve fine-scale precipitation variations within complex terrain. To improve forecasts, precipitation is often downscaled using statistical or dynamical downscaling. These methods have limitations, such as insufficient event-to-event variability or the high computational demand of running fine-scaled model simulations. We've proposed downscaling precipitation in complex terrain from orographic precipitation gradients (OPGs), which represent the relationship between precipitation and elevation, predicted from a Convolutional Neural Network (CNN). The workshop scripts provided here detail the process of predicting OPGs in northern UT using a CNN trained on ECMWF's ERA5. 

### Workshop Description
This workshop offers participants an introduction to convolutional neural networks (CNNs) for their application in hydro-meteorology. Core concepts to be covered include the layers within a CNN, the learning process of the CNN, and techniques related to Explainable AI (XAI). The hands-on portion of the workshop focuses on customizing a CNN through hyperparameter exploration, adjusting CNN layers, and manipulating inputs. Participants will gain an understanding of CNN architecture, practical skills in customizing a CNN, and the apply the models in Northern Utah for downscaling ERA5 data for the quantity of liquid precipitation. Participants will use GitHub to fork the repository and clone to their machine using the CIROH Cloud Computing environment.

### Datasets
* [Bohne et al. 2020](https://doi.org/10.1175/JHM-D-19-0229.1) - Climatology of orographic precipitation gradients of the western United States, subsetted to the Northern Utah region of winter (DJF) events from 1988 to 2017.
* [ECMWF ERA5](https://doi.org/10.1002/qj.3803) - Hourly data on pressure levels and single levels from 1940 to present, subsetted to latitudes 36°N – 45°N, longitudes -119°W – -106°W, of winter (DJF) events from 1988 to 2017. This dataset was accessed through the publicly available Copernicus Climate Change Service (C3S) Climate Data Store (CDS). The ERA5 predictor variables were processed from 6-hourly data on [pressure levels](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-pressure-levels?tab=overview) and 6-hourly data on [single levels](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=form).


# Getting Started:
### 1. Fork the Repository to your GitHub

Navigate to the top-right corner of the page, select Fork.

![image](https://github.com/s-wolvin/OPG-CNN-Northern-Utah-CIROH-Workshop/assets/34422513/6b96d86e-1ebb-4652-b0f8-c37fb46da3ca)

Confirm the details of this page and select Create Fork.

![image](https://github.com/s-wolvin/OPG-CNN-Northern-Utah-CIROH-Workshop/assets/34422513/343220ce-ec44-40be-a712-f21eaa2dbccc)

### 2. Start CIROH JupyterHub
Select the `Medium` server, which contains 11GB of RAM and 4 CPUs.

In the Image dropdown, select `Other`.

Input the following to the `Custom Image` text box. This selects a custom image containing the Python environment needed.
```
quay.io/benlee7411/devcon24:FIRST-INITIAL-LAST-NAME
```
Then select `Start Server`.

### 3. Clone Repository to your Machine
Identify a location where you would like to work in a development environment. Using the command prompt, change your working directory to this folder and git clone your forked OPG-CNN-Northern-Utah-CIROH-Workshop repository.
```
git clone https://github.com/YOUR-USERNAME/OPG-CNN-Northern-Utah-CIROH-Workshop
```

### 4. Register the Kernel with JupyterHub
Check that the notebook environment is activated.
```
conda activate notebook
```
Register the environment's kernel with JupyterHub.
```
python -m ipykernel install --user --name=YOUR-ENV-NAME
```

### 5. Selecting Kernel
From the Jupyter Notebooks, select your kernel.


# Folder Structure
    .
    ├── datasets                   # Pre-processed ERA5, facets, observed precipitation, and OPGs
    ├── figures                    # Figures created from the scripts/ files
    ├── pre-processing             # Pre-process datasets from the western CONUS to northern UT
    ├── scripts                    # CNN Workshop scripts
    ├── README.md                 
    ├── environment_jupyter.yml    # Environment file
    └── requirements.txt           # Environment requirements file

