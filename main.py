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
    # subtotal=0
    # for item in self.items:
    #     subtotal+=item.price_cal()
    # return subtotal
    return sum(item.price_cal() for item in self.items)


def apply_discount(subtotal,discount,discount_type):
    if discount_type=='percentage':
        return subtotal*(1-discount)
    return subtotal-discount


def apply_tax(amount,tax_rate):
    return amount * (1 + tax_rate)


def format_currency(amount):
    return f"PKR{amount:.2f}"


#This Formatting was generated with chatGPT
def format_invoice(invoice):
    subtotal=calculate_subtotal(invoice.items)
    discounted= apply_discount(subtotal,invoice.discount,invoice.discount_type)
    total=apply_tax(discounted,invoice.tax_rate)
    output = [
        f"Invoice Number: {invoice.invoice_number}",
        f"Date: {invoice.date.strftime('%Y-%m-%d %H:%M:%S')}",
        "\nClient Information:",
        f"Name: {invoice.client.name}",
        f"Email: {invoice.client.email}",
        f"Address: {invoice.client.address}",
        f"Phone: {invoice.client.phone or 'N/A'}",
        "\nItems:",
        "----------------------------------------",
        "Item Name          Qty    Price    Total"
        "----------------------------------------"
    ]
    for item in invoice.items:
        output.append(
            f"{item.name:<18} {item.quantity:>3} {format_currency(item.price):>8} "
            f"{format_currency(item.get_total()):>8}"
        )
    output.extend([
        "----------------------------------------",
        f"Subtotal: {format_currency(subtotal):>31}",
        f"Discount: {format_currency(invoice.discount):>31}",
        f"Tax ({invoice.tax_rate*100:.1f}%): {format_currency(subtotal * invoice.tax_rate):>25}",
        "----------------------------------------",
        f"Total: {format_currency(total):>33}"
    ])
    
    return "\n".join(output)


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
