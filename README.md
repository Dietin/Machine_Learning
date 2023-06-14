# Machine_Learning

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Dataset](#dataset)
* [Model Result](#model-results)

## General info
This repository will contain information about the models that used by Diet!n applicatin to predicts user's calories need per day with an approach using linear regression

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

[Data processing](https://github.com/Dietin/Machine_Learning/blob/main/Data/after_preprocessing.csv) is carried out as follows: 
1. Deleting the bmi_tags column and labels
2. Changing the category column to numeric
3. Changing the unit for the user's height column and rounding off the user's weight column

## Model Results
**Model's Summary**
![image](https://github.com/Dietin/Machine_Learning/assets/84969259/9e825104-7f1b-4cee-8a00-bc539e5dda8b)

**Model's Metric**

This is how our [final model](https://github.com/Dietin/Machine_Learning/blob/main/Model/notebook%5B2%5D.ipynb) training history
![WhatsApp Image 2023-06-14 at 19 07 44](https://github.com/Dietin/Machine_Learning/assets/99454751/3e2476a4-e7d6-4f9b-929c-a2a03f8bb7d8)

**Model's Testing**
![image](https://github.com/Dietin/Machine_Learning/assets/84969259/ac344a91-bf87-468c-9af7-0ea2293fee0f)
![image](https://github.com/Dietin/Machine_Learning/assets/84969259/fea23927-e32d-4989-8b83-9dc12a7b9275)
This is a result of calorie prediction from our model :
![image](https://github.com/Dietin/Machine_Learning/assets/84969259/39de99f3-2003-4d84-a8d4-7d5e8b9ebf64)


**Final Model's Flow for Daily Calorie Needs Prediction**
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
