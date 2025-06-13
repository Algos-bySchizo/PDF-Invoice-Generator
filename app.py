from flask import Flask, render_template, request, jsonify, send_file
from main import Client, Item, Invoice, generate_pdf
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_invoice', methods=['POST'])
def create_invoice():
    data = request.json
    
    # Create client
    client = Client(
        name=data['client']['name'],
        email=data['client']['email'],
        address=data['client']['address'],
        phone=data['client'].get('phone')
    )
    
    # Create invoice
    invoice = Invoice(client)
    
    # Add items
    for item_data in data['items']:
        item = Item(
            name=item_data['name'],
            quantity=int(item_data['quantity']),
            price=float(item_data['price'])
        )
        invoice.add_item(item)
    
    # Set tax and discount if provided
    if 'tax_rate' in data:
        invoice.set_tax_rate(float(data['tax_rate']))
    if 'discount' in data:
        invoice.set_discount(
            float(data['discount']),
            data.get('discount_type', 'flat')
        )
    
    # Generate PDF
    pdf_filename = generate_pdf(invoice)
    
    return jsonify({
        'success': True,
        'invoice_number': invoice.invoice_number,
        'pdf_url': f'/download/{pdf_filename}'
    })

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True) 