# Yolo-from-.mp4-file-
The goal of this repo is to use Yolov8 on an imported video.
![cat](https://github.com/user-attachments/assets/7a0bc4d8-738b-4ddf-89c8-58d248a19fc7)


## Files of this repo 
requirements.txt : importe all the library needed 
.py : Main core of the program
.bat : creat a virtual environement, importe all the libraries from requirements.txt and run the .py

## Model : YoloV8n
YoloV8n is a model trained by ultralytics, not by myself. The main goal of this model is to analyse the frame with a minimal latency. It is suitable for real time detection. 
Please note that if your goal is to detect in an imported video and your goal is not to use it in realtime operation you might want to change the model.

## How to run this repo 
Put the .mp4 file that you want to use in the folder of the repo 
Change the name of the file at line 6 : file = "C:/Users/TheoN/Desktop/Video_ouverture/video.mp4"
Launch the .bat and you are good to go !
