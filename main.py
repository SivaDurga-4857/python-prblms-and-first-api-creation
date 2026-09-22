from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/students")
def get_students():
    return{
        "students": ["siva","vishnu","vijay"]
    }