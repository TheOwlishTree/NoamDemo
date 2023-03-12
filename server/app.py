from fastapi import FastAPI
from server.calculator.endpoint import calc_router

app = FastAPI()
app.include_router(calc_router, prefix="/calculator", tags=["calculator"])


@app.get("/")
async def sanity():
    return {"Sanity": "Check"}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, port=8080)