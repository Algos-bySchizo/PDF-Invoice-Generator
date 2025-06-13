from dataclasses import dataclass
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import json
import os
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
    contact:None 
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
        self.items= []
        self.invoice_date=datetime.now()
        self.invoice_number=f"INV-{id(self)}"
        self.tax_rate: float=0.0
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

def calculate_subtotal(items):
    # subtotal=0
    # for item in self.items:
    #     subtotal+=item.price_cal()
    # return subtotal
    return sum(item.price_cal() for item in items)


def apply_discount(subtotal,discount,discount_type):
    if discount_type=='percentage':
        return subtotal*(1-discount)
    return subtotal-discount


def apply_tax(amount,tax_rate):
    return amount * (1 + tax_rate)


def format_currency(amount):
    return f"PKR{amount:.2f}"


#This Formatting was generated using AI-chatGPT
def format_invoice(invoice):
    subtotal=calculate_subtotal(invoice.items)
    discounted= apply_discount(subtotal,invoice.discount,invoice.discount_type)
    total=apply_tax(discounted,invoice.tax_rate)
    output = [
        f"Invoice Number: {invoice.invoice_number}",
        f"Date: {invoice.invoice_date.strftime('%Y-%m-%d %H:%M:%S')}",
        "\nClient Information:",
        f"Name: {invoice.client.name}",
        f"Email: {invoice.client.email}",
        f"Address: {invoice.client.address}",
        f"Phone: {invoice.client.contact or 'N/A'}",
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

#Generating JSON file was done using AI-ChatGPT

def export_to_json(invoice):
    data = {
        "invoice_number": invoice.invoice_number,
        "date": invoice.inovice_date.isoformat(),
        "client": {
            "name": invoice.client.name,
            "email": invoice.client.email,
            "address": invoice.client.address,
            "phone": invoice.client.contact
        },
        "items": [
            {
                "name": item.name,
                "quantity": item.quantity,
                "price": item.price,
                "total": item.get_total()
            }
            for item in invoice.items
        ],
        "subtotal": calculate_subtotal(invoice.items),
        "discount": invoice.discount,
        "discount_type": invoice.discount_type,
        "tax_rate": invoice.tax_rate,
        "total": apply_tax(
            apply_discount(
                calculate_subtotal(invoice.items),
                invoice.discount,
                invoice.discount_type
            ),
            invoice.tax_rate
        )
    }
    return json.dumps(data, indent=2)


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")
#This was generated using ChatGPT PD 
def generate_pdf(invoice, filename= None):
    if filename is None:
        filename = f"invoice_{invoice.invoice_number}.pdf"
    
    # Create the PDF document
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []
    
    # Add title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30
    )
    elements.append(Paragraph("INVOICE", title_style))
    
    # Add invoice details
    elements.append(Paragraph(f"Invoice Number: {invoice.invoice_number}", styles["Normal"]))
    elements.append(Paragraph(f"Date: {invoice.date.strftime('%Y-%m-%d %H:%M:%S')}", styles["Normal"]))
    elements.append(Spacer(1, 20))
    
    # Add client information
    elements.append(Paragraph("Client Information:", styles["Heading2"]))
    elements.append(Paragraph(f"Name: {invoice.client.name}", styles["Normal"]))
    elements.append(Paragraph(f"Email: {invoice.client.email}", styles["Normal"]))
    elements.append(Paragraph(f"Address: {invoice.client.address}", styles["Normal"]))
    if invoice.client.phone:
        elements.append(Paragraph(f"Phone: {invoice.client.phone}", styles["Normal"]))
    elements.append(Spacer(1, 20))
    
    # Add items table
    elements.append(Paragraph("Items:", styles["Heading2"]))
    
    # Table data
    data = [["Item Name", "Quantity", "Price", "Total"]]
    for item in invoice.items:
        data.append([
            item.name,
            str(item.quantity),
            format_currency(item.price),
            format_currency(item.get_total())
        ])
    
    # Create table
    table = Table(data, colWidths=[3*inch, 1*inch, 1.5*inch, 1.5*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(table)
    elements.append(Spacer(1, 20))
    
    # Add totals
    subtotal = calculate_subtotal(invoice.items)
    discounted = apply_discount(subtotal, invoice.discount, invoice.discount_type)
    total = apply_tax(discounted, invoice.tax_rate)
    
    elements.append(Paragraph(f"Subtotal: {format_currency(subtotal)}", styles["Normal"]))
    elements.append(Paragraph(f"Discount: {format_currency(invoice.discount)}", styles["Normal"]))
    elements.append(Paragraph(f"Tax ({invoice.tax_rate*100:.1f}%): {format_currency(subtotal * invoice.tax_rate)}", styles["Normal"]))
    elements.append(Paragraph(f"Total: {format_currency(total)}", styles["Heading2"]))
    
    # Build PDF
    doc.build(elements)
    return filename

def main():
    print("=== Invoice Generator ===")
    print("\nEnter Client Information:")
    client=Client(
        name=input('Client\'s Name: '),
        email=input('Client\'s email: '),
        contact=input('Client\'s contact no. (optional, press Enter to skip): ') or None,
        address=input('Client\'s address: ')
        )
    invoice=Invoice(client)
    print('Enter bought Items: (enter "done" to stop adding items) :')
    while True:
        item_name=input('Enter Item (enter "done" to stop adding items) :').strip()
        if item_name.lower()=='done':
            break
        if not item_name:
            print('Item name field cannot be left empty!')
            continue
        quantity=get_int_input("Quantity: ")
        if quantity<=0:
            print('Quantity must be greater than 0. Please try again!')
            continue
        price=get_float_input('Price Per Unit: ')
        if price<0:
            print("Price can not be negative. Please try again!")
        invoice.add_item(Item(item_name,quantity,price))
        print(f"added {quantity}x{item_name} at PKR{price:.2f} each")
        if not invoice.items:
            print('\n no items added. Exiting...')
            return
    tax_rate=get_float_input("\nEnter tax rate (e.g., 0.1 for 10%): ")
    while tax_rate<0:
        print("Tax rate cannot be negative. Please try again.")
        tax_rate = get_float_input("Enter tax rate (e.g., 0.1 for 10%): ")
    invoice.set_tax_rate(tax_rate)

    discount_type = input("\nDiscount type (flat/percentage): ").lower()
    while discount_type not in ['flat', 'percentage']:
        print("Invalid discount type. Please enter 'flat' or 'percenta  ge'.")
        discount_type = input("Discount type (flat/percentage): ").lower()
    discount = get_float_input("Enter discount amount: ")
    while discount < 0:
        print("Discount cannot be negative. Please try again.")
        discount = get_float_input("Enter discount amount: ")
    invoice.set_discount(discount, discount_type)
    print(format_invoice(invoice))
    print("\n" + "="*50)
    print(format_invoice(invoice))
    pdf_filename = generate_pdf(invoice)
    print(f"\nPDF invoice has been generated: {pdf_filename}")
    print(f"Full path: {os.path.abspath(pdf_filename)}")

if __name__ == "__main__":
    main() 