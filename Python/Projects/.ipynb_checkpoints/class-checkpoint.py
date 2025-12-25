class Car:
    totalCar=0      ## belongs to Car class not to object
    def __init__(self,brand,model): ## instructor (Object of class)
        self.__brand=brand
        self.__model=model
        Car.totalCar+=1             ## to exccess the local variables

    def get_brand(self):
        return self.__brand       ## add __ in front of variable to make it private

    def printData(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or diesel"

    @staticmethod
    def general_def():              ## To exccess methids using class name and wthout self paramter
        return f"Cars are Good!...{Car.totalCar}"

    @property
    def model(self):
        return f'{self.__model} !...'

class ElectricCar(Car):             ## inheritance
    def __init__(self, brand, model,batterySize):
        super().__init__(brand, model)       ## Super used to get upper class info
        self.batterySize=batterySize

    def fuel_type(self):          ## same methods in parent and child class is know as polimorphism
        return "Electric Charge"


myTesla = ElectricCar("Tesla","ModleS","85kWh")
# print(myTesla.general_def())
# print(myTesla.fuel_type())
# print(myTesla.printData())

myCarObj= Car("toyato","corolla")
# print(myCarObj.printData())
newCar=Car("NewBrand","modelNo")
#newCar.model="anotherModel"
# print(newCar.model)
# newCar=Car("NewBrandds","mdaodelNo")
# print(newCar.general_def())             ## static methods
# print(Car.general_def())
# print(newCar.fuel_type())
# print(Car.totalCar)                   ## to exccess the local variables(class variable)

# print(isinstance(myTesla,Car))
# print(isinstance(myTesla,ElectricCar))     ## is myTesla belongs to Car and Electricar classes

class Battery:
    def battery_info(self):
        return f'this is battery'

class Engine:
    def engine_info(self):
        return f'this is Engine'

class ElectricCarNew(Battery,Engine,Car):   ## multiple inheritance
    pass     # When the pass statement is executed, nothing happens, but it allows the code to run without errors in places where a statement is syntactically required

newTeslaCar=ElectricCarNew("Brands","models")
print(newTeslaCar.engine_info())
print(newTeslaCar.battery_info())
