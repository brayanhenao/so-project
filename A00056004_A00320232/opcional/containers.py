from pylxd import Client
client = Client()
seleccion = input('Digite 1 para crear un contenedor o 2 para eliminarlo: ')

if seleccion=='1':
        name = input("Nombre para el contenedor: ")
        imagen = input("Imagen del contenedor ")
        config = {'name': name, 'source': {'type': 'image', 'mode': 'pull', 'server': "https://cloud-images.ubuntu.com/daily", "protocol": "simplestreams", 'alias': imagen}, 'profiles': ['default']}
        container = client.containers.create(config, wait=True)
        print('Contenedor creado exitosamente')
	iniciar = input("¿Desea iniciarlo?" 1-Si 2-No: )
	if iniciar == '1':
		container.start()
elif seleccion=='2':
        id = input("Nombre del contenedor que desea eliminar: ")
        container = client.containers.get(id)
        container.delete()
        print("Contenedor borrado exitosamente")
else:
        print("Entrada invalida")
