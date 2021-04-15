import boto3
import os
import csv
import io

source_path = "/home/balazs/ipc/origin/"
client=boto3.client('rekognition')
for path, subdirs, files in os.walk(source_path):
    for filename in files:
        with io.open(source_path+filename, 'rb') as image_file:
            response = client.detect_labels(Image={'Bytes': image_file.read()})
            try:
                print(filename)
                with open(r'amazon.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([filename,response['Labels'][0]["Name"],response['Labels'][0]["Confidence"]])
            except(e): 
                with open(r'amazon.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([filename,"not found",0])
            
print("finished")