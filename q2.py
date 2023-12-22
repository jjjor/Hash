class Inventory:
    def __init__(self, id, stock, location, supplier):
        self.id = id
        self.stock = stock
        self.location = location
        self.supplier = supplier
    
    def __str__(self):
        return f'ID: {self.id} Stock: {self.stock} Location: {self.location} Supplier: {self.supplier}'

table_inventory = {}

# add function

def inventory_add(id, stock, location, supplier):
    inventario = Inventory(id, stock, location, supplier)
    table_inventory[id] = inventario

# update function
    
def inveotory_update(id, new_stock, new_location, new_supplier):
    if id in table_inventory:
        table_inventory[id].stock = new_stock
        table_inventory[id].location = new_location
        table_inventory[id].supplier = new_supplier
        
# search function
        
def inventory_search(id):
    if id in table_inventory:
        return table_inventory[id]
    else:
        print("ID não encontrado!")

inventory_add(1, 20, 'Loja 1', 'Jordan')
inventory_add(2, 30, 'Loja 1', 'Jordan')
inveotory_update(2, 60, 'Loja 2', 'Blade')
inventory_search(1)
print(inventory_search(1))