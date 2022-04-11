#Libreria para interaccion por consola (interfaz)

#Presentar mensaje generico en pantall
def mensaje(info=''):
    print()
    print(info)
    print()
    
#Formulario menu aplicacion CRUD
def formularioMenuAppCRUD():
    print(' 1. Agregar Tarea')
    print(' 2. Consultar Tareas')
    print(' 3. Actualizar Tarea')
    print(' 4. Eliminar Tarea')
    print(' 5. Salir')
    print('')
    #Capturar la opcion del usuario, validando el tipo de dato para retornarlo al controlador
    opcion = None
    while opcion == None:
        try:
            print(' Ingrese una opcion:')
            opcion = int(input('--> '))
        except:
            print()
            print("** Entrada invalida: Se debe ingresar una opcion numerica. **")
            print()
    #retornar opcion al controlador
    return opcion

#Formulario para adicionar tareas (Create)
def formularioAdicionarTarea():
    #Recoger los campos de la tarea
    print('Ingrese un ID para la tarea: ')
    tareaId = input('--> ')
    print('Ingrese descripcion de la tarea: ')
    descripcion = input('--> ')
    print('Ingrese el estado de la tarea: ')
    estado = input('--> ')
    #Capturar el tiempo validando el tipo de dato ingresado
    tiempo = None
    while tiempo == None:
        try:
            print('Ingrese el tiempo en el que debe completar la tarea: ')
            tiempo = int(input('--> '))
        except:
            print()
            print("** Entrada invalida: Se debe ingresar una opcion numerica. **")
            print()
    #Encapsular tareaNueva
    tareaNueva = {
        'descripcion': descripcion,
        'estado': estado,
        'tiempo': tiempo
    }
    #Retornar al controlador el identificador y la tareaNueva
    return tareaId, tareaNueva

#Presentacion de las tareas que llegan del controlador (Read)
def mostrarTareas(tareas):
    for tareaId, tarea in tareas.items():
        print(tareaId, '-', end=' ')
        for nombre_atributo, atributo in tarea.items():
            print(atributo, end=', ')
        print()

#Funcion de validacion en la coleccion recibida del controlador
def estaElemento(tareaId, tareas):
    #Extraer de la base de datos los ID's
    conjuntoIdentificadores = set(tareas.keys())
    #Revisar si se encuentra el elemento/ID solicitado
    if tareaId in conjuntoIdentificadores:
        return True
    else:
        return False

#Formulario para actualizacion de tareas (Update)
def formularioActualizarTarea(tareas):
    #Solicitar a usuario la tareaId
    print('Ingrese ID de la tarea a modificar:')
    tareaId = input('--> ')
    #Revisar si se encuentra ID solicitado
    if estaElemento(tareaId, tareas):
        #Recoger los nuevos datos de tarea
        print('Ingrese nueva descripcion:')
        nuevaDescripcion = str(input('--> '))
        print('Ingrese nuevo estado:')
        nuevoEstado = str(input('--> '))
        #Capturar el tiempo validando el tipo de dato ingresado
        nuevoTiempo = None
        while nuevoTiempo == None:
            try:
                print('Enter a task due time: ')
                nuevoTiempo = int(input('--> '))
            except:
                print()
                print("** Entrada invalida: Se debe ingresar una opcion numerica. **")
                print()
        #Encapsular tareaNueva
        tareaActualizada = {
            'descripcion': nuevaDescripcion,
            'estado': nuevoEstado,
            'tiempo': nuevoTiempo
        }
        #Retornar al controlador el identificador y la tareaNueva
        return tareaId, tareaActualizada
    else:
        print()
        print("** No se ha encontrado la tarea {} para actualizacion! **".format(tareaId))
        print()
        return False
    
def formularioEliminarTarea(tareas):
    #Solicitar a usuario la tareaId
    print('Ingrese ID de la tarea para eliminar:')
    tareaId = input('--> ')
    #Revisar si se encuentra ID solicitado
    if estaElemento(tareaId, tareas):
        return tareaId
    else:
        print()
        print("** No se ha encontrado la tarea {} para eliminacion! **".format(tareaId))
        print()
        return False    