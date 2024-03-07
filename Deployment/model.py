import streamlit as st
import pandas as pd
import numpy as np
import pickle
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import tensorflow_hub as hub
import matplotlib.pyplot as plt

from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model


 #load model
with open('dt_class_model.pkl', 'rb') as file:
        model1 = pickle.load(file)
model2 = tf.keras.models.load_model('tf_vgg16_model_2.h5')
    
def run():
    st.title('InsureWise Cam')
    st.header('Fill the form for prediction')
    st.markdown('----')

    # Display an image
    st.image('https://www.investopedia.com/thmb/H_pXhqJWpT-_B30c0vR_YoOzb2s=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-1012103542-a527d1f380024d5b87c02b255c1d4049.jpg', 
             caption='InsureWise Cam')

    # Form for collecting customer data
    st.subheader('Input Customer Data')
    
    sex_label_to_val = {
        'Male': 'male',
        'Female': 'female'
    }
    
    education_label_to_val = {
        'University': 'university',
        'High School': 'high school',
        'None': 'none'
    }
    Income_label_to_val = {
        'Middle Class': 'middle class',
        'Upper Class': 'upper class',
        'Working Class': 'working class',
        'Poverty': 'poverty'
    }
    vehicles_ownership_label_to_val = {
        'Yes': 1,
        'No': 0
    }
    married_label_to_val = {
        'Yes': 1,
        'No': 0
    }

    children_label_to_val = {
        'Yes': 1,
        'No': 0
    }
    
    def predict_damage(image):
        # Process image and predict damage type using the second model
        image = tf.keras.utils.load_img(image, target_size=(224, 224))
        x = tf.keras.utils.img_to_array(image)
        x = np.expand_dims(x, axis=0)
        classes = model2.predict(x)
        predicted_class_index = np.argmax(classes, axis=1)[0]
        labels = ['crack', 'dent', 'glass shatter', 'lamp broken', 'scratch', 'tire flat']
        predicted_class = labels[predicted_class_index]
        return predicted_class

    with st.form('form'):
        ID = st.text_input('customer ID')
        age = st.selectbox('Age Group', ('16-25','26-39', '40-64', '65+'))
        gender = st.radio("Sex",list(sex_label_to_val.keys()))
        driving_experience = st.selectbox('Driving Experience', ('0-9y','10-19y','20-29y','30y+'))
        education = st.selectbox("Education",list(education_label_to_val.keys()))
        income = st.selectbox("Income",list(Income_label_to_val.keys()))
        credit_score = st.number_input('Credit Score', min_value=0.0 ,max_value=1.0, step = 0.1)
        vehicle_ownership = st.radio("Vehicle Ownership",list(vehicles_ownership_label_to_val.keys()))
        vehicle_year = st.selectbox('Vehicle Year', ('Before 2015','After 2015'))
        type_of_vehicle = st.selectbox('Type of Vehicle', ('Sports Car', 'Hatchback', 'Sedan', 'SUV'))
        married = st.radio("Married",list(married_label_to_val.keys()))
        children = st.radio("Having a Children?",list(children_label_to_val.keys()))
        postal_code = st.text_input('Postal Code')
        annual_mileage = st.number_input('Annual Mileage', min_value=0,step=1000)
        speeding_violations = st.number_input('Speeding Violations', value=0,step=1)
        duis = st.number_input('Driving Under the Influence', value=0,step=1)
        past_accidents = st.number_input('Past Accidents', value=0,step=1)
        file = st.file_uploader("Upload an image", type=["jpg", "png"])
        submit = st.form_submit_button('Predicting customer reimbursement')


    if submit:
        prediction = predict_damage(file)
        data_baru = {
            'Employee ID': ID,
            'Age': age,
            'Gender': gender,
            'Driving Experience': driving_experience,
            'Education': education,
            'Income': income,
            'Credit Score': credit_score,
            'Vehicle Ownership': vehicle_ownership,
            'Vehicle Year': vehicle_year,
            'Type of Vehicle': type_of_vehicle,
            'Married': married,
            'Children': children,
            'Postal Code': postal_code,
            'Annual Mileage': annual_mileage,
            'Speeding Violations': speeding_violations,
            'DUIs': duis,
            'Past Accidents': past_accidents,
            'Issue': prediction
        }
                            

        data_inf = pd.DataFrame([data_baru])
        st.dataframe(data_inf)
        score = model1.predict(data_inf)
        st.write(score)
            


if __name__ == "__main__":
    run()
