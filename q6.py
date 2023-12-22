class Product:
    def __init__(self, id: int, control):
        self.id = id
        self.control = control
    
    def __str__(self):
        return self.control
    def __repr__(self):
        return f'ID: {self.id}, Quality control: {self.control}'
    
class Table:
    def __init__(self, lenght):
        self.lenght = lenght
        self.table = [None] * lenght
    
    def hash(self, value):
        return value % self.lenght
    
    def push(self, value: Product):
        key = self.hash(value.id)
        if self.table[key] is None:
            self.table[key] = [value]
        else:
            self.table[key].append(value)
            
    def search(self, id: int):
        key = self.hash(id)
        return self.table[key]
    
    def remove(self, value: Product):
        key = self.hash(value.id)
        self.table.pop(key)
        
if __name__ == '__main__':
    table = Table(10)
    product1 = Product(1, 'product damaged')
    product2 = Product(2, 'product aproved')
    product3 = Product(3, 'product aproved')
    product4 = Product(4, 'failed product')
    table.push(product1)
    table.push(product2)
    table.push(product3)
    table.push(product4)
    print(table.search(4))