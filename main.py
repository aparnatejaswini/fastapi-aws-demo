from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return "CI/CD pipeline established"