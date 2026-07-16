from pymongo import MongoClient


try:
    MONGO_URI="mongodb+srv://<db_username>:jan210@cluster0.xx8grmp.mongodb.net/"

    client = MongoClient(MONGO_URI)

    client.admin.command("ping")

    db = client["ssus123"]
     
    students_collection = db["students"]
    marks_collection = db["marks"]
    attendance_collection = db["attendance"]
    bmi_collection = db["bmi_reports"]

    print("MongoDB Connected Sucessfully")

except Exception as e:
    print("MongoDB Error:",e)
