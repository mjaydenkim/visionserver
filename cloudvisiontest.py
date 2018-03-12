import io
import os
from flask import Flask, request, jsonify
import base64
import glob
import random
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
    imgfile = request.files['image'].read()
    image = types.Image(content=imgfile)
    gcv_response = client.label_detection(image=image)
    labels = gcv_response.label_annotations
    response_dictionary = {}
    for label in labels:
        tag = label.description
        response_dictionary[tag] = label.score
    bestfoldermatch = get_match(response_dictionary)
    response = {'message':'Is this '+bestfoldermatch+'?'}
    random_image = get_random_image(bestfoldermatch)
    response['image'] = random_image
    # return jsonify(response_dictionary)
    print response_dictionary
    return jsonify(response)

def get_random_image(foldername):
    images = glob.glob('./pictures/'+foldername+'/*.jpg')
    image_path = random.choice(images)
    image_string = convert_img(image_path)
    return image_string

def get_match(tags_dict):
    folder_names = {'pizza':'pizza',
                    'dog':'dog',
                    'candy':'candy',
                    'hot dog':'hot dog',
                    'cat':'cat',
                    'french fries':'fries',
                    'junk food':'chips'}
    for key in tags_dict:
        percent_accuracy = tags_dict[key]*100
        if percent_accuracy > 80 and key in folder_names:
            return folder_names[key]

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
