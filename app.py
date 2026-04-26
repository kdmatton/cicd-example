from fastapi import FastAPI
import time
import requests
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {'message': [{'error':'some random error'}, {'pass':'it passed'}]}

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)


