from nexus_desktop.PyQt.services.entregas.entrega_service import EntregaService
from nexus_desktop.PyQt.view_model.entregas_vm import EntregaVm


class EntregaController:

    def __init__(self, entrega_service: EntregaService):
        self.entrega_service = entrega_service

    def entregas_list(self) -> list[EntregaVm]:
        entrega = self.entrega_service.entregas_list()
        return entrega

    def save_entrega(self, entrega: EntregaVm):
        self.entrega_service.save_entrega(entrega)

    def remove_entrega(self, entrega: EntregaVm):
        self.entrega_service.remove_entrega(entrega)
