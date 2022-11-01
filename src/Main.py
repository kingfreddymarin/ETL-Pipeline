from asyncio import tasks
import tkinter
from Extract import extract
from tkinter import *
from tkinter.ttk import *
import time


def submit():
    SSMS_SERVER = entry1.get()
    SSMS_DB = entry2.get()
    SSMS_USER = entry3.get()
    SSMS_PW = entry4.get()
    PSQL_SERVER = entry5.get()
    PSQL_DB = entry6.get()
    PSQL_USER = entry7.get()
    PSQL_PW = entry8.get()

    try:
        extract(SSMS_DB, SSMS_PW, SSMS_SERVER, SSMS_USER,
                PSQL_DB, PSQL_PW, PSQL_SERVER, PSQL_USER)
    except Exception as e:
        print("Error: " + str(e))


if __name__ == '__main__':

    window = Tk()
    window.title('Paquete ETL')

    # SUBMIT BUTTON
    submit = Button(window, text="Let's start", command=submit)

    # EVERY ENTRY
    entry1 = Entry()
    entry1.config(font=('sans', 16))
    entry1.insert(0, 'localhost')

    entry2 = Entry()
    entry2.config(font=('sans', 16))

    entry3 = Entry()
    entry3.config(font=('sans', 16))

    entry4 = Entry()
    entry4.config(font=('sans', 16))
    entry4.config(show='*')

    entry5 = Entry()
    entry5.config(font=('sans', 16))
    entry5.insert(0, 'localhost')

    entry6 = Entry()
    entry6.config(font=('sans', 16))

    entry7 = Entry()
    entry7.config(font=('sans', 16))

    entry8 = Entry()
    entry8.config(font=('sans', 16))
    entry8.config(show='*')

    # GUI LABELS
    lssms = tkinter.Label(text="SSMS DATA")
    lssms.config(font=('sans', 20))
    l1 = tkinter.Label(text="Ingrese el servidor de origen (localhost, etc):")
    l2 = tkinter.Label(
        text="Ingrese el nombre de la base de datos de origen: ")
    l3 = tkinter.Label(text="Ingrese el usuario: ")
    l4 = tkinter.Label(text="Ingrese la contraseña:")
    lpsql = tkinter.Label(text="PSQL DATA")
    lpsql.config(font=('sans', 20))
    l5 = tkinter.Label(text="Ingrese el servidor de destino (localhost, etc):")
    l6 = tkinter.Label(
        text="Ingrese el nombre de la base de datos de destino: ")
    l7 = tkinter.Label(text="Ingrese el usuario administrador de la base:")
    l8 = tkinter.Label(text="Ingrese la contraseña: ")

    # Setting up the grid SSMS
    lssms.grid(row=0, column=0)
    l1.grid(row=1, column=0)
    entry1.grid(row=2, column=0)
    l2.grid(row=3, column=0)
    entry2.grid(row=4, column=0)
    l3.grid(row=5, column=0)
    entry3.grid(row=6, column=0)
    l4.grid(row=7, column=0)
    entry4.grid(row=8, column=0)
    # Setting up the grid PSQL
    lpsql.grid(row=0, column=1)
    l5.grid(row=1, column=1)
    entry5.grid(row=2, column=1)
    l6.grid(row=3, column=1)
    entry6.grid(row=4, column=1)
    l7.grid(row=5, column=1)
    entry7.grid(row=6, column=1)
    l8.grid(row=7, column=1)
    entry8.grid(row=8, column=1)
    submit.grid(row=9, column=1)

    window.mainloop()
