import os
import subprocess
import re

def rotate_pdf(file_path, angle):
    """Rotate a PDF file using pdftk."""
    output_path = "rotated-" + os.path.basename(file_path)
    cmd = f"pdftk \"{file_path}\" cat {angle} output \"{output_path}\""
    subprocess.run(cmd, shell=True)

def main():
    # Traverse the current directory
    for file_name in os.listdir('.'):
        if file_name.endswith('.pdf') and file_name.startswith('Scan '):
            # Extract number from filename
            match = re.match(r'Scan (\d+).pdf', file_name)
            if match:
                number = int(match.group(1))
                
                # Decide rotation angle based on number
                if number % 2 == 0:
                    print(f"Rotating {file_name} 270 degrees...")
                    angle = "1-endwest"
                    rotate_pdf(file_name, angle)
                else:
                    print(f"Rotating {file_name} 90 degrees...")
                    angle = "1-endeast"
                    rotate_pdf(file_name, angle)
                    
                # Rename rotated file to original filename
                os.rename("rotated-" + file_name, file_name)
                
    print("Processing completed!")

if __name__ == "__main__":
    main()

