from fastapi import FastAPI

import endpoint
import model
from database import engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI()



app.include_router(endpoint.router)
