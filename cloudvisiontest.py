import io
import os
from flask import Flask, request, jsonify
import base64
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

app = Flask(__name__)
client = vision.ImageAnnotatorClient()
@app.route('/')
def hello():
    print(request.args['yatit'])
    return 'Helklo woroldsd'

@app.route('/image', methods = ['GET','POST'])
def img_upload():
    imgfile = request.files['sfimage'].read()
    image = types.Image(content=imgfile)
    gcv_response = client.label_detection(image=image)
    labels = gcv_response.label_annotations
    response_dictionary = {}
    for label in labels:
        print label.score
        print label.description
        tag = label.description
        tag2 ='hello'
        response_dictionary[tag] = label.score
        response_dictionary[tag2] = label.description
        return jsonify(response_dictionary)
def convert_img(img_path):
    with open(img_path, "rb") as imageFile:
        str = base64.b64encode(imageFile.read())
    return str
def detect_labels(path):
    """Detects labels in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
   #edit this line for h/w, next 3 lines too

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    return labels
    
    #for label in labels:
    #    print(label.description)
'''
image_labels = detect_labels('./sf.jpg')
print(image_labels)

# loop through image labels
for label in image_labels: 
    last_label = label
    print(label.description)
    print (str(label.score * 100)[:5] + "%")

print(dir(last_label))
'''
# b64img = convert_img('./sf.jpg')

# potential solutions
#if prop in dir(label)
#if prop in label
if __name__ == '__main__':
    app.run()
