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

**Train Model**

## Model Results
**Prediksi kalori harian (Linear Regression)**

1. Input data diri sesuai data yang di training (umur, jenis kelamin, berat, tinggi badan, aktivitas)
2. Pilih prioritas => gemukin, standar, kurusin
3. Prediksi kebutuhan kalori berdasarkan prioritas user
    - Misal, jika ingin gemukin, maka input gemukin nya berapa kg, kemudian lakukan prediksi kalori berdasarkan data yang diinputkan + data berat tambahannya
4. Output : jumlah kalori dalam sehari dan kebutuhan kalori per 3 sesi (pagi, siang dan malam) berdasarkan prioritas user
5. Cari rekomendasi resep sesuai selera user

**Pipeline untuk prediksi kalori harian**

1. Cari dataset yang berhubungan dengan kalori
2. Preprocessing dataset
3. Create model
4. Training model
5. Evaluate model
6. Retrain model
7. Deploy model
