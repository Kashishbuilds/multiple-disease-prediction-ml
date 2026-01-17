# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 20:46:16 2026

@author: Acer
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# ================= LOAD MODELS =================
diabetes_model = pickle.load(open("saved_models/diabetes_model.sav", "rb"))
heart_disease_model = pickle.load(open("saved_models/heart_disease_model.sav", "rb"))
parkinsons_model = pickle.load(open("saved_models/parkinsons_model.sav", "rb"))


# ================= SIDEBAR =================
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# ================= DIABETES =================
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Glucose = st.text_input('Glucose Level')
        Insulin = st.text_input('Insulin Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
        BMI = st.text_input('BMI value')

    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the person')

    if st.button('Diabetes Test Result'):
        try:
            prediction = diabetes_model.predict([[
                float(Pregnancies), float(Glucose), float(BloodPressure),
                float(SkinThickness), float(Insulin), float(BMI),
                float(DiabetesPedigreeFunction), float(Age)
            ]])

            if prediction[0] == 1:
                st.success(' The person is Diabetic')
            else:
                st.success(' The person is Not Diabetic')

        except:
            st.error(' Please enter valid numeric values')

# ================= HEART =================
elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
        trestbps = st.text_input('Resting Blood Pressure')
        restecg = st.text_input('Resting ECG')
        oldpeak = st.text_input('Oldpeak')

    with col2:
        sex = st.text_input('Sex')
        chol = st.text_input('Cholesterol')
        thalach = st.text_input('Maximum Heart Rate')
        slope = st.text_input('Slope')

    with col3:
        cp = st.text_input('Chest Pain Type')
        fbs = st.text_input('Fasting Blood Sugar')
        exang = st.text_input('Exercise Induced Angina')
        ca = st.text_input('CA')

    thala = st.text_input('Thal')

    if st.button('Heart Disease Test Result'):
        try:
            prediction = heart_disease_model.predict([[
                float(age), int(sex), int(cp), float(trestbps),
                float(chol), int(fbs), int(restecg),
                float(thalach), int(exang), float(oldpeak),
                int(slope), int(ca), int(thala)
            ]])

            if prediction[0] == 1:
                st.success(' Heart Disease Detected')
            else:
                st.success('No Heart Disease Detected')

        except:
            st.error(' Please enter valid numeric values')

# ================= PARKINSONS =================
elif selected == 'Parkinsons Prediction':
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        jitter_percent = st.text_input('MDVP:Jitter(%)')
        rap = st.text_input('MDVP:RAP')
        shimmer = st.text_input('MDVP:Shimmer')
        apq3 = st.text_input('Shimmer:APQ3')
        apq = st.text_input('MDVP:APQ')
        hnr = st.text_input('HNR')
        spread1 = st.text_input('spread1')
        d2 = st.text_input('D2')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        jitter_abs = st.text_input('MDVP:Jitter(Abs)')
        ppq = st.text_input('MDVP:PPQ')
        shimmer_db = st.text_input('MDVP:Shimmer(dB)')
        apq5 = st.text_input('Shimmer:APQ5')
        dda = st.text_input('Shimmer:DDA')
        rpde = st.text_input('RPDE')
        spread2 = st.text_input('spread2')
        ppe = st.text_input('PPE')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        ddp = st.text_input('Jitter:DDP')
        nhr = st.text_input('NHR')
        dfa = st.text_input('DFA')

    if st.button("Parkinson's Test Result"):
        try:
            prediction = parkinsons_model.predict([[
                float(fo), float(fhi), float(flo), float(jitter_percent),
                float(jitter_abs), float(rap), float(ppq), float(ddp),
                float(shimmer), float(shimmer_db), float(apq3), float(apq5),
                float(apq), float(dda), float(nhr), float(hnr),
                float(rpde), float(dfa), float(spread1),
                float(spread2), float(d2), float(ppe)
            ]])

            if prediction[0] == 1:
                st.success(" Parkinson's Disease Detected")
            else:
                st.success(" No Parkinson's Disease Detected")

        except:
            st.error(' Please enter valid numeric values')

