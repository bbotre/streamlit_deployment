import streamlit as st
import pickle

# Set the page configuration
st.set_page_config(page_title="Loan Eligibility Form", page_icon="💸", layout="centered")

# Apply custom CSS for a colorful theme
st.markdown(
    """
    <style>
    
    body {
        background-color: black;
        color: white; /* Dark grey text for readability */
    }
    .stApp {
    background-color: #c2b9bd;
    
    }
    .reportview-container {
        background-color: #ffffff; /* White background for the main content area */
        color: #333333; /* Dark grey text for readability */
    }
    .sidebar .sidebar-content {
        background-color: #ffebcd; /* Blanched almond background for the sidebar */
        color: #333333; /* Dark grey text for readability */
    }
    .stButton>button {
        background-color: #4CAF50; /* Green background for the button */
        color: white; /* White text on the button */
    }
    .stSelectbox>div>div>div {
        background-color: #f5f5dc; /* Beige background for the select boxes */
    }
    .stNumberInput>div>div>div {
        background-color: #f5f5dc; /* Beige background for the number inputs */
    }
    </style>
    """,
    unsafe_allow_html=True
)
#model open
model_pickle = open("./classifier.pkl", "rb")
clf = pickle.load(model_pickle)

# Set up the title and description
st.title("Loan Eligibility Form")
st.write("Please fill out the details below:")

# Create input fields for the form
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0, step=1000)
loan_amount = st.number_input("Loan Amount", min_value=0, step=500)
credit_history = st.selectbox("Credit History", ["Yes", "No"])

gender1 = gender
married1 = married
credit_history1 = credit_history

if gender == "Male":
    gender = 1
else:
    gender = 0 

if married == "Yes":
    married = 1
else:
    married = 0 

if credit_history == "Yes":
    credit_history = 1
else:
    credit_history = 0

result = clf.predict([[gender, married, applicant_income, loan_amount, credit_history]])

if result == 0:
        pred = "Rejected"
else:
        pred = "Approved"


print("debug 00", result)
# Display the entered information
st.write("## Summary")
st.write(f"**Gender:** {gender1}")
st.write(f"**Married:** {married1}")
st.write(f"**Applicant Income:** {applicant_income}")
st.write(f"**Loan Amount:** {loan_amount}")
st.write(f"**Credit History:** {credit_history1}")

# Add some interactivity with a button
if st.button('Submit'):
    st.write("Your loan status is", pred)
    # st.write(f"Preprocessed inputs are : {gender, married, applicant_income, loan_amount, credit_history}")