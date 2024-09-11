from flask import Flask, request, jsonify
# from .decorators import with_model
from flask_cors import CORS, cross_origin
from model.yolo import Yolo
from model.LLM import LLM
import cv2
from collections import Counter

llm = LLM()
yolo = Yolo()

flaskapp = Flask(__name__)
cors = CORS(flaskapp)
flaskapp.config['CORS_HEADERS'] = 'Content-Type'


@flaskapp.route('/getchat', methods=['POST'])
@cross_origin()
def getChat():
    data = dict(request.form)
    
    print(data, request.files)
    
    if 'attachment' in request.files:
        img = cv2.imread(request.files['attachment'])
        pred = yolo.predict(img)
        labels = [item['label'] for item in pred]
        label_counts = Counter(labels)

        # Format the result as "count label"
        result = [f"{count} {label}" for label, count in label_counts.items()]
        joinedstr = ", ".join(result)
        
        llm.addAssistantMessage(data['userId'], f"i have processed and identified the objects in the images using an external learning model, the image consists of the objects: {joinedstr}")
        op = llm.generate(data['userId'], "can you explain what objects were in the image processed earlier")

    else:
        op = llm.generate(data['userId'], data['content'])
        
    # print(llm.contexts)
    
    
    returnData = {
        "role": "assistant",
        "content": str(op)
    }
    
    return jsonify(returnData), 200

@flaskapp.route('/')
def home():
    return "welcome to reflex api"

if (__name__ == '__main__'):
    print('debug active')
    flaskapp.run(debug=True)

