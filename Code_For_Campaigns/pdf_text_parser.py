import pypdf

def extract_text_between_phrases(pdf_path, start_phrase, end_phrase, text_path):
    # Open the PDF file
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = pypdf.PdfFileReader(pdf_file)
    
    # Initialize a flag to indicate if the start phrase is found
    start_found = False
    
    # Initialize a string to store the extracted text
    extracted_text = ''
    
    # Iterate through each page of the PDF
    for page_num in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page_num)
        page_text = page.extractText()
        
        # Check if the start phrase is found in the current page
        if start_phrase in page_text:
            start_found = True
        
        # Extract text only if the start phrase is found
        if start_found:
            extracted_text += page_text
            
            # Check if the end phrase is found in the current page
            if end_phrase in page_text:
                break
    
    # Write the extracted text to a text file
    with open(text_path, 'w', encoding='utf-8') as text_file:
        text_file.write(extracted_text)
    
    # Close the PDF file
    pdf_file.close()

# Specify the paths for the PDF and text files
pdf_path = 'input.pdf'
text_path = 'output.txt'
start_phrase = 'For Council, City of San Antonio, District 9'
end_phrase = 'CITY OF SAN ANTONIO - PROPOSITION A'

# Extract text between specified phrases
# extract_text_between_phrases(pdf_path, start_phrase, end_phrase, text_path)
extract_text_between_phrases(pdf_path, start_phrase, end_phrase, text_path)