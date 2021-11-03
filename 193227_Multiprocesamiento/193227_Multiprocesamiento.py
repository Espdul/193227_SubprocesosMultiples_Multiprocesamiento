from imgurpython import ImgurClient
import os
import urllib.request
import timeit
import threading  
from multiprocessing import Pool
import multiprocessing
secreto_cliente = "5f8c3cce299db5e26a2eb96b0b7809a82805c9ad"
id_cliente = "bfa0e227a1c5643"
 
cliente = ImgurClient(id_cliente, secreto_cliente)

# Metodo para la descarga url imagen
# Datos necesarios del metodo
# Nombre de la imagen => yntdWAr
# Formato de la imagen => png
 
def descarga_url_img(link):
   print(link)
   # Con esto ya podemos obtener el corte de la url imagen
   nombre_img = link.split("/")[3]
   formato_img = nombre_img.split(".")[1]
   nombre_img = nombre_img.split(".")[0]
   #print(nombre_img, formato_img)
   url_local = "D:/Miscosas/7cuatrimestre/programacionConcurrente/corte3/act1/193227 FUENTES ESPINOSA/imagenes/{}.{}"
   #Guardar local las imagenes
   urllib.request.urlretrieve(link, url_local.format(nombre_img, formato_img))

def sincrono(imagenes):
    for imagen in imagenes:
       descarga_url_img(imagen.link)

def multiprocesamiento(imagenes):
    with Pool(multiprocessing.cpu_count()) as executor:  # Devuelve el número de CPU (núcleos de computadora) disponibles en su computadora
        executor.map(descarga_url_img,(imagen.link for imagen in imagenes)) # map() corta el iterable en varios trozos que envía al grupo de procesos como tareas separadas

def main():
   id_album = "bUaCfoz"
   imagenes = cliente.get_album_images(id_album)
   return imagenes
  
if __name__ == "__main__":
    imagenes = main()
    print("Tiempo de descarga sincrono {}".format(timeit.Timer(lambda:sincrono(imagenes)).timeit(number=1)))
    print("Tiempo de descarga Multiprocesamiento utilizando Pool {}".format(timeit.Timer(lambda:multiprocesamiento(imagenes)).timeit(number=1))) #Utilice lambda para envolver la funcion
