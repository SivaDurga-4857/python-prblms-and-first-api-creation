from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Calculator API"}


@app.get("/add")
def add_numbers(a: int, b: int,c: int):
    return {
        "number1": a,
        "number2": b,
        "number3": c,
        "result": a + b
    }
@app.get("/subtract")
def subtract_numbers(a: int,b: int,c: int):
    return {
        "number1": a,
        "number2": b,
        "number3": c,
        "result": a - b - c
    }
@app.get("/multiplication")
def multiplication_numbers(a: int,b: int):
    return {
        "number1": a,
        "number2": b,
        "number3": c,
        "result": a * b * c
    }

    
    