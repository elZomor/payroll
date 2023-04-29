from fastapi import FastAPI

app = FastAPI()


"""Healthcheck api"""
@app.get("/health")
def health_check():
    return {"status": "ok"}
