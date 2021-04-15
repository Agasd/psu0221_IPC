
import io
import os
import csv

# Imports the Google Cloud client library
from google.cloud import vision

# Instantiates a client
client = vision.ImageAnnotatorClient()

source_path = "/home/balazs/ipc/origin/"
for path, subdirs, files in os.walk(source_path):
    for filename in files:
        with io.open(source_path+filename, 'rb') as image_file:
            content = image_file.read()
            image = vision.Image(content=content)
            # Performs label detection on the image file
            response = client.label_detection(image=image)
            labels = response.label_annotations
            try:
                print(filename)
                with open(r'google.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([filename,labels[0].description,labels[0].score])
            except(e): 
                with open(r'google.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([filename,"not found",0])
            
print("finished")