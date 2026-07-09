from dataclasses import dataclass
from source.entities.Employee import Employee
@dataclass
class Car:
    marque:str
    moteur:str
    power:str
    vitesse:str
    def upgrade(self) -> None:
        self.power = "700 hp"
        self.vitesse = 210
    def __str__(self) -> str:
        return f"marque : {self.marque}\nmoteur : {self.moteur}\npower : {self.power}\nvitesse : {self.vitesse}km/h"

prado = Car(marque="Toyota", moteur="V8-biturbo", power="640 hp", vitesse=190)
prado.upgrade()
print(prado)

class Voiture:
    def __init__(self, marque, moteur):
        self.marque = marque
        self.moteur = moteur
    
ram = Voiture("Dodge", "Helcat TRX")
print(ram.moteur)


def add_ok():
    try:
        john = Employee(name="ok",email="nbjsf",salary=10,post="cs")
    except Exception as e:
        print(e)
    

add_ok()