# Invoice file identifier System

## Description
The Document Similarity Matching System is 
designed to automatically categorize incoming invoices by matching them to existing templates or previously processed invoices. This prototype system demonstrates the capability to identify and match similar documents based on their content and structure.

## Features
- **Text Extraction**: Extract text content from PDF invoices.
- **Feature Extraction**: Extract relevant features such as invoice number, date, and amount.
- **Similarity Calculation**: Calculate the similarity between invoices using cosine similarity with TF-IDF vectors.
- **Database Integration**: Simple in-memory database for storing and comparing invoices.
- **Output**: Provides the most similar invoice from the database along with a similarity score.

## Approach
**Document Representation**
- **Text Extraction**: Using the PyPDF2 library to extract text content from PDF invoices.
- **Feature Extraction**: Using regular expressions to extract key features like invoice number, date, and amount from the text.

**Similarity Metric**
- **Cosine Similarity**: Calculated using TF-IDF vectors to measure the similarity between two invoices.

## Output
This shows the Similarity Score of the Input Invoice file from the already available file in the database.

<img width="957" alt="result" src="https://github.com/user-attachments/assets/32c81d4a-51f6-4845-828a-c01b431acfdd">

## Setup
**Prerequisites**
- Python 3.x
- Required Python libraries: PyPDF2, scikit-learn, reportlab

**Installation**

1. Clone the Repository:
   ```bash
   git clone https://github.com/Garvit-Sharma-git/Invoice_Identefier.git
   cd SimilarInvoice.py

2. Install the required libraries:
   ```bash
   pip install PyPDF2 scikit-learn reportlab

## Results
The system outputs the ID and similarity score of the most similar invoice from the database. The similarity score indicates how closely the input invoice matches the existing ones.



## Contact
Garvit Sharma
- Email: garvitsharma1994@gmail.com
- LinkedIn: https://www.linkedin.com/in/garvit-sharma-99319a1b4/
- Github: https://github.com/Garvit-Sharma-git
   
