from fastapi import FastAPI
from datetime import datetime, date
from typing import Dict
import random

### Create FastAPI instance with custom docs and openapi url
app = FastAPI(docs_url="/api/py/docs", openapi_url="/api/py/openapi.json")

@app.get("/api/py/helloFastApi")
def hello_fast_api():
    return {"message": "Hello from FastAPI"}

@app.get("/api/py/ageCalculator/{birthday}")
def age_calculator(birthday: str) -> Dict[str, str]:
    """
    생년월일을 입력받아 만나이를 계산하는 API

    :param birthday: 생년월일 (형식: YYYY-MM-DD)
    :return: 생년월일 및 만나이를 포함한 JSON 응답
    """
    # random_age = random.randint(0, 100)
    
    today = date.today()
    birth_date = datetime.strptime(birthday, "%Y-%m-%d").date() 
    

    # TODO 생일 지난 여부 관련 로직 코드 작성
    if birth_date.month < today.month or (birth_date.month == today.month and birth_date.day <= today.day):
        age = today.year - birth_date.year
    else:
        age = today.year - birth_date.year - 1


    return {
            "birthday": birthday,
            "age": str(age),
            "basedate": str(today),
            "message": "Age calculated successfully!"
            }
