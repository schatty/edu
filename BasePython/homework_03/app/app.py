from fastapi import FastAPI, status


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from root!"}


@app.get("/ping", status_code=status.HTTP_200_OK)
def return_pong():
    return {"message": "pong"}