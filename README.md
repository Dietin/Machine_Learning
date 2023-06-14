# Machine_Learning

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Dataset](#dataset)
* [Model Architecture](#model-architecture)
* [Model Results](#model-results)

## General info
This repository will contain information about the models that used by Diet!n applicatin to predicts user's calories need per day.

## Technologies
* Tensorflow 
* Pandas
* Numpy
* Seaborn

## Setup
The setup to build and training the model : 
* Jupyter Notebook
* Install latest version of libraries (Tensorflow, Pandas, Numpy, Seaborn, etc)
* Prepare dataset with .csv format

## Dataset
The dataset that we used comes from [Kaggle's site](https://www.kaggle.com/datasets/vechoo/diet-plan-recommendation) which is a collection of calorie data to maintain weight based on age, weight, height, gender, BMI, BMR and activity level

## Model Architecture
**Data Pre-Processing**

Data processing is carried out as follows: 
1. Deleting the bmi_tags column and labels
2. Changing the category column to numeric
3. Changing the unit for the user's height column and rounding off the user's weight column

**Train History**



## Model Results
**Model's Flow for Daily Calorie Needs (Linear Regression)**

1. User inputs personal data according to the data in the training (age, gender, weight, height, activity)
2. User chooses priority or goals which is maintain, loose or gain their weight
3. Model will gives prediction of calorie needs based on user priorities
     - For example, if you want to be fat, then input how many kg you are fat, then predict calories based on the data entered + additional weight data
4. Output that will model gives is number of calories in a day based on user priority

**Pipeline for Daily Calorie Needs**

1. Look for datasets related to calories
2. Prep-rocessing dataset
3. Create model
4. Training model
5. Evaluate model
6. Retrain model
7. Deploy model
