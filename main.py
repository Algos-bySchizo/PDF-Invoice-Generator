from dataclasses import dataclass
from typing import Optional

# Declarative Approach in creating a Class
# class Client():
#     def __init__(self, name,email,address,contact: Optional[int]=None):
#         self.name=name
#         self.email=email
#         self.address=address
#         self.contact=contact
# Dataclass Approach in creating a Class
@dataclass
class Client:
    name:str 
    email:str 
    address:str 
    contact:Optional[int]=None 
# Declarative Approach in creating a Class
class Item():
    def __init__(self, name,qty,price):
        self.name=name
        self.qty=qty
        self.price=price
    def price_cal(self):
        total_price=self.qty*self.price
        return total_price
# Dataclass Approach in creating a Class
@dataclass
class Item:
    name:str 
    qty:float 
    price:float  

    def price_cal(self):
        total_price=self.qty*self.price
        return total_price