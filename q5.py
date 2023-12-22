class Production:
    def __init__(self, num: int, status, details, delivery_time):
        self.num = num
        self.status = status
        self.details = details
        self.delivery_time = delivery_time
    def __str__(self):
        return self.status, self.details, self.delivery_time
    def __repr__(self):
        return f'Product order N°: {self.num}, Status: {self.status}, Details: {self.details}, Delivery time: {self.delivery_time}'

class Table:
    def __init__(self, lenght):
        self.lenght = lenght
        self.table = [None] * lenght
    
    def hash(self, value):
        return value % self.lenght
    
    def push(self, value: Production):
        key = self.hash(value.num)
        if self.table[key] is None:
            self.table[key] = [value]
        else:
            self.table[key].append(value)
            
    def search(self, id: int):
        key = self.hash(id)
        return self.table[key]
    
    def remove(self, value: Production):
        key = self.hash(value.id)
        self.table.pop(key)

if __name__ == '__main__':
    table = Table(10)
    production1 = Production(123, 'Waiting for input', '---', 'Undefined')
    production2 = Production(456, 'Entry made','Checked today', '15 days')
    production3 = Production(789, 'Finished','Product shipped', 'Concluded')
    table.push(production1)
    table.push(production2)
    table.push(production3)
    print(table.search(789))