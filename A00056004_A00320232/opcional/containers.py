from pylxd import Client
client = Client()
seleccion = input('Digite 1 para crear un contenedor o 2 para eliminarlo: ')

if seleccion==1:
        name = raw_input("Nombre para el contenedor: ")
        imagen = raw_input("Imagen del contenedor ")
        config = {'name': name, 'source': {'type': 'image', 'mode': 'pull', 'server': "https://cloud-images.ubuntu.com/daily", "protocol": "simplestreams", 'alias': imagen}, 'profiles': ['profilename']}
        container = client.containers.create(config, wait=True)
        print('Contenedor creado exitosamente')
elif seleccion==2:
        id = raw_input("Nombre del contenedor que desea eliminar: ")
        container = client.containers.get('my-container')
        container.delete()
        print("Contenedor borrado exitosamente")
else:
        print("Entrada invalida")
