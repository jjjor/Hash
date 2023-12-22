class Reading:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def __str__(self):
        return self.name

    def __repr__(self):
        return f'ID: {self.id} - Name: {self.name}'

class Sensor:
    def __init__(self, id: int, readings: []):
        self.id = id
        self.readings = readings
    
    def __str__(self):
        return self.readings
    

class Table:
    def __init__(self, lenght):
        self.lenght = lenght
        self.table = [None] * lenght
    
    def hash(self, value):
        return value % self.lenght
    
    def push(self, value: Sensor):
        key = self.hash(value.id)
        if self.table[key] is None:
            self.table[key] = [value.readings]
        else:
            self.table[key].append(value)
            
    def search(self, id: int):
        key = self.hash(id)
        return self.table[key]
    
    def remove(self, value: Sensor):
        key = self.hash(value.id)
        self.table.pop(key)


if __name__ == '__main__':
    table = Table(10)
    reading1 = Reading(1, "reading 1")
    reading2 = Reading(2, "reading 2")
    reading3 = Reading(3, "reading 3")
    sensor1= Sensor(1, [reading1, reading2, reading3])
    sensor2 = Sensor(2, [reading1, reading2, reading3])
    table.push(sensor1)
    table.push(sensor2)
    print(table.search(2))