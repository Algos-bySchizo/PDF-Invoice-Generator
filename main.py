from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime
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
# class Item():
#     def __init__(self, name,qty,price):
#         self.name=name
#         self.qty=qty
#         self.price=price
#     def price_cal(self):
#         total_price=self.qty*self.price
#         return total_price
# Dataclass Approach in creating a Class
@dataclass
class Item:
    name:str 
    qty:float 
    price:float  

    def price_cal(self):
       return self.qty*self.price
# Declarative Approach in creating a Class
class Invoice():
    def __init__(self, client):
        self.client=client
        self.items: List[Item] = []
        self.invoice_date=datetime.now()
        self.invoice_number=f"INV-{id(self)}"
        self.tax_rate=0.0
        self.discount=0.0
        self.discount_type=['Flat','Percentage']
    def add_item(self,item):
        self.items.append(item)
    def calculate_subtotal(self):
        subtotal=0
        return sum(item.price_cal() for item in self.items)
        # subtotal=0
        # for item in self.items:
        #     subtotal+=item.price_cal()
        # return subtotal
    def calculate_total(self):
        subtotal=self.calculate_subtotal()
        tax_amount=subtotal*self.tax_rate        
