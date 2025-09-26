import json
from pdfminer.high_level import extract_text

def extract_json_from_pdf(pdf_path):
    """
    Extracts text from a PDF file and converts it into JSON format.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        dict: JSON representation of the extracted text.
    """
    try:
        # Extract text from the PDF
        extracted_text = extract_text(pdf_path)

        # Convert text into JSON format
        json_content = {"content": extracted_text}

        return json_content
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    pdf_path = "sample.pdf"  # Replace with your PDF file path
    json_output = extract_json_from_pdf(pdf_path)
    print(json.dumps(json_output, indent=4))