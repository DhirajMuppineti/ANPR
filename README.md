# ANPR Project Using YOLOv8 and Roboflow

## Overview

This Automatic Number Plate Recognition (ANPR) project uses YOLOv8 and Roboflow for detecting and recognizing license plates, specifically trained on an Indian license plate dataset. We have utilized image preprocessing and augmentation techniques to improve the accuracy and robustness of the model. The project involves detecting license plates in images, extracting the license plate area, and recognizing the characters using Tesseract OCR.

## Dataset

The dataset consists of over 300 images of Indian license plates. We applied various data augmentation techniques, including grayscaling, adding noise, and rotating images, to increase the dataset to over 900 images. The augmented dataset was then used to train the YOLOv8 model, achieving an accuracy of over 90%.

## Tools and Libraries

- **YOLOv8**: For object detection.
- **Roboflow**: For data augmentation and preprocessing.
- **OpenCV**: For image processing.
- **Tesseract OCR**: For character recognition.
- **NumPy**: For numerical operations.

## Setup

### Prerequisites

- Python 3.x
- OpenCV
- Tesseract OCR
- Roboflow
- NumPy

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/DhirajMuppineti/ANPR.git
    ```

2. **Install the required Python packages**:

    ```bash
    pip install opencv-python pytesseract numpy roboflow
    ```

3. **Set up Tesseract OCR**:
    - Download and install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).
    - Ensure `tesseract` is added to your system's PATH.

## Usage

1. **Train the YOLOv8 model**:
    - Follow the instructions on the [Roboflow](https://roboflow.com) platform to train the model using the augmented dataset.

2. **Run the ANPR script**:
    - Use the provided script to process images and extract license plate numbers.

## Results

The model achieves an accuracy of over 90% for detecting license plates. The ANPR system demonstrates good performance in recognizing characters from the detected license plates.

## Acknowledgments

- [Roboflow](https://roboflow.com) for providing the platform for data augmentation and model training.
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for the OCR engine.
- [OpenCV](https://opencv.org) for the image processing library.
