from nexus_desktop.tkinter.services.rider.rider_service import RiderService
from nexus_desktop.tkinter.view_model.rider_vm import RiderVM

class RiderController:
    
    def __init__(self, riderService: RiderService):
        self.riderService = riderService

    def rider_list(self) -> list[RiderVM]:
        rider = self.riderService.rider_list()
        return rider