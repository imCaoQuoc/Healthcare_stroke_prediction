import tensorflow as tf
import streamlit as st
import pandas as pd

model = tf.keras.models.load_model("D:\stroke\PROJECT\model.h5", compile=False)
st.title("STROKE PREDICTION WEB")

lst = []
columns_name = ['gender', 'age', 'hypertension', 'heart_disease', 'ever_married',
       'work_type', 'Residence_type', 'avg_glucose_level', 'bmi',
       'smoking_status']
st.sidebar.title("Making some examination")
gender = st.sidebar.selectbox("Select gender", ("Male", "Female", "Other"))
if gender == "Male":
    lst.append(1)
elif gender == "Female":
    lst.append(0)
else:
    lst.append(2)
age = st.sidebar.slider("How old are you ?", 0, 120)
lst.append(age)
hypertension = st.sidebar.selectbox("Do you have hypertension ?", ("Yes", "No"))
if hypertension == "Yes":
    lst.append(1)
else: 
    lst.append(0)
heart_disease = st.sidebar.selectbox("Do you have heart disease ?", ("Yes", "No"))
if heart_disease == "Yes":
    lst.append(1)
else:
    lst.append(0)
married = st.sidebar.selectbox("Do you ever married ?", ("Yes", "No"))
if married == "Yes":
    lst.append(1)
else:
    lst.append(0)
work = st.sidebar.selectbox("What is your work type ?", ("Private", "Self-employed", "Children", "Government job", "Never worked"))
if work == "Private":
    lst.append(2)
elif work == "Self-employed":
    lst.append(3)
elif work == "Children":
    lst.append(4)
elif work == "Government job":
    lst.append(0)
else:
    lst.append(1)
residence_type =  st.sidebar.selectbox("What is your residence type ?", ("Urban", "Rural"))
if residence_type == "Urban":
    lst.append(1)
else:
    lst.append(0)
glucose = st.sidebar.slider("Choosing your average glucose level:", 0, 272)
lst.append(glucose)
bmi = st.sidebar.slider("Choosing your bmi:", 0, 50)
lst.append(bmi)
smoke = st.sidebar.selectbox("Do you smoke ?", ("Never smoked", "Formely smoker", "Smokes", "Unknown"))
if smoke == "Never smoked":
    lst.append(2)
elif smoke == "Formely smoker":
    lst.append(1)
elif smoke == "Smokes":
    lst.append(3)
else:
    lst.append(0)
start = st.sidebar.button("Start")
if start:
    X = pd.DataFrame([lst], columns=columns_name)

    y = model.predict(X)
    formatted_num = "{:.2f}".format(float(y[0]*100))
    st.write(f"You have {formatted_num} % to have a stroke")