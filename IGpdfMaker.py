from tkinter import *
from tkinter import messagebox
from tkinter import Tk
import os
import sys
import errno
import easygui
from PIL import Image, ImageDraw, ImageFont


def jpg():
    try:
        os.mkdir('pdfMakerArchivosJPG')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    ruta_archivo = easygui.fileopenbox()

    w = 4000
    h = 2250
    W_text = w/2-1000
    image = Image.open(ruta_archivo)
    NewImg = image.resize((w,h))

    font = ImageFont.truetype( 'arial.ttf', 150)
    font_CI = ImageFont.truetype( 'arial.ttf', 100)

    draw = ImageDraw.Draw(NewImg)
    print(NewImg.size)

    draw.text((w/2-190,750),suNombre.get(),(0,0,0),font=font)
    draw.text((w/2-300,930),"C.I: " + suCedula.get(),(0,0,0),font=font_CI)

    NewImg.show()
    NewImg.save("pdfMakerArchivosJPG/" + archivo.get() + ".JPEG","JPEG")
    messagebox.showinfo(title="pdfMaker ha creado el archivo: ",message="El certificado a sido creado para: " )

def pdf():
    # Librerias
    from reportlab.lib.units import cm
    from reportlab.pdfgen.canvas import Canvas
    from reportlab.platypus import Frame, Image


    try:
        os.mkdir('pdfMakerArchivos')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    ruta_archivo = easygui.fileopenbox()



    # W = Ancho H = Alto del archivo
    w = 4000
    h = 2250
    # El lienzo del archivo
    c = Canvas("pdfMakerArchivos/" + archivo.get() + suNombre.get() + ".pdf",pagesize=(w,h))
    c.setTitle(archivo.get())

    # La imagen del certificado
    c.drawImage(ruta_archivo, 1,1, width=w, height=h)

    # los datos del usuario
    certificado = suNombre.get()
    ci = "C.I: " + str(suCedula.get())

    # Comandos para insertarlos y ubicarlos en el archivo
    c.setFont('Helvetica-Bold', 150)
    c.drawCentredString(w/2,1350,certificado)
    c.setFont('Helvetica', 100)
    c.drawCentredString(w/2,1230,ci)

    #Guardar el archivo
    c.save()

    if os.path.isfile("pdfMakerArchivos/" + str(archivo.get()) + str(suNombre.get()) + ".pdf"):
        #Mesaje de todo correcto
        messagebox.showinfo(title="pdfMaker ha creado el archivo: " + str(archivo.get()),message="El certificado a sido creado para: " + str(certificado))
    else:
        #Mensaje de algo salio mal
        messagebox.showwarning(title="Error: 404 Not Found ", message="El archivo no se a creado correctamente")


#Se crea la ventana
master = Tk()
master.title("PdfMaker")

main_frame = Frame(master)
main_frame.pack()
main_frame.pack_propagate(0)
main_frame.config(bg="black",width="500",height="300")

frame = Frame(main_frame)
frame.pack(anchor="c")
frame.pack_propagate(0)
frame.config(width="300",height="200")

black= "#181616"
white= "white"
frame.config(bg=black)
#Estilos para los texto de los Label y Entry
disenoText = ('Helvetica',10,"bold")
disenoText1 = ('Helvetica',10)

#Label y Entry para Ingresar el nombre del archivo
lblarchivo = Label(frame,text="Nombre del archivo:",fg=white,bg=black,font=disenoText)
lblarchivo.pack(anchor=W,pady=2)

archivo = StringVar()
Archivo = Entry(frame,textvariable=archivo,width=50,bd=1,font=disenoText1)
Archivo.pack()

Archivo.focus()

#Entry para Ingresar el nombre de la persona
lblnombre = Label(frame,text="Nombre:",bg=black,fg=white,font=disenoText)
lblnombre.pack(anchor=W,pady=2)

suNombre = StringVar()
Nombre =Entry(frame,textvariable=suNombre,width=50,bd=1,font=disenoText1)
Nombre.pack()

#Entry para ingresar la cedula de la persona
lblCedula = Label(frame,text="Cedula:",fg=white,bg=black,font=disenoText)
lblCedula.pack(anchor=W,pady=2)

suCedula = StringVar()
Cedula = Entry(frame,textvariable=suCedula,width=50,bd=1,font=disenoText1)
Cedula.pack()

#El boton para Activar la Funcion que crea el archivo
btnPdf = Button(frame,bg="white",text="Crear Pdf",command=pdf)
btnPdf.pack(pady=5)

master.mainloop()
