class Tracking:
    def __init__(self, num: int, location, status, details):
        self.num = num
        self.location = location
        self.status = status
        self.details = details
    
    def __str__(self):
        return self.location, self.status, self.details
    def __repr__(self):
        return f'Shipment tracking n°: {self.num}, Current location: {self.location}, Delivery status: {self.status}, Recipient details: {self.details}'

class Table:
    def __init__(self, lenght):
        self.lenght = lenght
        self.table = [None] * lenght
    
    def hash(self, value):
        return value % self.lenght
    
    def push(self, value: Tracking):
        key = self.hash(value.num)
        if self.table[key] is None:
            self.table[key] = [value]
        else:
            self.table[key].append(value)
            
    def search(self, num: int):
        key = self.hash(num)
        return self.table[key]
    
    def remove(self, value: Tracking):
        key = self.hash(value.num)
        self.table.pop(key)

if __name__ == '__main__':
    table = Table(10)
    tracking1 = Tracking(1, 'Waiting for input', 'Undefined', 'Shop 1')
    tracking2 = Tracking(2, 'Entry completed', '10 day deadline', 'Shop 2')
    tracking3 = Tracking(3, 'Out', 'Fulfilled', 'Shop 3')
    tracking4 = Tracking(4, 'Went out to the store', 'Concluded', 'Shop 1')
    table.push(tracking1)
    table.push(tracking2)
    table.push(tracking3)
    table.push(tracking4)
    print(table.search(2))