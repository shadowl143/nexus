from nexus_desktop.PyQt.services.entregas.entrega_service import EntregaService
from nexus_desktop.PyQt.view_model.entregas_vm import EntregaVm


class EntregaController:

    def __init__(self, rider_service: EntregaService):
        self.rider_service = rider_service

    def rider_list(self) -> list[EntregaVm]:
        rider = self.rider_service.entregas_list()
        return rider

    def save_rider(self, rider: EntregaVm):
        self.rider_service.save_entrega(rider)

    def remove_rider(self, rider: EntregaVm):
        self.rider_service.remove_entrega(rider)
