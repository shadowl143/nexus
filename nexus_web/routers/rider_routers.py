from fastapi import APIRouter
from controller import rider_controller

router = APIRouter()

@router.get("/usuarios")
def leer_rider():
    return rider_controller.obtener_rider_db()