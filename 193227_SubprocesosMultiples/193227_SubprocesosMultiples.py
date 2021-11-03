from imgurpython import ImgurClient
import os
import urllib.request
import timeit
import threading  
from concurrent.futures import ThreadPoolExecutor
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

def subprocesomultiple(imagenes):
    with ThreadPoolExecutor(max_workers=10) as executor: #La ejecución asincrónica se puede realizar mediante hilos, usando ThreadPoolExecutor, se estan utilizando 10 hilos
        executor.map(descarga_url_img,(imagen.link for imagen in imagenes)) #los iterables son recolectados inmediatamente, en lugar de perezosamente, la funcion se ejecuta de forma asincrónica y se pueden realizar varias llamadas a funcion simultáneamente
        
def main():
   id_album = "bUaCfoz"
   imagenes = cliente.get_album_images(id_album)
   return imagenes
  
if __name__ == "__main__":
    imagenes = main()
    print("Tiempo de descarga sincrono {}".format(timeit.Timer(lambda:sincrono(imagenes)).timeit(number=1)))
    print("Tiempo de descarga subproceso multiple utilizando ThreadPoolExecutor {}".format(timeit.Timer(lambda:subprocesomultiple(imagenes)).timeit(number=1))) #Utilice lambda para envolver la funcion
