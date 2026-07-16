import streamlit as st
 
from database.mongodb import students_collection 

st.title("student registration")

First_name = st.text_input(

    "First name"
)

Last_name = st.text_input(

    "Last name"
)

Email = st.text_input(

    "Email"
)

Course = st.text_input(

    "Course"
)
if st.button("Register Student"):

    students_collection.insert_one({

        "First_name": First_name,

        "Last_name": Last_name,

        "email": Email,

        "course": Course
    })

    st.success("sucessfully")