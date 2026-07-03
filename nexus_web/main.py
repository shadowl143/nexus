from fastapi import FastAPI
from routers import rider_routers

app = FastAPI()

# Conectas el router a tu aplicación principal
app.include_router(rider_routers.router)