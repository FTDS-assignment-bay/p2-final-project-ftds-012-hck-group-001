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
    st.title('Exploring Vehicle Demage Data')
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
        st.write('The largest number of vehicle insurance users are men, because men tend to take more risks when driving than women, such as driving at high speeds, dangerous maneuvers, and ignoring traffic rules.')
    elif opsi1 == 'married':
        st.write('1. Married people use more vehicle insurance than unmarried people.')
        st.write('2. Married people usually have greater responsibilities, they tend to think about security and financial protection for their partners and children, so vehicle insurance is one way to reduce financial risks that may arise from accidents.')
    elif opsi1 == 'education':
        st.write('1. Insurance users with a high school education level are the largest users, followed by insurance users with a university education level.')
        st.write('2. Insurance users with a high school education may enter the workforce earlier than those pursuing higher education, thereby gaining the financial ability to own a vehicle more quickly.')
    elif opsi1 == 'type_of_vehicle':
        st.write('1. The trend is that more vehicle insurance users own sports cars, followed by sedans, hatchbacks and finally SUVs.')
        st.write('2. Sports cars are often considered high risk and high value, so owners are more likely to insure them to protect their investment.')
        st.write('3. Meanwhile, sedans and hatchbacks have more moderate risks and values, so the number of vehicle insurance users for this type is not as many as sports cars.') 
        st.write('3. SUVs, despite their great popularity, tend to have lower insurance premiums because they are considered safer, but high repair costs and popularity among thieves can affect the number of insurance users for this type.') 
    elif opsi1 == 'vehicle_year':
        st.write('The difference in the number of vehicles insured based on year of manufacture (before vs. after 2015) could be caused by the cost of insurance premiums. Insurance premiums can be higher for new vehicles compared to older vehicles because the replacement value is higher and repairs may be more expensive. This can make new vehicle owners prefer not to insure their vehicles')
    elif opsi1 == 'outcome':
        st.write('In data on vehicle insurance users, claims that are rejected are greater than claims that are accepted, which means: ')
        st.write('1. Many claims are rejected because they do not meet the conditions stated in the insurance policy.')
        st.write('2. Some claims may be rejected because the vehicle damage is minor and the repair costs are below the minimum claim limit set by insurance.')
        st.write('3. Claims may also be rejected if there are indications of fraud or violation of insurance policy.')

    st.write('---')

# Judul visualisasi 2
    st.write('### Vehicle Damage Relation Chart')
    # opsi 2
    opsi2 = st.selectbox('Select column : ', ('gender', 'driving_experience','type_of_vehicle') \
                        , format_func=lambda x: "gender" if x == "gender" else ('driving experience' if x == 'driving_experience' else ('type of vehicle' if x == 'type_of_vehicle'  else x)))
    
    fig, ax = plt.subplots(figsize=(10, 6)) 
    ax = sns.countplot(x=opsi2, hue='outcome', data=df, linewidth=2.5)
    plt.title(f'The Relationship Between {opsi2} and Outcome')
    ax.bar_label(ax.containers[0])
    ax.bar_label(ax.containers[1])
    st.pyplot(fig)


    # Insight 2
    st.write('Insight :')
    if opsi2 == 'gender':
        st.write('1. The largest number of vehicle insurance users are men, because men tend to take more risks when driving than women, such as driving at high speed, dangerous maneuvers, and ignoring traffic rules.')
        st.write('2. In terms of differences in the ratio of denied and accepted claims between men and women in vehicle insurance, perhaps women submit different claims than men, both in terms of frequency and type. For example, if women tend to file claims for smaller damages or incidents that do not involve accidents, those claims may be easier to process and accept.')
    elif opsi2 == 'driving_experience':
        st.write('Differences in the difference between denied and accepted claims between drivers with different levels of experience can be influenced by several factors related to claims risk and propensity.')
        st.write('1. Better Driving Experience, drivers with more than 30 years of experience may have better driving skills and have developed safer habits over the years.')
        st.write('2. Safer Driving Behavior: Drivers with more experience may be more aware of compliance with traffic rules and driving safety principles.')
    elif opsi2 == 'type_of_vehicle':
        st.write('Sports cars tend to have a higher price and value than hatchbacks, sedans, or SUVs. This may make insurance companies more careful in handling claims for sports cars due to the higher financial risks associated with these vehicles.')
    
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
