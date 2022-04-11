#Librería para interacción por consola (interfaz)
#################################################

#Librerías con las clases para construir los widgets (ventanas, botones, cambos, labels, etc)
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#LIbreria para interactuar con el backend
import CRUD

#Funcion para crear la tabla de tareas en la estructura tipo treeview
def generarTablaListadoTareas(marcoInteraccion,tareas):
    #Instanciado del treeview, permite jerarquia pero se utilizara com ouna tabla para las tareas
    TablaTareas = ttk.Treeview(marcoInteraccion)
    #Especificacion de las columnas
    TablaTareas['columns'] = ('ID', 'Descripcion', 'Estado', 'Tiempo')
    TablaTareas.column('#0', width=0, stretch=tk.NO)
    TablaTareas.column('ID', anchor=tk.CENTER, width=40)
    TablaTareas.column('Descripcion', anchor=tk.W, width=300)
    TablaTareas.column('Estado', anchor=tk.W, width=100)
    TablaTareas.column('Tiempo', anchor=tk.CENTER, width=80)
    #Especificaciones de las columnas
    TablaTareas.heading('#0', text='', anchor=tk.CENTER)
    TablaTareas.heading('ID', text='ID', anchor=tk.CENTER)
    TablaTareas.heading('Descripcion', text='Descripcion', anchor=tk.W)
    TablaTareas.heading('Estado', text='Estado', anchor=tk.CENTER)
    TablaTareas.heading('Tiempo', text='Tiempo', anchor=tk.CENTER)
    #Insertar el listado de tareas cargado en memoria proveniente de la capa de datos en la tabla
    indiceNumerico = 0
    for tareaId, tarea in tareas.items():
        TablaTareas.insert(parent='', index=indiceNumerico, iid=indiceNumerico, text='', values=(tareaId, tarea['descripcion'], tarea['estado'], tarea['tiempo']) )
        indiceNumerico += 1
    #Retornar el objeto para las actualizaciones que se generen por los eventos  
    return TablaTareas

