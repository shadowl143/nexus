class EntregaVm:
    def __init__(
        self, _id: int, _rider_id: int, _name: str, _distance: float, _co2: float
    ):
        self._name = _name
        self._id = _id
        self._rider_id = _rider_id
        self._distance = _distance
        self._co2 = _co2

    # --- GETTER Y SETTER PARA ID ---
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    # --- GETTER Y SETTER PARA ID ---
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    # --- GETTER Y SETTER PARA RIDER_ID ---
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def rider_id(self, value: str):
        self._name = value

    # --- GETTER Y SETTER PARA DISTANCE ---
    @property
    def distance(self) -> float:
        return self._distance

    @distance.setter
    def distance(self, value: float):
        self._distance = value

    # --- GETTER Y SETTER PARA CO2 ---
    @property
    def co2(self) -> float:
        return self._co2

    @co2.setter
    def co2(self, value: float):
        self._co2 = value
