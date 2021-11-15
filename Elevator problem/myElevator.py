class myElevator:

    def __init__(self, id: int, speed: float, close_time: float, open_time: float, start_time: float, stop_time: float):
        self.id = id
        self.speed = speed
        self.close_time = close_time
        self.open_time = open_time
        self.start_time = start_time
        self.stop_time = stop_time
        self.call_list = []
        self.curr_time = 0

    def get_id(self) -> int:
        return self.id

    def set_id(self, id: int):
        self.id = id

    def get_speed(self) -> float:
        return self.speed

    def set_speed(self, speed: float):
        self.speed = speed

    def get_close_time(self) -> float:
        return self.close_time

    def set_close_time(self, close_time: float):
        self.close_time = close_time

    def get_open_time(self) -> float:
        return self.open_time

    def set_open_time(self, open_time: float):
        self.open_time = open_time

    def get_start_time(self) -> float:
        return self.start_time

    def set_start_time(self, start_time: float):
        self.start_time = start_time

    def get_stop_time(self) -> float:
        return self.stop_time

    def set_stop_time(self, stop_time: float):
        self.stop_time = stop_time

    def __str__(self):
        return f"Elevetor : Id: {self.id}, Speed: {self.speed}, CloseTime: {self.close_time}, OpenTime: {self.open_time}, StarTime: {self.start_time},StopTime: {self.stop_time} "

    def __repr__(self):
        return f"Elevetor : Id: {self.id}, Speed: {self.speed}, CloseTime: {self.close_time}, OpenTime: {self.open_time}, StarTime: {self.start_time},StopTime: {self.stop_time} "