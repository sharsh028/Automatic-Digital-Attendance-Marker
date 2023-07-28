import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faceSamples = []
    Ids = []
    
    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage,'uint8')
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        
        faceSamples.append(imageNp)
        Ids.append(Id)
        
    return faceSamples, Ids

faces, Ids = getImagesAndLabels('dataSet/')
recognizer.train(faces, np.array(Ids))
recognizer.write('trainer/trainer.yml')

if os.path.exists(os.getcwd()+'/trainer/trainer.yml'):
    os.system("python message_gui.py")
