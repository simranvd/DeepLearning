from tensorflow.keras.models import load_model
import pickle
import pandas as pd
import streamlit as st

#Load feature scaling and encoding objects
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('gender_encoder.pkl', 'rb') as f:
    gender_encoder = pickle.load(f)

with open('geography_encoder.pkl', 'rb') as f:
    geography_encoder = pickle.load(f)

#Load the trained model
loaded_model = load_model('churn_model.h5')

# for backend testing
# print(gender_encoder.classes_)
# print(geography_encoder.categories_[0])

#Title
st.title("Customer Churn Prediction")

#Input fields for user to enter customer data
credit_score = st.number_input("Credit Score")
geography = st.selectbox("Geography", geography_encoder.categories_[0])
gender = st.selectbox("Gender", gender_encoder.classes_)
age = st.slider("Age", 18, 92)
tenure = st.slider("Tenure", 0, 10)
balance = st.number_input("Balance")
num_of_products = st.slider("Number of Products", 1, 4)
has_cr_card = st.checkbox("Has Credit Card")
is_active_member = st.checkbox("Is Active Member")
estimated_salary = st.number_input("Estimated Salary")

#input to dataframe
input_data = pd.DataFrame([{'CreditScore': credit_score,
                           'Geography': geography,
                           'Gender': gender_encoder.transform([gender])[0],
                           'Age': age,
                           'Tenure': tenure,
                           'Balance': balance,
                           'NumOfProducts': num_of_products,
                           'HasCrCard': has_cr_card,
                           'IsActiveMember': is_active_member,
                           'EstimatedSalary': estimated_salary,
}])

#Encode the input data
geography_new = pd.DataFrame(geography_encoder.transform(input_data[['Geography']]),columns=geography_encoder.get_feature_names_out(['Geography']))
input_data = pd.concat([input_data.drop('Geography', axis=1),geography_new],axis=1)

# for backend testing
# print(input_data)

# scale and predict
X = scaler.transform(input_data)
prediction = loaded_model.predict(X)

st.write("Prediction Probability: ", prediction[0][0])

if(prediction[0][0] > 0.5):
    st.write("The customer is likely to churn.")
else:
    st.write("The customer is not likely to churn.")