def create_inventory(items):
    inventory=dict()
    set_items=set(items)
    for m in set_items:
        v=items.count(m)
        inventory[m]=v 
    return inventory

def add_items(inventory, items):
    set_items=set(items)
    for m in set_items:
        v=items.count(m)
        if n in inventory:
        inventory[m]= inventory[m]+v 
    else:
        inventory[m]=v
    return inventory

def decrement_items(inventory, items):
    set_items=set(items)
    for m in set_items:
        v=items.count(m)
        if m<v:
            inventory[m]=0
        else:
            inventory[m]=inventory[m]- v
    return inventory

def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    return inventory

def list_inventory(inventory):
    lista=[]
    for k,v in inventory.items():
        if v>0:
            elemento=(k,v)
            lista.append(elemento)
