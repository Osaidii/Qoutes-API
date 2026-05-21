import json
from fastapi import FastAPI, HTTPException
import uvicorn
from random import randint

adminkey = "onlyiaddorremove"

app = FastAPI()
FILE = "quotes.json"

@app.get("/get")
def get():
    temp_list: list = []
    with open (FILE) as f:
        temp_list = json.load(f)
    num_of_quotes = len(temp_list)
    random_num = randint(0, num_of_quotes - 1)
    quote = temp_list[random_num]
    return{"quote": quote}

@app.post("/add/{quote}/{admin_key}")
def add(quote: str, admin_key: str):
    if admin_key != adminkey:
        raise HTTPException(status_code=403, detail="Invalid admin key")
        return{"error": "Invalid admin key"}
    temp_list: list = []
    with open (FILE, "r") as f:
        temp_list = json.load(f)
    temp_list.append(quote)
    with open (FILE, "w") as f:
        json.dump(temp_list, f)
    return{"confirmation": "quotes added successfully"}

@app.post("/remove")
def remove(quote: int, admin_key: str):
    if admin_key != adminkey:
        raise HTTPException(status_code=403, detail="Invalid admin key")
        return{"error": "Invalid admin key"}
    temp_list: list = []
    with open (FILE) as f:
        temp_list = json.load(f)
    if 0 <= quote < len(temp_list):
        temp_list.pop(quote)
    with open (FILE, "w") as f:
        json.dump(temp_list, f)
    return{"confirmation": "quotes removed successfully"}
    
@app.get("/list")
def list():
    temp_list: list = []
    with open (FILE, "r") as f:
        temp_list = json.load(f)
    return{"quotes": temp_list}


