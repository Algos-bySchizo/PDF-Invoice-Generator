from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime
# Declarative Approach in creating a Client Class
# class Client():
#     def __init__(self, name,email,address,contact: Optional[int]=None):
#         self.name=name
#         self.email=email
#         self.address=address
#         self.contact=contact
# Dataclass Approach in creating a Client Class
@dataclass
class Client:
    name:str 
    email:str 
    address:str 
    contact:Optional[int]=None 
# Declarative Approach in creating an Item Class
# class Item():
#     def __init__(self, name,qty,price):
#         self.name=name
#         self.qty=qty
#         self.price=price
#     def price_cal(self):
#         total_price=self.qty*self.price
#         return total_price

# Dataclass Approach in creating an Item Class
@dataclass
class Item:
    name:str 
    qty:float 
    price:float  

    def price_cal(self):
       return self.qty*self.price
# Declarative Approach in creating the Inovice Class
class Invoice():
    def __init__(self, client):
        self.client=client
        self.items: List[Item] = []
        self.invoice_date=datetime.now()
        self.invoice_number=f"INV-{id(self)}"
        self.tax_rate=0.0
        self.discount=0.0
        self.discount_type='flat'
    def add_item(self,item):
        self.items.append(item)
    def remove_item(self,index):
        # if index>=0 and index<len(self.items):
        self.items.pop(index) if (0 <= index < len(self.items)) else None
    def set_tax_rate(self,rate):
        self.tax_rate=rate
    def set_discount(self,amount,discount_type):
        self.discount=amount
        self.discount_type=discount_type

#Functional Programming that will be used in PDF generation and Report Generation in Terminal and JSON format!
def calculate_subtotal(self):
    return sum(item.price_cal() for item in self.items)
    # subtotal=0
    # for item in self.items:
    #     subtotal+=item.price_cal()
    # return subtotal
def apply_discount(subtotal,discount,discount_type):
    if discount_type=='percentage':
        return subtotal*(1-discount)
    return subtotal-discount
def apply_tax(amount,tax_rate):
    return 
    def calculate_total(self):
        subtotal=self.calculate_subtotal()
        tax_amount=subtotal*self.tax_rate
        if self.discount_type.lower()=='flat':
            discount_amount=self.discount
        elif self.discount_type.lower()=='percentage':
            discount_amount=subtotal*(self.discount/100)
        else:
            discount_amount=0
        total=subtotal+tax_amount-discount_amount
        return total
    def format_currency(amount):
