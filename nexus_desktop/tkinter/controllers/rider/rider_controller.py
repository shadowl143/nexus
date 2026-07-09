from nexus_desktop.tkinter.services.rider.rider_service import RiderService
from nexus_desktop.tkinter.view_model.rider_vm import RiderVM


class RiderController:

    def __init__(self, rider_service: RiderService):
        self.rider_service = rider_service

    def rider_list(self) -> list[RiderVM]:
        rider = self.rider_service.rider_list()
        return rider

    def rider_select(self) -> list[RiderVM]:
        rider = self.rider_service.rider_select()
        return rider

    def save_rider(self, rider: RiderVM):
        self.rider_service.save_rider(rider)

    def remove_rider(self, rider: RiderVM):
        self.rider_service.remove_rider(rider)
