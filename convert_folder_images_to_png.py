from PIL import Image
import os

def convert_to_png(input_folder, output_folder):
    # Check if input folder is empty
    if not os.listdir(input_folder):
        print("No files found in the input folder.")
        return

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.png')

        try:
            # Open the input image
            with Image.open(input_file_path) as image:
                # Convert to RGB if image is not in RGB mode
                if image.mode != 'RGB':
                    image = image.convert('RGB')
                
                # Save as PNG format with optimization
                image.save(output_file_path, 'PNG', optimize=True)
            
            print(f"Conversion successful: {input_file_path} -> {output_file_path}")
        except Exception as e:
            print(f"Error converting {input_file_path} to PNG: {e}")

# Example usage:
input_folder = 'C:/Users/Username/Images/input_folder'  #Replace path to the folder containing the input images
output_folder = 'C:/Users/Username/Images/output_folder' #Replace path to the folder where you want to save the converted PNG images.

convert_to_png(input_folder, output_folder)
