import json

#Adicion de una tarea (Create)
def Create(tareas, tareaId, tareaNueva):
    tareas[tareaId] = tareaNueva
    #print("\n** Tarea {} actualizada **\n".format(tareaId))
    return tareas

#Consultar la informacion de todas las tareas (Read)
def Read(rutaArchivo='listadoTareas.json'):
    #Cargar el listado de tareas a un diccionario desde la capa de datos (archivo JSON)
    diccionarioTareas = {} #Contenedor del listado de tareas que gestiona la App
    try:
        with open(rutaArchivo) as archivo:
            diccionarioTareas = json.load(archivo)
    except:
        print("\n** No se pudo cargar la informacion de la capa de datos **\n")
        return False #Reportar fallo en la carga
    return diccionarioTareas
    
#Actualizar una tarea especifica (Update)
def Update(tareas, tareaId, tareaActualizada):
    #Revisar los campos que llegan con informacion para actualizar
    for id_campo, campo in tareaActualizada.items():
        if campo:
            tareas[tareaId][id_campo] = campo #Actualiza el campo del diccionario
    #print("\n** Tarea {} actualizada **\n".format(tareaId))

#Eliminar una tarea especifica (Delete)
def Delete(tareas, tareaId):
    tareas.pop(tareaId)    
    #print("\n** Tarea {} eliminada **\n".format(tareaId))

#Operacion de escritura en la capa de datos al cierre de la aplicacion
def Write(tareas, rutaArchivo='listadoTareas.json'):
    #Descargar contenedor de datos con las modificaciones realizadas por la App
    try:
        with open(rutaArchivo, 'w') as archivo_json:
            json.dump(tareas, archivo_json)
    except:
        print("\n** Error: No se pudo guardar la informacion en la capa de datos **\n")
        return False
    #Si la escritura fue exitosa
    return True