import streamlit as st
import pandas as pd
import datetime
import requests
import json

from fastsql import create_user, delete_user, update_user, get_all_users

# page configuration
st.set_page_config(page_title="My Streamlit App", page_icon=":smiley:", layout="wide", initial_sidebar_state="expanded")

st.title("Streamlit - This is Home")
# st.header("")
# st.subheader("")
# st.text("Streamlit Text Example")
# st.markdown("Streamlit Markdown Example")
# st.write("Streamlit Write Example")
st.write("Current Date and Time:", datetime.datetime.now())

st.sidebar.header("Sidebar")
st.sidebar.write("Please select a page from the list below.")

# set API URL to loclhost for testing purposes
API_URL = "http://127.0.0.1:8000/"

# check if API is reachable
def check_api():
    try:    
        response = requests.get(API_URL)
        response.raise_for_status()  # Check if the request was successful
        st.success("API is reachable!")
    except requests.exceptions.RequestException as e:
        st.error(f"API is not reachable: {e}")


# function for API call (fetch data)
def fetch_all_users():
    try:
        response = requests.get(f"{API_URL}users/")
        response.raise_for_status()  # Check if the request was successful
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data from API: {e}")
        return []


def display_data(data):
    if data:
        # Ensure data is a list
        if isinstance(data, dict):
            data = [data]
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.warning("No data to display.")

def display_all_users():
    st.subheader("All Users")
    data = fetch_all_users()
    display_data(data)


def create_user():
    st.subheader("Create a New User")
    loginid = st.text_input("Login ID")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    email = st.text_input("Email")
    
    if st.button("Create User"):
        if loginid and name and age and email:
            user_data = {
                "loginid": loginid,
                "name": name,
                "age": age,
                "email": email
            }
            try:
                response = requests.post(f"{API_URL}users/", json=user_data)
                response.raise_for_status()  # Check if the request was successful
                st.success(f"User '{loginid}' created successfully!")
            except requests.exceptions.RequestException as e:
                st.error(f"Error creating user: {e}")
        else:
            st.warning("Please fill in all fields to create a user.")

def update_user():
    loginid = st.text_input("Login ID of the user to update")
    name = st.text_input("New Name (leave blank to keep unchanged)")
    age = st.number_input("New Age (leave blank to keep unchanged)", min_value=0)
    email = st.text_input("New Email (leave blank to keep unchanged)")
    
    if st.button("Update User"):
        if loginid:
            user_data = {}
            if name:
                user_data["name"] = name
            if age:
                user_data["age"] = age
            if email:
                user_data["email"] = email
            
            if user_data:
                try:
                    response = requests.put(f"{API_URL}users/{loginid}", json=user_data)
                    response.raise_for_status()  # Check if the request was successful
                    st.success(f"User '{loginid}' updated successfully!")
                except requests.exceptions.RequestException as e:
                    st.error(f"Error updating user: {e}")
            else:
                st.warning("Please provide at least one field to update.")
        else:
            st.warning("Please enter the Login ID of the user to update.")

def delete_user():
    st.subheader("Delete a User")
    loginid = st.text_input("Login ID of the user to delete")
    
    if st.button("Delete User"):
        if loginid:
            try:
                response = requests.delete(f"{API_URL}users/{loginid}")
                response.raise_for_status()  # Check if the request was successful
                st.success(f"User '{loginid}' deleted successfully!")
            except requests.exceptions.RequestException as e:
                st.error(f"Error deleting user: {e}")
        else:
            st.warning("Please enter the Login ID of the user to delete.")


# Page routing
page = st.sidebar.selectbox("Select a page", ["Home", "Get All Users", "Create User", "Update User", "Delete User"])

if page == "Get All Users":
    display_all_users()
if page == "Create User":
    create_user()
if page == "Update User":
    st.subheader("Update an Existing User")
    update_user()
if page == "Delete User":
    delete_user()



