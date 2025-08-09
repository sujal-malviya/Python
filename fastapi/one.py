from fastapi import FastAPI

app = FastAPI()

@app.get('/')

def Name():
    return {'data':{'name':'sujal'}}


# steps to install fast FastAPI

# 1) python -m venv venv

# 2) .\venv\Scripts\Activate.ps1

# 3) python -m pip install --upgrade pip

# 4) pip install fastapi uvicron

# 5)uvicron main:app --reload