import streamlit as st

from database.mongodb import(
    students_collection,
    attendance_collection
)

st.title(":rainbow[attendance Management]")

students = list(
    students_collection.find()
    )

if not students:

    st.warning(
        "No students available"
    )

    st.stop()

student_names = []

for student in students:

    full_name =(
        student["First_name"]
        +" "
        + student["Last_name"]
    )

    student_names.append(full_name)

selected_student = st.selectbox(
    "select student",
    student_names

)
attendance_date = st.date_input(
    "Attendance Date"
)

status = st.selectbox(

    "status",

    [
        "present",
        "Absent"

    ]
)

if st.button("save attendance"):

    attendance_collection.insert_one({

        "student_name":
        selected_student,

        "date":
        str(attendance_date),

        "status":
        status
    })

    st.success(
        "attendance_saved"
    )
    st.subheader(
        "attendance Records"
    )

    records = list(
        attendance_collection.find()
    )

    for record in records:

        st.write(

            record["student_name"],

            "|",

            record["date"],

            "|",

            record["status"]
        )

    st.subheader(
        "attendance Summary"
    )

    for student in student_names:

        total = attendance_collection.count_documents({

            "student_name":
            student
        })

        present = attendance_collection.count_documents({

            "student_name":
            "present"
        })

        if total > 0:

            percentage =(
                present/total
            ) *100

            st.write(

                f"{student}:"
                f"{round(percentage,2)}%")
            
