from nexus_desktop.tkinter.view_model.entregas_vm import EntregaVm

rider_table = [
    EntregaVm(_id=1, _rider_id=1, _distance=1.12, _co2=1.12),
    EntregaVm(_id=2, _rider_id=1, _distance=1.12, _co2=1.12),
    EntregaVm(_id=3, _rider_id=1, _distance=1.12, _co2=1.12),
    EntregaVm(_id=4, _rider_id=1, _distance=1.12, _co2=1.12),
]


class EntregaService:
    def __init__(self):
        pass

    def entregas_list(self) -> list[EntregaVm]:
        model = [(r.id, r.rider_id, r.distance, r.co2) for r in rider_table]
        return model

    def save_entrega(self, rider: EntregaVm):
        if rider not in rider_table:
            rider_table.append(rider)

    def remove_entrega(self, rider: EntregaVm):
        if rider in rider_table:
            rider_table.remove(rider)
