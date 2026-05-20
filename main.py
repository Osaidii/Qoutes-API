import json
from fastapi import FastAPI
import uvicorn
from random import randint

app = FastAPI()
FILE = "quotes.json"

def get():
    temp_list: list = []
    with open (FILE) as f:
        temp_list = json.load(f)
    num_of_quotes = len(temp_list)
    random_num = randint(0, num_of_quotes - 1)
    quote = temp_list[random_num]
    print(quote) # changes this

def add_quote():
    num_of_quotes = input("How many quotes will you add: ") # changes
    num_of_quotes = int(num_of_quotes)
    temp_list: list = []
    with open (FILE, "r") as f:
        temp_list = json.load(f)
    for i in range(num_of_quotes):
        quote: str = ""
        quote = input("Enter your quote: ") # changes
        temp_list.append(quote)
    with open (FILE, "w") as f:
        json.dump(temp_list, f)

def remove_quote():
    num_of_quotes = input("How many quotes will you remove: ") # changes
    num_of_quotes = int(num_of_quotes)
    temp_list: list = []
    with open (FILE) as f:
        temp_list = json.load(f)
        print(temp_list)
    removing_list: list = []
    for i in range(num_of_quotes):
        quote_num = input("Enter the quote index: ") # changes
        quote_num = int(quote_num)
        removing_list.append(quote_num)
    removing_list.sort(reverse = True)
    for i in range(len(removing_list)):
        if 0 <= i >= len(temp_list):
            temp_list.pop(removing_list[i])
    with open (FILE, "w") as f:
        json.dump(temp_list, f)
    