#Funcion para crear la tabla de tareas en la estructura tipo treeview
def ventanaMenuPrincipal(tareas):
    m = tk.Tk()
    m.title("App CRUD Lista Tareas") #Especificar el titulo de la ventana

    ####### Composicion de widgets y procedimientos para el funcionamiento de la interfaz #######
    #Crear los marcos para agrupar visualmente los widgets
    marcoInteraccion = ttk.Frame(m,  borderwidth=2, relief='flat', padding=(10,10))#Formulario
    marcoCRUD = ttk.Frame(m, borderwidth=2, relief='flat', padding=(10,10))#Acciones
    
    #Crear tabla de tareas
    TablaTareas = generarTablaListadoTareas(marcoInteraccion,tareas)
    
    #Agregar entradas para los atributos de las tareas
    #Id Tarea
    etiquetaId = ttk.Label(marcoInteraccion, text='ID:')
    entradaId = ttk.Entry(marcoInteraccion)
    #Descripcion Tarea
    etiquetaDescripcion = ttk.Label(marcoInteraccion, text='Descripcion:')
    entradaDescripcion = ttk.Entry(marcoInteraccion)
    #Estado Tarea
    etiquetaEstado = ttk.Label(marcoInteraccion, text='Estado:')
    entradaEstado = ttk.Entry(marcoInteraccion)
    #Tiempo Tarea
    etiquetaTiempo = ttk.Label(marcoInteraccion, text='Tiempo:')
    entradaTiempo = ttk.Entry(marcoInteraccion)
    
    #Funcion que limpia los campos del formulario (marcoInteraccion)
    def limpiarCampos():
        entradaId.delete(0,tk.END)
        entradaDescripcion.delete(0,tk.END)
        entradaEstado.delete(0,tk.END)
        entradaTiempo.delete(0,tk.END)
    #Boton para limpiar los campos
    btnLimpiarCampos = ttk.Button(marcoInteraccion, text='Limpiar Campos', command=limpiarCampos)
    
    #Cargar informacion de la tarea seleccionada
    def cargarTareaSeleccionada():
        #Estraer informacion de la interfaz
        seleccionada = TablaTareas.focus()
        print(seleccionada)
        infoSeleccionada = TablaTareas.item(seleccionada, 'values')
        print(infoSeleccionada)
        #Limpiar los campos
        limpiarCampos()
        #Cargar la informacion extraida
        entradaId.insert(0,infoSeleccionada[0])
        entradaDescripcion.insert(0,infoSeleccionada[1])
        entradaEstado.insert(0,infoSeleccionada[2])
        entradaTiempo.insert(0,infoSeleccionada[3])            
    #Boton para cargar la tarea seleccionada
    btnCargarTareaSeleccionada = ttk.Button(marcoInteraccion, text='Cargar Info Tarea Seleccionada', command=cargarTareaSeleccionada)   
   
    #Ubicacion de los elementos (frame para el formulario) de interaccion en la ventana principal
    marcoInteraccion.grid(column=0, row=0)
    TablaTareas.grid(column=0,row=0,columnspan=3)
    etiquetaId.grid(column=0,row=1,sticky=tk.W)
    entradaId.grid(column=1,row=1)
    etiquetaDescripcion.grid(column=0,row=2,sticky=tk.W)
    entradaDescripcion.grid(column=1,row=2)
    etiquetaEstado.grid(column=0,row=3,sticky=tk.W)
    entradaEstado.grid(column=1,row=3)
    etiquetaTiempo.grid(column=0,row=4,sticky=tk.W)
    entradaTiempo.grid(column=1,row=4)
    btnLimpiarCampos.grid(column=2,row=2)
    btnCargarTareaSeleccionada.grid(column=2,row=3)
    
    ####### Composicion de widgets y procedimientos para las operaciones CRUD de la interfaz #######
    #Funcion intermediaria para preparar informacion recogida de los campos y CRUD
    #redirige la informacion encapsulada a los eventos especificados en los botones
    def encapsularInfoFormulario(accion):
        #Obtener tareaId de las entradas
        tareaId = entradaId.get()
        #Intentar convertir el tiempo a tipo entero
        try:
            entradaTiempoFormatoEntero = int(entradaTiempo.get())
        except:
            #Colocar un valor por defecto si no es posible realizar el parseo
            entradaTiempoFormatoEntero = 0
        #Encapsular informacion
        infoCampos = {
            'descripcion': entradaDescripcion.get(),
            'estado': entradaEstado.get(),
            'tiempo': entradaTiempoFormatoEntero
        }
        #Revisar evento del boton para iniciar las acciones correspondientes en las otras capas
        if accion == 'Create':
            #Llamar la funcion que realiza la actualizacion de la vista y el backend
            adicionarTarea(TablaTareas, tareas, tareaId, infoCampos)
        elif accion == 'Update':
            #Llamar la funcion que realiza la actualizacion de la vista y el backend
            actualizarTarea(TablaTareas, tareas, tareaId, infoCampos)
        elif accion == 'Delete':
            #Llamar la funcion que realiza la actualizacion de la vista y el backend
            eliminarTarea(TablaTareas, tareas, tareaId, infoCampos)
    
    #Funcion que realiza la adicion de la tarea en la vista y backend
    def adicionarTarea(TablaTareas, tareas, tareaId, tareaNueva):
        #Actualiza la interfaz acorde a la operacion solicitada
        #Limpiar los campos de la interfaz
        limpiarCampos()
        #Actualizar el widget correspondiente en la interfaz
        indiceNumerico = len(TablaTareas.get_children())
        TablaTareas.insert(parent='', index=indiceNumerico, iid=indiceNumerico, text='', values=(tareaId, tareaNueva['descripcion'], tareaNueva['estado'], tareaNueva['tiempo']))
        #Llamar el backend para actualizar el contenedor de las tareas
        CRUD.Create(tareas, tareaId, tareaNueva)
    #Boton para adicion de tarea, desencadenando los eventos en las demas capas
    btnAdicionarTarea = ttk.Button(marcoCRUD, text='Adicionar Tarea', command=lambda : encapsularInfoFormulario('Create'))
    
    #Función que realiza la actualización de la tarea cargada en la vista y el backend
    def actualizarTarea(TablaTareas, tareas, tareaId, tareaNueva):
        #Actualizar la interfaz acorde a la operación solicitada
        #Limpiar los campos de la interfaz
        limpiarCampos()        
        #Eliminar todos los elementos (filas o hijos) de la tabla de la interfaz
        for i in TablaTareas.get_children():
            TablaTareas.delete(i)
        #Actualizar el contenedor cargado en memoria (llamado a backend)
        CRUD.Update(tareas, tareaId, tareaNueva)
        #Insertar en la vista todas las tareas que están cargadas en memoria
        indiceNumerico = 0
        for tareaId, tarea in tareas.items():
            TablaTareas.insert(parent='', index=indiceNumerico, iid=indiceNumerico, text='', values=(tareaId, tarea['descripcion'], tarea['estado'], tarea['tiempo']) )
            indiceNumerico += 1   
    #Botón para actualización de tarea, desencadenando los eventos en las demás capas    
    btnActualizarTarea = ttk.Button(marcoCRUD, text='Actualizar Tarea', command = lambda : encapsularInfoFormulario("Update")  )

    #Función que realiza la eliminación de la tarea cargada en la vista y el backend
    def eliminarTarea(TablaTareas, tareas, tareaId, tareaNueva):    
        #Actualizar la interfaz acorde a la operación solicitada
        #Limpiar los campos de la interfaz
        limpiarCampos() 
        #Eliminar todos los elementos (filas o hijos) de la tabla de la interfaz
        for i in TablaTareas.get_children():
            TablaTareas.delete(i)
        #Actualizar el contenedor cargado en memoria (llamado a backend)
        CRUD.Delete(tareas, tareaId)     
        #Insertar en la vista todas las tareas que están cargadas en memoria posterior a la eliminación
        indiceNumerico = 0
        for tareaId, tarea in tareas.items():
            TablaTareas.insert(parent='', index=indiceNumerico, iid=indiceNumerico, text='', values=(tareaId, tarea['descripcion'], tarea['estado'], tarea['tiempo']) )
            indiceNumerico += 1
    #Botón para eliminación de tarea, desencadenando los eventos en las demás capas    
    btnEliminarTarea = ttk.Button(marcoCRUD, text='Eliminar Tarea', command = lambda : encapsularInfoFormulario("Delete")  )
    
    #Función que guarda los cambios y cierra la aplicación
    def salirGuardar():
        #Solicitar al backend que actualice la base de datos
        CRUD.Write(tareas)
        #Informar a través de la interfaz gráfica
        messagebox.showinfo(message="Información guardada en capa de datos", title="Cierre Sesión")       
        #Cerrar la ventana
        m.destroy()
    #Botón para salir y guardar cambios
    btnSalirGuardar = ttk.Button(marcoCRUD, text='Salir y Guardar', command = salirGuardar  )
    
    #Carga de imagen para asociar a widget tipo etiqueta
    from PIL import ImageTk, Image #Libreria para procesar formato png y redimensionar
    #Proporciones de la imagen
    w = 120
    h = 140
    imagenCargada = Image.open('imagenListaTareas.png')
    imagenCargada.thumbnail((w,h))
    imagenListaTareas = ImageTk.PhotoImage(imagenCargada)#Encapsular para tkinter
    #Creacion de la etiqueta
    etiquetaImagenListaTareas = tk.Label(marcoCRUD)
    #Asociacion de la imagen a etiqueta
    etiquetaImagenListaTareas.config(image=imagenListaTareas, width=w, height=h)
    etiquetaImagenListaTareas.image = imagenListaTareas
    
    #Etiqueta informativa funcionamiento App
    mensajeFuncionamiento = "-> Cargar Info antes de CRUD"
    etiquetaFuncionamiento = ttk.Label(marcoCRUD, text=mensajeFuncionamiento)
    
    #Ubicacion de los botones del CRUD
    marcoCRUD.grid(column=1,row=0,rowspan=5,sticky=tk.N+tk.S)
    etiquetaImagenListaTareas.grid(column=1,row=0, sticky=tk.W+tk.E )
    btnAdicionarTarea.grid(column=1,row=1,sticky=tk.W+tk.E)
    btnActualizarTarea.grid(column=1,row=2,sticky=tk.W+tk.E)
    btnEliminarTarea.grid(column=1,row=3,sticky=tk.W+tk.E)
    btnSalirGuardar.grid(column=1,row=4,sticky=tk.W+tk.E)
    etiquetaFuncionamiento.grid(column=1,row=5)
    
    #Retornar ventana con elemtos y funcionalidades de la App al controlador para que inicie mainloop
    return m