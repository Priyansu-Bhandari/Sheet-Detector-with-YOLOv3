import cv2
import numpy as np
from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Load YOLO
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Load COCO names
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    height, width, channels = image.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []

    for out in outs:
        for detection in out:
            if len(detection) < 7:
                continue  
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.3:  
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.7, 0.3)  


    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = confidences[i]
            color = (0, 255, 0)
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
            cv2.putText(image, label + " " + str(round(confidence, 2)), (x, y + 30), cv2.FONT_HERSHEY_PLAIN, 2, color, 2)

    output_image_path = "static/output_" + os.path.basename(image_path)
    cv2.imwrite(output_image_path, image)

    return len(indexes), boxes, output_image_path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        filepath = os.path.join('uploads', file.filename)
        if not os.path.exists('uploads'):
            os.makedirs('uploads')
        file.save(filepath)
        sheet_count, boxes, output_image_path = preprocess_image(filepath)
        return render_template('result.html', sheet_count=sheet_count, output_image_path=output_image_path)

if __name__ == "__main__":
    app.run(debug=True)
