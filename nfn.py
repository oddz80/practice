import datetime
import math

class Warship:
    def __init__(self, name: str, nation: str, date_report: datetime.datetime) -> None:
        self.name = name
        self.nation = nation
        self.date_report = date_report
        
class Braunschweig_corvette(Warship):
    def __init__(self, name: str, nation: str, date_report: datetime.datetime, x_cordinate: float, y_cordinate: float) -> None:
        self.x_cordinate = x_cordinate
        self.y_cordinate = y_cordinate
        super().__init__(name, nation, date_report)
        
    def distance_xy(self, x2: float, y2:float):
        distance = math.sqrt(pow((x2 - self.x_cordinate), 2) + pow((y2 - self.y_cordinate), 2))
        return distance
    
magdeburg = Braunschweig_corvette('Magdeburg', 'Germany', datetime.datetime.now(), 1, 1)
print(magdeburg.distance_xy(4, 5))
        
        

        