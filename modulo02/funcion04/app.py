def saludo():
    global nombre
    global nombre = "John Doe"
    print(f'hola {nombre}')

    def despedida():
        global nombre
        nombre = "Sara Swan"
        print(f'Adios {nombre}')

saludo()
despedida()
print(nombre)