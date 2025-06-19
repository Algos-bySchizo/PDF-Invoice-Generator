# Invoice Generator

A simple, modern web application for generating professional invoices as PDF files. Built with Python, Flask, and ReportLab, this project allows users to input client and item details, apply tax and discounts, and download a ready-to-send invoice PDF.

## Features
- User-friendly web interface (responsive, built with Tailwind CSS)
- Add multiple items with quantity and price
- Input client details (name, email, address, phone)
- Apply tax rate and discount (flat or percentage)
- Generate and download PDF invoices instantly
- All invoice data processed locally (no external storage)

## Demo
![Invoice Generator Screenshot](screenshot.png)
*Add a screenshot of your app here for better presentation.*

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Project-Invoice-Generator.git
   cd Project-Invoice-Generator
   ```
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install Flask reportlab
   ```

## Usage
1. **Start the Flask app:**
   ```bash
   python app.py
   ```
2. **Open your browser and go to:**
   [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
3. **Fill in the client and item details, set tax/discount, and click 'Generate Invoice'.**
4. **The PDF invoice will be generated and downloaded automatically.**

## Project Structure
```
Project-Invoice-Generator/
├── app.py               # Flask web server
├── main.py              # Invoice logic and PDF generation
├── templates/
│   └── index.html       # Web UI (Tailwind CSS)
└── README.md            # Project documentation
```

## Dependencies
- [Flask](https://flask.palletsprojects.com/) (web framework)
- [reportlab](https://www.reportlab.com/dev/docs/) (PDF generation)

Install all dependencies with:
```bash
pip install Flask reportlab
```

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENSE) *(add a LICENSE file if you want to specify a license)*

## Contact
For questions or suggestions, open an issue or contact the maintainer.
