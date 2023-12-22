class Component:
    def __init__(self, id, status, location, historic):
        self.id = id
        self.status = status
        self.location = location
        self.historic = historic
    
    def __str__(self):
        return f'id: {self.id}, status: {self.status}, location: {self.location}, historic: {self.historic}'

component_table = {}


# add function

def add_component(id, status, location, historic):
    component = Component(id, status, location, historic)
    component_table[id] = component

# update function

def atualizar_componente(id, new_status, new_location, new_historic):
    if id in component_table:
        component_table[id].status = new_status
        component_table[id].location = new_location
        component_table[id].historic = new_historic
    else:
        print("ID not found.")

# search function
        
def search_component(id):
    if id in component_table:
        return component_table[id]
    else:
        print("ID not found.")

add_component(1, 'Self making...', 'A', 'NEW')
add_component(2, 'Self making...', 'A', 'NEW')
add_component(3, 'SOLD', 'NO SECTION', 'No historic')
atualizar_componente(2, 'Produzido', 'Setor B', 'NEW')
atualizar_componente(3, 'SOLD', 'NO SECTION', 'No historic')
search_component(2)
print(search_component(4))