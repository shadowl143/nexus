class RiderVM:
    def __init__(self, id:int, name:str, bike_type:str):
        self._id = id
        self._name = name
        self._bike_type = bike_type

        
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, value:int) -> None:
        self._id = value

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value:str) -> None:
        self._name = value.capitalize()
        
    @property
    def bike_type(self) -> str:
        return self._bike_type
    @bike_type.setter
    def bike_type(self, value:str) -> None:
        self._bike_type = value.capitalize()


