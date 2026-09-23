from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/students")
def get_students():
    return {
        "students": [
            {
                "id": 1,
                "name": "Siva",
                "branch": "EEE"
            },
            {
                "id": 2,
                "name": "Ravi",
                "branch": "CSE"
            }
        ]
    }

@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {
        "student_id": student_id,
        "message": f"You requested student {student_id}"
    }