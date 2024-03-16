from PIL import Image
import os

def convert_to_png(input_file, output_file):
    try:
        # Check if the input file is already in PNG format
        if input_file.lower().endswith('.png'):
            print("Input file is already in PNG format. No conversion needed.")
            return
        
        # Open the input image
        with Image.open(input_file) as image:
            # Convert to RGB if image is not in RGB mode
            if image.mode != 'RGB':
                image = image.convert('RGB')

            # Preserve size and aspect ratio
            size = image.size

            # Create a blank white background image with the same size as the original
            new_image = Image.new("RGB", size, "white")

            # Paste the original image onto the new background
            new_image.paste(image, (0, 0))

            # Save as PNG format with optimization
            new_image.save(output_file, 'PNG', optimize=True)
        
        print(f"Conversion successful: {output_file}")
    except Exception as e:
        print(f"Error converting {input_file} to PNG: {e}")

# Example usage:
input_file = 'C:/Users/Username/Images/example.jpg' # Replace with the path to your input image
output_file = 'C:/Users/Username/Images/example_output.png' # Replace with the desired output PNG file path

convert_to_png(input_file, output_file)
