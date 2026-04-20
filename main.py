app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello WOrld"}

@app.get ("/teste1")
async def funcaoteste():
    return {"teste": "deu certo"}