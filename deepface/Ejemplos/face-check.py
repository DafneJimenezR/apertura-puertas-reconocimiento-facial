from deepface import DeepFace

print("Se han comparado dos imagenes. Se verificara que la persona sea la misma")
print("Cargando...")

result = DeepFace.verify(
img1_path = "/home/dafne/Documents/GitHub/apertura-puertas-reconocimiento-facial/deepface/ai-face/harry3.jpg",
img2_path = "/home/dafne/Documents/GitHub/apertura-puertas-reconocimiento-facial/deepface/ai-face/harry4.jpg")

print("RESULTADOS:")
print(result)
