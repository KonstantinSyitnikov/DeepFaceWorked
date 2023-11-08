#python deepface facial recognition

import cv2
from deepface import DeepFace
import sys
import face_recognition

def take_picture():
    print("Scaning Face...")
    cap =cv2.VideoCapture(0)
    ret,frame =cap.read()
    cv2.imwrite('Its me/MeAle.jpeg',frame) #делает фото
    cv2.destroyAllWindows()
    cap.release()
    print("Face scan Complete")

def analize_user():
    print('Analize user...')
    baseimg=face_recognition.load_image_file('Its me/Anna1.jpg')# загружает фото исходника с которым нужно сравнить
    baseimg=cv2.cvtColor(baseimg,cv2.COLOR_BGR2RGB)
    myFace=face_recognition.face_locations(baseimg)[0]
    encodemyfase=face_recognition.face_encodings(baseimg)[0]
    cv2.rectangle(baseimg,(myFace[3],myFace[0],),(myFace[1],myFace[2]),(255,0,255),2)
    
    sampleimg=face_recognition.load_image_file('Its me/MeAle.jpeg')
    sampleimg=cv2.cvtColor( sampleimg,cv2.COLOR_BGR2RGB)

    try:
        samplefacetest=face_recognition.face_locations(sampleimg)[0]
        encodesamplefacetest=face_recognition.face_encodings(sampleimg)[0]
    except ImportError as e:
        print('Index Error. Autentification Failed')
        sys.exit()


    result= face_recognition.compare_faces([encodemyfase],encodesamplefacetest) #сравнивет encodemyfase и encodesamplefacetest
    resultstring=str(result)

    if resultstring == "[True]":
        print("User Authenticated.Welcome back sir !")
    else:
        print("Authentification failed.Go away!")    


take_picture()
analize_user()

#take_picture()
#img1='Its me/MeAndSmile.jpeg' 
#img2='Its me/MeAndStrict.jpeg'
#model_name1='Facenet'


#autentification = DeepFace.verify(img1_path=img1,img2_path=img2,model_name='Facenet')
#print(autentification)
#if(autentification['verified']):
 #   print('Access granted.')
#else:
 #   print('Acess denied.Shutting down sytstem.')    