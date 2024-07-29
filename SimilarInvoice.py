import os
import PyPDF2
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Step 1: Create Sample PDF Invoices
def create_invoice(filename, invoice_number, date, amount):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.drawString(100, height - 100, f"Invoice Number: {invoice_number}")
    c.drawString(100, height - 120, f"Date: {date}")
    c.drawString(100, height - 140, f"Total Amount: {amount}")

    c.save()

# Create sample invoices in the current directory
create_invoice("invoice1.pdf", "INV001", "2023-07-01", "$500")
create_invoice("invoice2.pdf", "INV002", "2023-07-05", "$300")
create_invoice("input_invoice.pdf", "INV003", "2023-07-10", "$450")

# Verify that files were created
assert os.path.exists("invoice1.pdf"), "invoice1.pdf was not created"
assert os.path.exists("invoice2.pdf"), "invoice2.pdf was not created"
assert os.path.exists("input_invoice.pdf"), "input_invoice.pdf was not created"

# Step 2: Text Extraction from PDFs
def extract_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

# Step 3: Feature Extraction
def extract_features(text):
    invoice_number = re.search(r'Invoice Number:\s*(\S+)', text)
    date = re.search(r'Date:\s*(\S+)', text)
    amount = re.search(r'Total Amount:\s*(\S+)', text)
    
    return {
        'invoice_number': invoice_number.group(1) if invoice_number else None,
        'date': date.group(1) if date else None,
        'amount': amount.group(1) if amount else None
    }

# Step 4: Similarity Calculation
def calculate_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text1, text2])
    return cosine_similarity(vectors[0], vectors[1])[0][0]

# Step 5: Database Integration
database = [
    {'id': 1, 'text': extract_text('invoice1.pdf'), 'features': extract_features(extract_text('invoice1.pdf'))},
    {'id': 2, 'text': extract_text('invoice2.pdf'), 'features': extract_features(extract_text('invoice2.pdf'))},
    # Add more invoices as needed
]

def find_most_similar(input_text):
    similarities = [(doc['id'], calculate_similarity(input_text, doc['text'])) for doc in database]
    most_similar = max(similarities, key=lambda x: x[1])
    return most_similar

# Step 6: Output the Result
def main(input_invoice_path):
    input_invoice_text = extract_text(input_invoice_path)
    most_similar_invoice = find_most_similar(input_invoice_text)
    print(f"Most similar invoice ID: {most_similar_invoice[0]}, Similarity Score: {most_similar_invoice[1]}")

# Run the script
main('input_invoice.pdf')
