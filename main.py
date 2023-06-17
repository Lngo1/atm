import mysql.connector
from tkinter import *
import datetime
def logowanie():
    podany_pin = int(pin.get())
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="bankomat")
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT * FROM `klienci` WHERE `PIN` = '{podany_pin}'")
        mycursor.fetchall()

        pokaz_menu()


    except:
        komunikat.config(text="Blad logowania")
def pokaz_menu():
    window1 = Tk()
    podany_pin = int(pin.get())
    mydb1 = mysql.connector.connect(host="localhost", user="root", password="", database="bankomat")
    mycursor1 = mydb1.cursor()
    mycursor1.execute(f"SELECT `SALDO` FROM `klienci` WHERE `PIN` = '{podany_pin}'")
    myresult = mycursor1.fetchall()
    for i in myresult:
        napis1 = Label(window1, text=i)
        napis1.grid(row=0, column=1)
    napis2 = Label(window1, text="SALDO: ")
    napis2.grid(row=0, column=0)
    window1.geometry("300x300")
    button = Button(window1,text="wplata", command=wpalt_menu)
    button.grid(row=1, column=0)
    button2 = Button(window1,text="wyplata")
    button2.grid(row=2, column=0)
    button3 = Button(window1,text="Historia")
    button3.grid(row=3, column=0)
    window1.mainloop()
def wpalt_menu():
    window2 = Tk()
    window2.geometry("200x200")
    dodajkwot = Entry(window2)
    dodajkwot.grid(row=1, column=0)
    dodajkwot_napis = Label(window2,text="Dodaj Koszty")
    dodajkwot_napis.grid(row=1, column=1)
    dodano = Button(window2,text="dodaj", command= )
    dodano.grid(row=2, column=0)
    podany_pin = int(pin.get())
    podana_kwota = dodajkwot.get()
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="bankomat")
    mycursor = mydb.cursor()
    mycursor.execute(f"UPDATE `klienci`SET `SALDO`=`SALDO`+'{podana_kwota}' WHERE 'PIN`= '{podany_pin}'")
    mycursor.fetchall()
    mydb2 = mysql.connector.connect(host="localhost", user="root", password="", database="bankomat")
    mycursor2 = mydb2.cursor()
    mycursor2.execute(f"INSERT INTO `tranzakji` (`NUMER`, `DATA`, `OPERACJI`,`ID_KLIENTA`) VALUES (%s,'{datetime.datetime.now()}','{podana_kwota}',%s)")
    etykieta1 = Label(window2,text="jest w historii")
    etykieta1.grid(row=3,column=0)
    window2.mainloop()


window = Tk()
window.geometry("200x100")
napis1 = Label(text='PIN 1 ')
napis1.grid(row=1, column=1)
pin = Entry()
pin.grid(row=1, column=0)
button = Button(text="zaloguj", command=logowanie)
button.grid(row=3, column=0)
komunikat = Label(text="")
komunikat.grid(row=4, column=0)
window.mainloop()