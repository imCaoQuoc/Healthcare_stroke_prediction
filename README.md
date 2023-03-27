# **HEALTHCARE - STROKE PREDICTION**

---

### **INTRODUCTION**
This Github repository contains a machine learning project on stroke prediction. The project includes data preprocessing, exploratory data analysis, feature engineering, and model selection. The aim of this project is to predict stroke based on factors such as gender, age, heart disease,...and provide a demo application using Streamlit.

Technologies I used:
  - [Tensorflow](https://www.tensorflow.org/) to build a deep learning model.
  - [Sci-kit learn](https://www.tensorflow.org/) to preprocessing data.
  - [Streamlit](https://streamlit.io/) to build a simple web.
  - [Streamlit documentation](https://www.youtube.com/playlist?list=PLtqF5YXg7GLmCvTswG32NqQypOuYkPRUE) to learn the basic of streamlit

---

### **INSTALLATION**
I highly recommend you using Google Colab to run the healthcare_stroke_prediction.ipynb file because it already has backages and libraries I use. But if you want to run on your local machine, following the instruction below.
  - Install essential libraries and packages:
  
  ```
  pip install -r requirements.txt
  ```
  
  - Run demo:
  
  ```
  streamlit run demo.py
  ```

---

### **DATA INFORMATION** 

The source of our data is referred from Kaggle: [CLICK HERE](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)

This data has 12 columns, which stayed for 12 factors may cause stroke. These factors include: 
  - `id`: unique identifier
  - `gender`: "Male", "Female" or "Other"
  - `age`: age of the patient
  - `hypertension`: 0 if the patient doesn't have hypertension, 1 if the patient has hypertension
  - `heart_disease`: 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease
  - `ever_married`: "No" or "Yes"
  - `work_type`: "children", "Govt_jov", "Never_worked", "Private" or "Self-employed"
  - `Residence_type`: "Rural" or "Urban"
  - `avg_glucose_level`: average glucose level in blood
  - `bmi`: body mass index
  - `smoking_status`: "formerly smoked", "never smoked", "smokes" or "Unknown"
  - `stroke`: 1 if the patient had a stroke or 0 if not

Data has 5110 samples, where it has 201 missing values in column `bmi`.

