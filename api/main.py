from fastapi import FastAPI
from api.router import area, reader, transactions
from api import models
from api.db import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()





app.include_router(area.router)
app.include_router(reader.router)
app.include_router(transactions.router)




