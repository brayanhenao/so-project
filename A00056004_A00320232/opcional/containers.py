from pylxd import Client
import time

client = Client()
seleccion = input('Digite 1 para crear un contenedor o 2 para eliminarlo: ')

if seleccion == '1':
    name = input("Nombre para el contenedor: ")
    imagen = input("Imagen del contenedor ( 'xenial/amd64', 'trusty/amd64', 'bionic/amd64', 'artful/amd64') :")
    config = {'name': name,
              'source': {'type': 'image', 'mode': 'pull', 'server': "https://cloud-images.ubuntu.com/daily",
                         "protocol": "simplestreams", 'alias': imagen}, 'profiles': ['default']}
    try:
        container = client.containers.create(config, wait=True)
    except Exception:
        print("Error en la imagen, nombre inválido.")
        exit(1)
    print('Contenedor creado exitosamente')
    iniciar = input("¿Desea iniciarlo? Digite 1 para iniciarlo o 2 para no iniciarlo:")
    if iniciar == '1':
        container.start()

elif seleccion == '2':
    id = input("Nombre del contenedor que desea eliminar: ")
    try:
        container = client.containers.get(id)
    except Exception:
        print("No hay ningún contenedor con ese nombre.")
        exit(1)
    print("Deteniendo contenedor ......")
    container.stop()
    time.sleep(5)
    container.delete()
    print("Contenedor borrado exitosamente")
else:
    print("Entrada invalida")
