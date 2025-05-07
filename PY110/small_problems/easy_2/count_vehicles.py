def count_occurrences(vehicles):
    for vehicle in set(vehicles):
        print(f"{vehicle} => {vehicles.count(vehicle)}")

def count_occurrences_case_insensitive(vehicles):
    vehicles = [vehicle.lower() for vehicle in vehicles]
    for vehicle in set(vehicles):
        print(f"{vehicle} => {vehicles.count(vehicle)}")

                      

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)