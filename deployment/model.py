import streamlit as st
import pandas as pd
import numpy as np
import pickle
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import tensorflow_hub as hub
import matplotlib.pyplot as plt

from PIL import Image
import tensorflow as tf


 #load model
with open('xgb_base_model.pkl', 'rb') as file:
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
    
    gender_label_to_val = {
        'Male': 'male',
        'Female': 'female'
    }
    
    education_label_to_val = {
        'University': 'university',
        'High School': 'high school',
        'None': 'none'
    }

    type_of_vehicle_label_to_val = {
        'Sports Car': 'sports car', 
        'Hatchback': 'hatchback', 
        'Sedan': 'sedan', 
        'SUV': 'suv'
    }
    
    income_label_to_val = {
        'Middle Class': 'middle class',
        'Upper Class': 'upper class',
        'Working Class': 'working class',
        'Poverty': 'poverty'
    }
    vehicles_ownership_label_to_val = {
        'Yes': 1.0,
        'No': 0.0
    }
    married_label_to_val = {
        'Yes': 1.0,
        'No': 0.0
    }

    children_label_to_val = {
        'Yes': 1.0,
        'No': 0.0
    }
    
    def predict_damage(image_data):
        # Process image and predict damage type using the second model
        image = load_img(image_data, target_size=(224, 224))
        img_array = img_to_array(image)
        img_array = tf.expand_dims(img_array, 0)  # Create a batch

        # Normalize the image
        img_array = img_array / 255.0

        # Make prediction
        predictions = model2.predict(img_array)

        # Get the predicted class
        predicted_class = np.argmax(predictions)

        labels = ['crack', 'dent', 'glass shatter', 'lamp broken', 'scratch', 'tire flat']

        predicted_label = labels[predicted_class]

        return predicted_label

    with st.form('form'):
        ID = st.number_input('Customer ID', min_value=1, step=1)
        age = st.selectbox('Age Group', ('16-25','26-39', '40-64', '65+'))
        gender = st.radio("Gender",list(gender_label_to_val.keys()))
        driving_experience = st.selectbox('Driving Experience', ('0-9y','10-19y','20-29y','30y+'))
        education = st.selectbox("Education",list(education_label_to_val.keys()))
        income = st.selectbox("Income",list(income_label_to_val.keys()))
        credit_score = st.number_input('Credit Score', min_value=0.0 ,max_value=1.0, step = 0.1)
        vehicle_ownership = st.radio("Vehicle Ownership",list(vehicles_ownership_label_to_val.keys()))
        vehicle_year = st.selectbox('Vehicle Year', ('Before 2015','After 2015'))
        type_of_vehicle = st.selectbox('Type of Vehicle', ('Sports Car', 'Hatchback', 'Sedan', 'SUV'))
        married = st.radio("Married",list(married_label_to_val.keys()))
        children = st.radio("Having a Children?",list(children_label_to_val.keys()))
        postal_code = st.number_input('Postal Code', min_value=10238, step=1)
        annual_mileage = st.number_input('Annual Mileage', min_value=0.0,step=1000.0)
        speeding_violations = st.number_input('Speeding Violations', value=0,step=1)
        duis = st.number_input('Driving Under the Influence', value=0,step=1)
        past_accidents = st.number_input('Past Accidents', value=0,step=1)
        file = st.file_uploader("Upload the Damaged Vehicle Image", type=["jpg", "png"])
        submit = st.form_submit_button('Predict')

    if submit:
        st.markdown('---')

        if file == None:
            st.markdown('### **Please Upload Your Damaged Vehicle Image** :warning:')
        else:
            st.markdown('### Vehicle Damage Detection')
            st.image(file)
            prediction = predict_damage(file)

            prediction_disp = {
                'crack': 'Crack', 
                'dent': 'Dent', 
                'glass shatter': 'Glass Shatter', 
                'lamp broken': 'Lamp Broken', 
                'scratch': 'Scratch', 
                'tire flat': 'Tire Flat'
            }
            st.markdown(f'Vehicle damage detected as **{prediction_disp[prediction]}**.')
            st.markdown('---')

            data_raw = {
                'ID': ID,
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
                'Issue': prediction_disp[prediction]
            }
                                

            data_inf_display = pd.DataFrame([data_raw])
            st.markdown('### Inputted Data')
            st.dataframe(data_inf_display)

            data_cleaned = {
                'id': ID,
                'age': age,
                'gender': gender_label_to_val[gender],
                'driving_experience': driving_experience,
                'education': education_label_to_val[education],
                'income': income_label_to_val[income],
                'credit_score': credit_score,
                'vehicle_ownership': vehicles_ownership_label_to_val[vehicle_ownership],
                'vehicle_year': vehicle_year,
                'type_of_vehicle': type_of_vehicle_label_to_val[type_of_vehicle],
                'married': married_label_to_val[married],
                'children': children_label_to_val[children],
                'postal_code': postal_code,
                'annual_mileage': annual_mileage,
                'speeding_violations': speeding_violations,
                'duis': duis,
                'past_accidents': past_accidents,
                'issue': prediction
            }

            data_inf = pd.DataFrame([data_cleaned])

            score = model1.predict(data_inf)
            if score == 0:
                st.markdown(f'Insurance claim for Customer ID - {ID} is **DENIED**.')
            else:
                st.markdown(f'Insurance claim for Customer ID - {ID} is **ACCEPTED**.')
                


if __name__ == "__main__":
    run()
