from deepface import DeepFace

# df = DeepFace.find(img_path = "~/Documents/GitHub/apertura-puertas-reconocimiento-facial/deepface/ai-face/img.jpg", db_path = "C:/workspace/my_db")

obj = DeepFace.analyze(img_path = "~/Documents/GitHub/apertura-puertas-reconocimiento-facial/deepface/ai-face/img.jpg", 
        actions = ['age', 'gender', 'race', 'emotion']
)

print("El resultado de la imagen es: ")

print(obj)

