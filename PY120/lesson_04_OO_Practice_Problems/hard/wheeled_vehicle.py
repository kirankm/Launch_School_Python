class TyrePressureMixin:
    def tire_pressure(self, tire_index):
        return self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure

class VehicleRangeMixin:
    def range(self):
        return self.fuel_capacity * self.fuel_efficiency

class WheeledVehicle:
    def __init__(self,
                 tire_list,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.tires = tire_list
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

class Auto(TyrePressureMixin, VehicleRangeMixin, WheeledVehicle):
    def __init__(self):
        # 4 tires with various tire pressures
        super().__init__([30, 30, 32, 32], 50, 25.0)

class Motorcycle(TyrePressureMixin, VehicleRangeMixin, WheeledVehicle):
    def __init__(self):
        # 2 tires with various tire pressures
        super().__init__([20, 20], 80, 8.0)

class Cataraman(VehicleRangeMixin):
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        self.number_propellers = number_propellers
        self.number_hulls = number_hulls
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

class MotorBoat(Cataraman):
    def __init__(self,kilometers_per_liter,
                liters_of_fuel_capacity):
        super().__init__(1, 1, kilometers_per_liter, liters_of_fuel_capacity)