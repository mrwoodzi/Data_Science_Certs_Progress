import pypdf

# Function to extract text from a PDF and save it to a text file
def extract_text_to_txt(pdf_path, txt_path):
    pdf_reader = pypdf.PdfReader(pdf_path)
    
    extracted_text = ''
    for page in pdf_reader.pages:
        extracted_text += page.extract_text()
    
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(extracted_text)

# Specify the paths for the PDF and text files
pdf_path = 'May_6_2023_PrecinctResults.pdf'
txt_path = 'full_pdf_text.txt'

# Extract text from the PDF and write to a text file
extract_text_to_txt(pdf_path, txt_path)

# Specify start and end phrases for extraction
start_phrase = 'For Council, City of San Antonio, District 9'
end_phrase = 'CITY OF SAN ANTONIO - PROPOSITION A'

# Paths for input and output text files
input_txt_path = 'full_pdf_text.txt'
output_txt_path = 'extracted_text.txt'

# Read the full text from the input file
with open(input_txt_path, 'r', encoding='utf-8') as input_file:
    full_text = input_file.read()

# Initialize start index for searching
start_index = 0

# Loop to extract text between start and end phrases
while start_index != -1:
    # Find the start phrase from the current start index
    start_index = full_text.find(start_phrase, start_index)
    
    if start_index == -1:
        break
    
    # Find the end phrase from the current start index
    end_index = full_text.find(end_phrase, start_index)
    
    if end_index == -1:
        break
    
    # Extract the text between the phrases
    extracted_text = full_text[start_index:end_index + len(end_phrase)]
    
    # Write the extracted text to the output file
    with open(output_txt_path, 'a', encoding='utf-8') as output_file:
        output_file.write(extracted_text + '\n')  # Adding a newline between extracted texts
    
    # Update the start index for the next iteration
    start_index = end_index + len(end_phrase)

# Print a message after extraction is complete
print("Text extracted and saved to", output_txt_path)