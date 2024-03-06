import streamlit as st
import eda
import model

navigasi = st.sidebar.selectbox('Page Selector :', 
                                ('Home Page','Model Prediksi', 'EDA'))

if navigasi == 'Home Page':
    st.header('Welcome to InsureWise')
    st.subheader('Your Trusted Partner for Vehicle Insurance')

    st.image('https://r2.easyimg.io/8zf0odixl/insurewise.png', use_column_width=True)

    st.markdown("InsureWise is a leading provider of vehicle insurance solutions, prioritizing safety, convenience, and customer satisfaction. With a strong dedication to service quality and innovation, InsureWise has become a preferred choice for vehicle owners seeking reliable protection.")

    st.markdown("### Company Profile of InsureWise:")

    st.markdown("- **Leadership in the Industry:** InsureWise has emerged as a pioneer in the vehicle insurance industry, offering smart and dependable solutions. By staying abreast of the latest trends in technology and risk analysis, InsureWise consistently delivers protection tailored to customer needs.")

    st.markdown("- **Security and Protection:** InsureWise is committed to unwavering security for vehicles and the safety of their owners. Through comprehensive insurance products, InsureWise provides protection against various risks, including damages due to accidents and vehicle theft.")

    st.markdown("- **Excellent Customer Service:** InsureWise believes that excellent customer service is key to success. A team of professional and experienced individuals stands ready to assist customers at every step, from explaining product details to efficiently processing claims.")

    st.markdown("- **Openness and Transparency:** InsureWise prioritizes openness and transparency in every customer interaction. Information about insurance policies, claims procedures, and service protocols is readily available and clearly communicated to customers.")

    st.markdown("- **Sustainable Environmental Commitment:** As part of its corporate social responsibility, InsureWise actively participates in environmental conservation efforts. Through environmentally-friendly policies and sustainable programs, InsureWise contributes to the protection and restoration of vulnerable ecosystems.")

    st.markdown("Through its leadership in the industry, focus on security and protection, excellent customer service, openness and transparency, and sustainable environmental commitment, InsureWise continually strives to be a reliable partner in meeting the insurance needs of its customers.")
    st.markdown('----')


    st.write('Thank you for visiting our homepage.')
    st.write('Please explore our menu options to access additional features, such as Exploratory Data Analysis (EDA) or Insurance Prediction.')
    
    st.caption('Developed by: Angger Rizky Firdaus, Basyira Sabita, Muhammad Hafidz Adityaswara')



elif navigasi == 'Model Prediksi':
    model.run()
else :
    eda.run()