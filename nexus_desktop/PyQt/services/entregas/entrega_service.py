from nexus_desktop.PyQt.view_model.entregas_vm import EntregaVm

entrega_table = [
    EntregaVm(_id=1, _name="Ana Torres", _rider_id=1, _distance=4.2, _co2=0.85),
    EntregaVm(_id=2, _name="Luis Mendoza", _rider_id=1, _distance=1.12, _co2=1.12),
    EntregaVm(_id=3, _name="Carla Ruiz", _rider_id=1, _distance=1.12, _co2=1.12),
    EntregaVm(_id=4, _name="Diego Paz", _rider_id=1, _distance=1.12, _co2=1.12),
]


class EntregaService:
    def __init__(self):
        pass

    def entregas_list(self) -> list[EntregaVm]:
        model = [(r.id, r.name, r.distance, r.co2) for r in entrega_table]
        return model

    def save_entrega(self, rider: EntregaVm):
        if rider not in entrega_table:
            entrega_table.append(rider)

    def remove_entrega(self, rider: EntregaVm):
        if rider in entrega_table:
            entrega_table.remove(rider)
