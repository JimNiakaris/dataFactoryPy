class Car:
    def __init__(self,cc:int, hp: float,color:str,brand:str,modelName:str):
        self.cc = cc
        self.hp = hp


    def presentCar(self):
        return f"The new car is {self.brand} {self.modelName} {self.hp} {self.cc}"

newCar = Car(cc=1400,hp=150,color="Red",brand="AlfaRomeo",modelName="Tonale")

