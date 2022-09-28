# Importar bibilioteca
from deepface import DeepFace

# Busqueda
print("Buscando rostro...")

df = DeepFace.find(img_path="/home/dafne/Documents/GitHub/apertura-puertas-reconocimiento-facial/deepface/faces/personax.png", db_path="/home/dafne/Documents/GitHub/apertura-puertas-reconocimiento-facial/deepface/mydb", enforce_detection="false")

print("Resultados")
print(df)

print("Seleccion")
# print(df[0])