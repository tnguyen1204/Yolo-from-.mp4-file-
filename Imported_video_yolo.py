import cv2
from ultralytics import YOLO
import time 

#VIDEO SOUHAITEE 
file = "C:/Users/TheoN/Desktop/Video_ouverture/video.mp4"

cap = cv2.VideoCapture(file)
print(f"Chemin vers la vidéo : {file}")
print(f"Statut d'ouverture : {cap.isOpened()}")

#VERIFICATION VIDEO EXPLOITABLE
if not cap.isOpened(): 
    print('Erreur lors de l\'ouverture du fichier.')
    exit()

#IMPORTATION DU MODELE YOLO
model = YOLO('yolov8n.pt') #Modele pre-entrainé comprenant le moins de latence avec Yolo V8, faudra faire des essais avec V9
     
#LECTURE DE LA VIDEO AVEC YOLO
start_time_yolo = time.time()
while True:
    ret, frame = cap.read() 
    results = model(frame)
    annotated_frame = results[0].plot()
    if not ret: 
        print("Aucune frame lue. Fin de la vidéo ou problème de lecture.")
        break

    cv2.imshow('Video', annotated_frame)  

    if cv2.waitKey(25) & 0xFF == ord('q'):
        print("Lecture interrompue par l'utilisateur.")
        break
time_yolo = time.time() - start_time_yolo
print(time_yolo)

cap.release()
cv2.destroyAllWindows()
