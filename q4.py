class Authentication:
    def __init__(self, id: int, credentials, level):
        self.id = id
        self.credentials = credentials
        self.level = level
        
    def __str__(self):
        return self.credentials, self.level
    def __repr__(self):
        return f'ID: {self.id}, Credentials: {self.credentials}, Level: {self.level}'

class Table:
    def __init__(self, lenght):
        self.lenght = lenght
        self.table = [None] * lenght
    
    def hash(self, value):
        return value % self.lenght
    
    def push(self, value: Authentication):
        key = self.hash(value.id)
        if self.table[key] is None:
            self.table[key] = [value]
        else:
            self.table[key].append(value)
            
    def search(self, id: int):
        key = self.hash(id)
        return self.table[key]
    
    def remove(self, value: Authentication):
        key = self.hash(value.id)
        self.table.pop(key)

if __name__ == '__main__':
    table = Table(10)
    authentication1 = Authentication(1, 'Employee', 'Master')
    authentication2 = Authentication(2, 'Packer', 'Jr')
    authentication3 = Authentication(3, 'Cashier', 'Fixed')
    table.push(authentication1)
    table.push(authentication2)
    table.push(authentication3)
    print(table.search(3))