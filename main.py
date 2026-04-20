app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello WOrld"}

@app.get ("/teste")
async def funcaoteste():
    return {"teste": "deu certo"}