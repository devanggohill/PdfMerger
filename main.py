from PyPDF2 import PdfMerger

# Paths to the input PDF files
pdf1_path = 'sample.pdf'
pdf2_path = 'sample2.pdf'

# Path to save the merged PDF file
output_pdf_path = 'output.pdf'

# Create a PdfMerger object
merger = PdfMerger()

# Append the PDF files
merger.append(pdf1_path)
merger.append(pdf2_path)

# Write the merged PDF to a file
merger.write(output_pdf_path)

# Close the PdfMerger object
merger.close()

print(f"Successfully merged {pdf1_path} and {pdf2_path} into {output_pdf_path}")
