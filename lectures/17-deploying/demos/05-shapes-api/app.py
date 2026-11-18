from fastapi import FastAPI

# create the application; FastAPI handles the HTTP requests and responses for us
app = FastAPI()

# each endpoint is just a Python function. the function's parameters become the query
# parameters of the request, and FastAPI validates their types for us.

@app.get("/circle")
def circle(radius: float):
    return {"shape": "circle", "area": 3.1415 * radius**2}


@app.get("/rectangle")
def rectangle(width: float, height: float):
    return {"shape": "rectangle", "area": width * height}


@app.get("/triangle")
def triangle(base: float, height: float):
    return {"shape": "triangle", "area": 0.5 * base * height}
