from pymongo import MongoClient

try:
    MONGO_URI = "mongodb+srv://pu910495_db_user:pankaj2002@cluster0.yvlmiv0.mongodb.net/?appName=Cluster0"
    client = MongoClient(MONGO_URI)

    client.admin.command("ping")

    db = client["ssus"]
    students_collection = db["students"]
    marks_collection = db["marks"]
    attendance_collection = db["attendance"]
    bmi_collection = db["bmi_report"]

    print("MongoDB connected Successfully!")
except Exception as e:
    print("MongoDB error:",e)
