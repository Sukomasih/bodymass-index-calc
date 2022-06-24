from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse

app = FastAPI(title='BMI Calculator API')

## custom default error handeling non zero value input
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str("error input value or URL"), status_code=422)

@app.get("/")
async def bmi(height: float, weight: float):

    ## validate variable value
    if height == 0 and weight == 0:
        raise HTTPException(status_code=404, detail="error input value")
    elif height == 0 or weight == 0:
        raise HTTPException(status_code=404, detail="error input value")

    ## convert cm to m
    conWeight = float(height / 100)
    ## calculate BMI proses
    bmi = round(weight / (conWeight * conWeight), 2)

    ## validate label
    if bmi <= 18.5:
        result = "underweight"
    elif bmi >= 18.5 and bmi <= 24.99:
        result = "normal"
    elif bmi >= 25.0:
        result = "overweight"
    
    ## response rest api
    return JSONResponse(
        content={
            "bmi": bmi,
            "label": result,},
        status_code=200)