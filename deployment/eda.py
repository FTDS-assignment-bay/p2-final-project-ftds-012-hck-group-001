# import library
import pandas as pd 
import numpy as np
import streamlit as st 

# library for visualization
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px

# Function untuk menjalankan streamlit model prediksi
def run():
    # Title
    st.title('Exploring Vehicle Damage Data')
    st.write('---')


    # Menampilkan gambar dengan menggunakan CSS untuk mengatur tata letak
    st.markdown(
        """
        <style>
        .centered {
            display: flex;
            justify-content: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Menampilkan gambar di tengah halaman
    st.markdown(
        """
        <div class="centered">
            <img src='https://static.vecteezy.com/system/resources/previews/002/275/202/non_2x/car-insurance-concept-can-be-used-as-protection-for-vehicle-damage-and-emergency-risks-illustration-vector.jpg'  alt='Diabetes Image' style='width:800px;height:400px;'>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write('---')


    # Menampilkan teks dalam dua baris dan menggunakan CSS untuk menata tata letaknya
    st.markdown(
        """
        <style>
        .two-columns {
            display: flex;
            justify-content: space-between;
        }
        </style>
        <div class="two-columns">
            <div> Welcome to the EDA page! <br><br>
                Here, we present an exploratory data analysis aimed at understanding the factors that contribute to vehicle damage in insurance claims. 
                Through the use of relevant statistical techniques and data visualization, we seek to identify patterns and relationships between various variables related to vehicle damage in the context of insurance claims. 
                Our primary goal is to provide valuable insights for insurance companies, policy makers and the general public in efforts to prevent and manage risks associated with vehicle damage. 
                With an emphasis on an in-depth understanding of risk factors, we hope this page will serve as a source of useful information and motivate proactive action to improve traffic safety and compliance, 
                and to reduce vehicle damage.  <br><br>
                Thank you for joining us on this journey!
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write('---')


    # Subjudul
    st.write('## Dataframe')

    # loading dataset
    df = pd.read_csv('C:/Users/Muhammad Hafidz Adit.DESKTOP-6IPGJGG/Documents/Hacktiv8/Project-Akhir/p2-final-project-ftds-012-hck-group-001/deployment/car_insurance_clean.csv')

    # menampilkan dataframe
    st.dataframe(df)
    st.write('---')

    # Bab Visualisasi
    st.write('## Exploratory Data Analysis (EDA)')

    # Judul visualisasi 1
    st.write('### Vehicle Damage Distribution Chart')
    # opsi 1
    opsi1 = st.selectbox('Select column : ', ('gender', 'married', 'education','type_of_vehicle','vehicle_year','outcome') \
                        , format_func=lambda x: "gender" if x == "gender" else ('married' if x == 'married' else ('education' if x == 'education' else \
                        ('type of vehicle' if x == 'type_of_vehicle' else ('outcome' if x == 'outcome' else ('vehicle year' if x == 'vehicle_year' else x))))))
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x=opsi1, data=df, palette='Set2')
    plt.title(f'{opsi1} distribution')
    plt.xlabel('')
    st.pyplot(fig)

    # Insight 1
    st.write('Insight :')
    if opsi1 == 'gender':
        st.write('More accidents tend to occur in men than women, because men tend to take more risks when driving than women, such as driving at high speeds, dangerous maneuvers, and ignoring traffic rules.')
    elif opsi1 == 'married':
        st.write('Married people have more accidents than those who are not married.')
    elif opsi1 == 'education':
        st.write('People with a high school level of education have more accidents than people with a university level of education.')
        st.write('Drivers with a high school education are usually younger and have less driving experience than those with a university level. Lack of driving experience at a younger age can increase the risk of accidents.')
    elif opsi1 == 'type_of_vehicle':
        st.write('Sports cars have more accidents than other types of cars, because sports car drivers often drive at higher speeds and make more aggressive maneuvers compared to sedan, hatchback and SUV drivers.') 
    elif opsi1 == 'vehicle_year':
        st.write('There are more accidents in cars aged before 2015 than after 2015, perhaps because these cars are not equipped with the advanced safety technologies available in cars after 2015, such as airbags, ABS systems, and passive safety systems, which can help reduce injuries in accidents.')
    elif opsi1 == 'outcome':
        st.write('In data on vehicle insurance users, it can be seen that the number of rejected claims is greater than the claims accepted. This shows that there are several main reasons why claims are rejected, including non-fulfillment of the conditions in the insurance policy, minor vehicle damage and repair costs below the minimum claim limit set by insurance, as well as indications of fraud or violations of insurance policies.')
        
    st.write('---')

# Judul visualisasi 2
    st.write('### Vehicle Damage Relation Chart')
    # opsi 2
    opsi2 = st.selectbox('Select column : ', ('gender', 'driving_experience','type_of_vehicle') \
                        , format_func=lambda x: "gender" if x == "gender" else ('driving experience' if x == 'driving_experience' else ('type of vehicle' if x == 'type_of_vehicle'  else x)))
    
    fig, ax = plt.subplots(figsize=(10, 6)) 
    ax = sns.countplot(x=opsi2, hue='outcome', data=df, linewidth=2.5)
    plt.title(f'the relationship between {opsi2} and outcome')
    ax.bar_label(ax.containers[0])
    ax.bar_label(ax.containers[1])
    st.pyplot(fig)


    # Insight 2
    st.write('Insight :')
    if opsi2 == 'gender':
        st.write('In terms of differences in the ratio of denied and accepted claims between men and women in vehicle insurance, perhaps women submit different claims than men, both in terms of frequency and type. For example, if women tend to file claims for smaller damages or incidents that do not involve accidents, those claims may be easier to process and accept.')
    elif opsi2 == 'driving_experience':
       st.write('In the difference between the ratio of denied and accepted claims between drivers experience in vehicle insurance, drivers with driving experience between 0-9 years may have less experience, which can increase the risk of accidents. Insurance may be stricter in denying claims from these drivers due to the higher risk of accidents. On the other hand, drivers with driving experience over 30 years may have higher experience and more experience in driving, which may increase their awareness of risks and reduce the possibility of accidents. It may also increase their awareness of how to avoid accidents, so they may be more likely to file a valid claim.')
    elif opsi2 == 'type_of_vehicle':
        st.write('In the difference in the ratio of denied (denied) and accepted (accepted) claims between vehicle types, supercars have the largest difference with deny more than acc due to the higher risk of accidents and lack of safety aids. In contrast, SUVs have the smallest margin with deny over ACC due to their taller and wider design, more complete safety aids, and higher driver awareness of risks.')
    
    st.write('---')

    # FINAL PROJECT
    st.markdown(
        """
        <style>
        .right-align {
            text-align: right;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        "<p class='right-align'>Final Project Group 01</p>",
        unsafe_allow_html=True
    )


# Menjalankan perintah setelah halaman terbuka
if __name__ == "__main__":
    run()
