from pymongo import MongoClient


try:
    MONGO_URI="mongodb+srv://jankunwarmeravi02_db_user:jan210@cluster0.gthur1c.mongodb.net/?appName=Cluster0"

    client = MongoClient(MONGO_URI)

    client.admin.command("ping")

    db = client["ssus"]
     
    students_collection = db["students"]
    marks_collection = db["marks"]
    attendance_collection = db["attendance"]
    bmi_collection = db["bmi_reports"]

    print("MongoDB Connected Sucessfully")

except Exception as e:
    print("MongoDB Error:",e)