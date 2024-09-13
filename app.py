import streamlit as st
import pandas as pd
import numpy as np
import joblib  # or import pickle
from sklearn.preprocessing import StandardScaler
from PIL import Image
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load the trained model
model = joblib.load('model.pkl')

# st.set_page_config(page_title="Heart Disease Prediction", page_icon="👩‍⚕️",layout='wide')

html_temp = """
    <div style="background-color:#3A506B;padding:9px;border-radius:6px">
    <h1 style="color:White;text-align:center;"> Heart Disease Prediction </h1>
    </div>
    """
st.html(html_temp)
# Background image
st.markdown("""
    <style>
    .stApp {
        background-image: url("E:\ML Project\Heart Diease Prediction\Background.jpg");
        background-size: cover;
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit app
##left,right= st.columns([1,3])

# Display the logo

# with left:
   # st.image("Logo.png", width=200)  # Adjust width as needed
##with right:
    # Sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Home", "About", "Heart Disease Prediction","Connect"])

    # Home Section
if selection == "Home":
    st.header("Home")
    background_image = r'E:\ML Project\Heart Diease Prediction\Background.jpg'
    image = Image.open('Background.jpg')

# Display the image in Streamlit
    st.image(image, caption='Sample Image', use_column_width=True)

# Or use forward slashes
# background_image = 'E:/ML Project/Heart Diease Prediction/Background.jpg'

# Use Markdown with inline HTML and CSS to set the background image
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("file://{background_image}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.write("### Welcome to the Heart Disease Prediction App!")
    st.write("Heart disease prediction using machine learning involves building models that can accurately predict the likelihood of heart disease in individuals based on various health indicators and risk factors. These models utilize historical patient data to learn patterns and relationships between features (such as age, cholesterol levels, and blood pressure) and the presence or absence of heart disease.")
    st.markdown( "### Introduction to Heart Disease Prediction")
    st.write("Heart disease is a leading cause of death worldwide. Early detection and prevention are crucial to reducing mortality rates. Machine learning models can assist in predicting heart disease by analyzing patterns in patient data and identifying high-risk individuals.")
    st.markdown("### Importance of Machine Learning in Healthcare")
    st.write("Machine learning (ML) provides advanced tools and techniques to analyze large datasets efficiently, identify hidden patterns, and make predictions with high accuracy. In healthcare, ML models can help in diagnostic processes, predicting disease progression, and personalizing treatment plans.")
    st.markdown("### Conclusion")
    st.write("Heart disease prediction using machine learning is a promising field that can revolutionize healthcare by providing tools for early diagnosis, risk stratification, and personalized treatment planning. With the ongoing advancements in AI and data science, these models will continue to evolve, offering more accurate and actionable insights for clinicians and patients alike.")
    
        # Add your Home content 
        

    # About Section
elif selection == "About":
    st.header("About")
    st.write("This Below Video refers food and excerise to prevent heart disease.")
    # video_file = open('The_best_food_and_exercises_for_heart_health.mp4', 'rb')
    # video_bytes = video_file.read()
    # Video_Fileone = open('E:\ML Project\Heart Diease Prediction\8 Ways to Reduce Your Coronary Artery Disease Risk.mp4','rb')
    # Video_bytesone = Video_Fileone.read()

    # Display the video in the Streamlit app
    st.video("https://www.youtube.com/watch?v=NAaMN_I3mSU")
    # st.video(video_bytesone)
        # Add your About content here

    # Login Section
#elif selection == "Connect with linkedin":
    #st.header("Connect with linkedin")
    #linkedin_url = "https://www.linkedin.com/in/divya-duraisamy-a249bb211/"
    #st.markdown(f"[Connect with me on LinkedIn]({linkedin_url})", unsafe_allow_html=True)   
    #st.write("Please enter your credentials to log in.")
    

    #username = st.text_input("Username")
    #password = st.text_input("Password", type="password")
    #if st.button("Submit"):
        #st.write(f"Username: {username}")
        #st.write(f"Password: {password}")
        # Add your Login content here
elif selection == "Heart Disease Prediction":
    ## st.header("Heart Disease")
   
   ## if st.button("Click here to Predict"):
        ##st.write("Enter the following details to predict heart disease:") 
    c1,c2,c3 = st.columns(3)

    with c1:
        age = st.number_input('Age', min_value=0)
        Gender = st.selectbox('Sex', ['Male', 'Female'])
        chestPain = st.selectbox('Chest Pain Type', [
                    'Typical angina',
                    'Atypical angina',
                    'Non-anginal',
                    'Asymptomatic'
        ])
        trestbps = st.number_input('Resting Blood Pressure', min_value=0)
        st.caption('Enter your resting blood pressure. Normal range is between 150 and 180. Values above 180 may indicate high blood pressure.')
        chol = st.number_input('Cholesterol Level', min_value=0)
        st.caption('Enter your cholestrol level less than 200 mg/dl is normal')
    with c2:
        fbs = st.selectbox('Fasting Blood Sugar', ['Below 120 mg/dl', 'Above 120 mg/dl'])
        st.caption('Enter your Diabetes or Sugar. Normal range is between 150 and 180. Values above 180 may indicate high blood pressure.')
        oldpeak = st.number_input('Depression Induced by Exercise >1.5 - normal', min_value=0.0)
        restecg = st.selectbox('Resting Electrocardiographic Results|Normal', ['Normal', 'ST-T wave abnormality', 'Left ventricular hypertrophy'])
        Name = st.text_input('Enter your Name')
        input_email = st.text_input('Enter your email address')
    with c3:
        thalach = st.number_input('Maximum Heart Rate Achieved| 120 to 208 - normal', min_value=0)
        exang = st.selectbox('Exercise Induced Angina', ['No', 'Yes'])
        slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])
        ca = st.selectbox('Number of Major Vessels Colored by Fluoroscopy |3 , 0 normal', [0, 1, 2, 3])
        thal = st.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversable Defect'])

            # Map string values to numerical values
            
        sex_map = {
                  'Male':1,
                  'Female':0
        }
        cp_map = {
                    'Typical angina': 0,
                    'Atypical angina': 1,
                    'Non-anginal': 2,
                    'Asymptomatic': 3
            }

        fbs_map = {
                    'Below 120 mg/dl': 0,
                    'Above 120 mg/dl': 1
                }

        restecg_map = {
                    'Normal': 0,
                    'ST-T wave abnormality': 1,
                    'Left ventricular hypertrophy': 2
                }

        exang_map = {
                    'No': 0,
                    'Yes': 1
                }

        slope_map = {
                    'Upsloping': 0,
                    'Flat': 1,
                    'Downsloping': 2
             }

        thal_map = {
                    'Normal': 0,
                    'Fixed Defect': 1,
                    'Reversable Defect': 2
                }

                # Create DataFrame for prediction
        input_data = pd.DataFrame([[age,Gender,chestPain,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]],columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal'])
        
        input_data['sex'].replace(['Male','Female'],[1,0],inplace = True)
        input_data['cp'].replace(['Typical angina','Atypical angina','Non-anginal','Asymptomatic'],[1,2,3,4],inplace = True)
        input_data['fbs'].replace(['Below 120 mg/dl', 'Above 120 mg/dl'],[0,1],inplace=True)
        input_data['restecg'].replace(['Normal','ST-T wave abnormality','Left ventricular hypertrophy'],[0,1,2],inplace=True)
        input_data['exang'].replace(['No', 'Yes'],[0,1],inplace=True)
        input_data['slope'].replace(['Upsloping','Flat','Downsloping'],[0,1,2],inplace=True)
        input_data['thal'].replace(['Normal','Fixed Defect','Reversable Defect'],[0,1,2],inplace=True)
        
        #})
        # Input_data = pd.DataFrameataFrame({
        #             'age': [age],
        #             'sex': [sex_map.get(Gender,sex)],
        #             'cp': [cp_map.get(cp, chestPain)],
        #             'trestbps': [trestbps],
        #             'chol': [chol],
        #             'fbs': [fbs_map.get(fbs, fbs)],
        #             'restecg': [restecg_map.get(restecg, restecg)],
        #             'thalach': [thalach],
        #             'exang': [exang_map.get(exang, exang)],
        #             'oldpeak': [oldpeak],
        #             'slope': [slope_map.get(slope, slope)],
        #             'ca': [ca],
        #             'thal': [thal_map.get(thal, thal)]
                    
        # )}

                    # Preprocess input data
                    # processed_data = preprocess_data(input_data)

                    # Make prediction
        prediction = model.predict(input_data)

                # Show prediction result
    with c2:
        
        if st.button('Predict'):
            if prediction == 1:
                st.write("The model predicts that the person is at risk of heart disease.")
                
            else:
                st.write("The model predicts that the person is not at risk of heart disease.")
                
        def send_email(receiver_email,prediction):
            sender_email = "divyadrsm@gmail.com"
            password = "wosl ezuo zhea sjpw"  # You might want to use OAuth or environment variables for security

            # Create message object
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = "Heart Disease Prediction Result"

            # Body of the email
            body = f"Dear {Name},\n\nYour heart disease prediction result is: {prediction}\n\nStay healthy This result is generated by a machine learning model with 90% accuracy. Please don't be alarmed by a negative result; it is an initial assessment based on the data you provided and should be followed up with professional consultation for further evaluation."
            msg.attach(MIMEText(body, 'plain'))

            # Sending the email
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, password)
                text = msg.as_string()
                server.sendmail(sender_email, receiver_email, text)
                server.quit()
                return "Email sent successfully!"
            except Exception as e:
                return str(e)
                    
        if st.button('Predict and Send Result'):
        
        # Map prediction to a message
            prediction_message = "No Heart Disease Detected  Stay Healthy, Stay Prosperous, and Take Care of Your Well-being!" if prediction == 0 else "Heart Disease Detected Stay Calm and Schedule a Consultation with Your Cardiologist for Further Guidance"
            #prediction_message = "The prediction result for heart disease is: {prediction_result}"


        # Send prediction result via email
            if input_email.endswith('@gmail.com'):  # Optional email validation
                email_status = send_email(input_email, prediction_message)
                st.success(f"Prediction: {prediction_message}")
                st.info(email_status)
            else:
                st.error("Please enter a valid Gmail address.")

elif selection == "Connect":
    st.header("Connect with linkedin")
    linkedin_url = "https://www.linkedin.com/in/divya-duraisamy-a249bb211/"
    st.markdown(f"[Connect with me on LinkedIn]({linkedin_url})", unsafe_allow_html=True)  
    st.write("""
    If you are looking for collaboration on machine learning and AI projects, or need help with a freelancing project, feel free to reach out to me through any of the following:
    """)

    # Contact information
    st.write("### Contact Information")
    st.write("**Gmail**: [divya711yadhav@gmail.com](mailto:divya711yadhav@gmail.com)")
    st.write("**LinkedIn**: [Click here to connect via LinkedIn](https://www.linkedin.com/in/divya-duraisamy-a249bb211/)")
    st.write("**GitHub**: [Click here to view GitHub Profile](https://github.com/divya711yadhav)")

    # Closing message
    st.write("Looking forward to collaborating on innovative technologies and delivering efficient, high-quality projects together.") 
    
