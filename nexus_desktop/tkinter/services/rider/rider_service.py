from nexus_desktop.tkinter.view_model.rider_vm import RiderVM

rider_table = [
    RiderVM(id=1, name="Ana Torres", bike_type="electric"),
    RiderVM(id=2, name="Luis Mendoza", bike_type="cargo"),
    RiderVM(id=3, name="Carla Ruiz", bike_type="standard"),
    RiderVM(id=4, name="Diego Paz", bike_type="electric"),
    RiderVM(id=4, name="Marina Solis", bike_type="cargo"),
]


class RiderService:
    def __init__(self):
        pass

    def rider_list(self) -> list[RiderVM]:
        model = [(r.id, r.name, r.bike_type) for r in rider_table]
        return model

    def rider_select(self) -> list[RiderVM]:
        model = [r for r in rider_table]
        return model

    def save_rider(self, rider: RiderVM):
        if rider not in rider_table:
            rider_table.append(rider)

    def remove_rider(self, rider: RiderVM):
        if rider in rider_table:
            rider_table.remove(rider)
