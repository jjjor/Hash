class Marketplace:
    def __init__(self, id: int, data, demand, rating):
        self.id = id
        self.data = data
        self.demand = demand
        self.rating = rating
    
    def __str__(self):
        return self.id, self.data, self.demand, self.rating
    def __repr__(self):
        return f'ID: {self.id}, Sales data: {self.data}, Demand: {self.demand}, Client ratings: {self.rating}'
    

class Table:
    def __init__(self, lenght):
        self.lenght = lenght
        self.table = [None] * lenght
    
    def hash(self, value):
        return value % self.lenght
    
    def push(self, value: Marketplace):
        key = self.hash(value.id)
        if self.table[key] is None:
            self.table[key] = [value]
        else:
            self.table[key].append(value)
            
    def search(self, id: int):
        key = self.hash(id)
        return self.table[key]
    
    def remove(self, value: Marketplace):
        key = self.hash(value.id)
        self.table.pop(key)

if __name__ == '__main__':
    table = Table(10)
    marketplace1 = Marketplace(1, 'Incomplete sales', 'Low', 'Negatives')
    marketplace2 = Marketplace(2, 'Sales almost completed', 'Good', 'Improvements')
    marketplace3 = Marketplace(3, 'Sales completed', 'Very good', 'Excellent')
    marketplace4 = Marketplace(4, 'Outsold', 'Excellents', 'Excellent')
    table.push(marketplace1)
    table.push(marketplace2)
    table.push(marketplace3)
    table.push(marketplace4)
    print(table.search(4))