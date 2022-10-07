import argparse
parser = argparse.ArgumentParser()
parser.add_argument("img_src",help="Imagen a buscar en la bd de caras")
parser.add_argument("db_path", help="Ruta de la bsase de datoos de caras")
args = parser.parse_args()

ruta = args.img_src + " "+ args.db_path
#print(args.img_src)
#print(args.db_path)
print("Las rutas recibidas son: "+ruta)