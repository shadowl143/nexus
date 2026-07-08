from nexus_desktop.tkinter.view_model.rider_vm import RiderVM
rider_table = [
    RiderVM(id=1, name="nombre1", bike_type="datos1"),
    RiderVM(id=2, name="nombre2", bike_type="datos2"),
    RiderVM(id=3, name="nombre3", bike_type="datos3"),
    RiderVM(id=4, name="nombre4", bike_type="datos4"),
]
class RiderService:
    def __init__(self):
        pass

    def rider_list(self) -> list[RiderVM]:
        return [(r.id, r.name, r.bike_type) for r in rider_table]

    def save_rider(self, rider: RiderVM):
        # Aquí deberías implementar la lógica para guardar el rider
        # Por ejemplo, agregarlo a la lista si no existe
        if rider not in rider_table:
            rider_table.append(rider)

    def remove_rider(self, rider: RiderVM):
        # Método para eliminar un rider de la lista
        if rider in rider_table:
            rider_table.remove(rider)