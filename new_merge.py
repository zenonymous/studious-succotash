import os
import subprocess
import re

def sort_filenames(filenames):
    """Sort filenames so that those without a number come first."""
    def extract_number(filename):
        """Extract the number from the filename."""
        try:
            return int(''.join(filter(str.isdigit, filename)))
        except ValueError:
            return float('inf')  # Return a very large number for filenames without a number

    return sorted(filenames, key=extract_number)

def construct_pdftk_command(sorted_filenames, output_filename):
    """Construct a pdftk command to merge PDF files."""
    input_files = ' '.join(f'"{filename}"' for filename in sorted_filenames)  # Escape filenames with spaces
    return f"pdftk {input_files} cat output \"{output_filename}\""

def main():
    # List all .pdf files in the current directory
    pdf_files = [file for file in os.listdir('.') if file.endswith('.pdf')]

    # Sort filenames
    sorted_files = sort_filenames(pdf_files)

    # Construct pdftk command
    output_filename = "merged_document.pdf"
    pdftk_command = construct_pdftk_command(sorted_files, output_filename)

    print("pdftk command to merge PDF files:")
    print(pdftk_command)

    # Execute pdftk command
    subprocess.run(pdftk_command, shell=True)

if __name__ == "__main__":
    main()

