import CRUD
import InterfazConsola as ic
import InterfazGUI as iGUI
import tkinter as tk
import sys

#Carga de la base de datos de la aplicacion (archivo JSON)
tareas = CRUD.Read()
if not(tareas): #Si no se obtine el listado de tareas archivo JSON (Base de datos)
    sys.exit(1) #Terminacion de la App reportando error

###################################################################################
#->Observar que:
# Al terner las dos alternativas de vistas, basta con activar cualquier de los dos
# mainloops para tener modo consola o modo GUI.
###################################################################################

#Iniciar Mainloop de la App por GUI
#----------------------------------
#Carga de la interfaz
m = iGUI.ventanaMenuPrincipal(tareas)

#La ventana va a estar escuchando todos los eventos
m.mainloop()

"""
#Iniciar Mainloop de la App por consola
#--------------------------------------
mainloop = True
while mainloop:
    #Solicitar a la interfaz la seleccion de una opcion
    ic.mensaje('====== CRUD App - Tareas pendintes ======')
    opcion = ic.formularioMenuAppCRUD()
    
    #Si Create fue seleccionado por el usuario en el menu
    if opcion == 1:
        #Solicitar a la interfaz mostar el mensaje
        ic.mensaje('============ Agregar Tarea ==============')
        #Presentar formulario para encapsular ingreso de datos en diccionario tareaNueva
        tareaId, tareaNueva = ic.formularioAdicionarTarea()
        #Adicionar tareaNueva al contenedor
        CRUD.Create(tareas, tareaId, tareaNueva)
    
    #Si Read fue seleccionado por el usuario en el menus
    elif opcion == 2:
        #Solicitar a la interfaz mostar el mensaje
        ic.mensaje('============ Lista de Tareas ============')
        #Solicitar a la interfaz que muestre la base de datos de tareas cargada
        ic.mostrarTareas(tareas)
    
    #Si Update fue seleccionado por el usuario en el menu
    elif opcion == 3:
        #Solicitar a la interfaz mostar el mensaje
        ic.mensaje('=========== Actualizar Tarea ============')
        #Presentar formulario de actualizacion de tareas
        respuestaInterfaz = ic.formularioActualizarTarea(tareas)
        # Si la Interfaz preparo la actualizacion
        if respuestaInterfaz != False:
            #Desempacar informacion de la respuesta
            tareaId, tareaActualizada = respuestaInterfaz
            #Realizar la actualizacion
            CRUD.Update(tareas, tareaId, tareaActualizada)
    
    #Si Delete fue seleccionado por el usuario en el menu
    elif opcion == 4:
        #Solicitar a la interfaz mostar el mensaje
        ic.mensaje('============ Eliminar Tarea =============')
        #Presentar formulario deeliminar tarea
        tareaId = ic.formularioEliminarTarea(tareas)
        # Si la Interfaz preparo la actualizacion
        if tareaId != False:
            #Realizar la eliminacion si llega autorizacion desde la interfaz
            CRUD.Delete(tareas, tareaId)
    
    #Si Salir fue seleccionado por el usuario en el menu
    elif opcion == 5:
        #Guardar el listado de tareas en la base de datos (archivo JSON)
        if CRUD.Write(tareas):
            #Solicitar a la interfaz reporte de salida exitosa
            ic.mensaje('** Datos guardados: Cierre Exitoso **')
        #Solicitar a la interfaz mostar el mensaje
        ic.mensaje('============== Hasta Luego! ===============')
        #Terminar el mainloop de la aplicacion
        mainloop = False
        
    #Si la opcion seleccionada es invalida
    else:
        ic.mensaje("** Entrada invalida: Intente de nuevo. **")          
 """              