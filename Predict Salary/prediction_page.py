import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]
le_age = data['le_age']


def show_predict_page():
    st.title("Salary Prediction")
    st.write("### we need some information to predict the salary")

    countries = [
        'United States',
        'India',
        'Germany',
        'United Kingdom',
        'Canada',
        'France',
        'Brazil',
        'Spain',
        'Netherlands',
        'Australia',
        'Poland',
        'Italy',
        'Russian Federation',
        'Sweden',
        'Turkey',
        'Switzerland',
        'Norway',
    ]

    educations = [
        'Master’s degree',
        'Bachelor’s degree',
        'Post grad',
        'Less than a Bachelors'
    ]

    ages = [
        '25-34 years old',
        '35-44 years old',
        '45-54 years old',
        '18-24 years old',
        '55-64 years old',
        '65 years or older',
        'Under 18 years old',
        'Prefer not to say'
    ]

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education", educations)
    age = st.radio("Age", ages)

    experience = st.slider("Years of experience",
                           min_value=0, max_value=50, value=3)

    ok = st.button("Calculate Salary")
    if ok:
        X = np.array([[country, education, experience, age]])
        X[:, 0] = le_country.transform(X[:, 0])
        X[:, 1] = le_education.transform(X[:, 1])
        X[:, 3] = le_age.transform(X[:, 3])
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")
