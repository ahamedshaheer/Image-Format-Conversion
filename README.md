<!DOCTYPE html>
<html lang="en">
<body>
    <h1>Image Format Conversion</h1>
    <p>This script allows you to convert images from various formats to PNG format using Python and Pillow library.</p>
    <h2>Single Image Conversion</h2>
    <p>To convert a single image, follow these steps:</p>
    <ol>
        <li>Install Pillow library if not already installed:
            <pre><code>pip install Pillow</code></pre>
        </li>
        <li>Run the provided Python script <code>convert_single_image_to_png.py</code>.</li>
        <li>Specify the input file path (<code>input_file</code>) and the output file path (<code>output_file</code>) within the script.</li>
        <li>Execute the script. It will convert the specified input image to PNG format and save it at the specified output location.</li>
    </ol>
    <h2>Multiple Image Conversion</h2>
    <p>To convert multiple images from a folder, follow these steps:</p>
    <ol>
        <li>Install Pillow library if not already installed:
            <pre><code>pip install Pillow</code></pre>
        </li>
        <li>Run the provided Python script <code>convert_folder_images_to_png.py</code>.</li>
        <li>Specify the input folder path (<code>input_folder</code>) containing the images to be converted and the output folder path (<code>output_folder</code>) where the converted PNG images will be saved within the script.</li>
        <li>Execute the script. It will convert all images within the specified input folder to PNG format and save them in the output folder with the same filenames and <code>.png</code> extension.</li>
    </ol>
    <h2>Notes</h2>
    <ul>
        <li>The script uses Pillow library for image processing and conversion.</li>
        <li>For multiple image conversion, ensure that the input folder contains only image files. Other file types will be ignored.</li>
        <li>If there are no files in the input folder for multiple image conversion, the script will print a message indicating that there are no files to convert.</li>
    </ul>
</body>
</html>
