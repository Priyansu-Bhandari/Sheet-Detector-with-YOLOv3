# Sheet Detector with YOLOv3

## Overview

This project provides a web application to detect and count sheets in an image using the YOLOv3 object detection model. The application features a user-friendly interface for uploading images and viewing detection results.

## Project Status

- **Integration Completed:** The web application is fully integrated and functional. Users can upload images, and the system will process and display results.

- **Detection Status:** While the integration is complete, the detection functionality is not fully optimized. The current model may not accurately detect all sheets as expected. Efforts have been made to refine the detection, but further improvements are needed to achieve optimal performance. 

We are actively working on enhancing the detection accuracy, and contributions or suggestions are welcome to help resolve these issues.


## Prerequisites

Before running the application, ensure you have the following:

- Python 3.6 or higher
- A virtual environment (recommended)

## Setup Instructions

Follow these steps to set up and run the project:

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/sheet-detector-yolov3.git
cd sheet-detector-yolov3
```

## 2. Set Up Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

## 3.Download YOLOv3 Weights and Configuration

Download the YOLOv3 weights and configuration files from the official YOLO website:

- YOLOv3 Weights: Download yolov3.weights
- YOLOv3 Configuration: Download yolov3.cfg

Place these files in the project directory.

## 4. Download COCO Names File
The coco.names file contains the list of object classes used by YOLOv3. Download it from the following link:

- COCO Names: Download coco.names
- Place this file in the project directory.

## 5. Run the Flask Application
Start the Flask web application:

```bash
python app.py
```
The application will start and should be accessible at http://127.0.0.1:5000/ in your web browser.

## How to Use
- Upload Image: Navigate to the home page (http://127.0.0.1:5000/), and use the provided form to upload an image file.
- View Results: After uploading, the application will process the image and display the number of detected sheets along with the annotated image on the results page.

## Notes
- The user interface is designed to be user-friendly, but the sheet detection is currently not fully optimized. Future improvements include training a custom YOLOv3 model specific to sheet detection for better accuracy.

## Troubleshooting
- Model Files Not Found: Ensure that yolov3.weights, yolov3.cfg, and coco.names are in the project directory.
- Dependencies Issues: Verify that all dependencies are installed by running pip install -r requirements.txt.

## Contributing

Feel free to contribute to the project by submitting issues or pull requests. Your feedback and improvements are welcome!











