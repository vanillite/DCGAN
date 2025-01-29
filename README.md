# DCGAN project

This repository contains a modified GVGAI framework to create Zelda level datasets, and the Wasserstein GAN with Gradient Penalty to generate new levels.
Instructions for obtaining the Zelda datasets and running the WGAN model are provided below.

Disclaimer:

This project/code uses the GVGAI framework, which was originally developed 
by the Essex University MCTS group. I do not claim any ownership or credit 
for the GVGAI framework. The original source can be found at:
https://github.com/EssexUniversityMCTS/gvgai

## Dependencies
Below you can find the versions of software I used. Other versions may also work.

GVGAI:
* 23.0.1 Java
  
WGAN:
* Python 3.10.11
* PyTorch 2.5.1
* CUDA 12.1


## Generate level descriptions
* Download the GVGAI folder
* Open TestLevelGeneration.java
* Set generatorNames[] to include the desired generators
* Set gameIdx to choose the game to generate levels from (90 is Zelda)
* Set generateLevelPath to specify where the generated levels are saved

## Map Zelda levels to the correct format
Note that the encoder only works for the Zelda level generators. It has not been tested with other games
* Download encoder.py
* Set generators to specify the locations of the GVGAI generated level descriptions
* Run the file to get the correct VGDL encoded levels that can be used to play the game in GVGAI

## Generate the dataset for WGAN using the VGDL levels
* Open GVGAI framework
* Open Play.java
* Set game to choose which game to play
* Set i to choose the amount of levels to generate
* Set level to the location of VGDL encoded levels
* Set screenshotFile to the save location of the screenshots
* Running the file will start and terminate i amount of games while saving the first frame to the specified location

## Running the WGAN-GP model
* Download the WGAN-GP folder
* Open run_all.ipynb
* Adjust hyperparameters if necessary
* Set path to datasets
* Adjust image transformation if necessary
* Open wgan_gp.py
* Modify the generator and critic architecture to be compatible with your data (unless you work with the same Zelda levels)
* Run run_all.ipynb
* Training progress can be observed in the notebook output and the WGAN gemerated levels will be saved to the specified location every 50 steps

## Acknowledgments

Original GVGAI framework:

* [GVGAI](https://github.com/EssexUniversityMCTS/gvgai)

Tutorial used for the WGAP-GP:

* [Rohan-Paul-AI](https://www.youtube.com/watch?v=8bStI2gxHL4&list=PLxqBkZuBynVSRYUck5dFes9kp9M__A8Ad&index=5)
