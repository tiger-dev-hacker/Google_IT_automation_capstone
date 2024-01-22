from PIL import Image
import os

input_folder = "/home/student-01-8f48ea40cfff/images"
output_folder = "/opt/icons/"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".jpeg"):
        with Image.open(os.path.join(input_folder, filename)) as img:
            img = img.rotate(-90)
            img = img.resize((128, 128))

            output_path = os.path.join(output_folder, filename)
            img.save(output_path, "JPEG")

print("Task completed successfully.")
