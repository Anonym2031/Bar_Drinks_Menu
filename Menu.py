# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect("Menu.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()


def show_menu():
    print("       Our Menu \n|_____________________|\n|                     |")
    cursor.execute("""SELECT * FROM main.Menu order by Name""")
    row = cursor.fetchone()
    while row is not None:
        print(str(row[0]) + "." + str(row[1]) + "  -  " + str(row[2] + " AMD"))
        print("\n")
        row = cursor.fetchone()


def enter():
    id_drink = str(input("  Please enter drink number  -  "))
    cursor.execute("""select ID,Name,Price from menu Where ID = (?)""", id_drink)
    row = cursor.fetchone()
    while row is not None:
        print("\n")
        print(str(row[1]) + "  -  " + str(row[2] + " AMD"))
        print("\n")
        row = cursor.fetchone()

    chose = str(input("Do You Want Buy this Drink    -   "))
    if chose == "Yes":
        print("\nThanks for buying\n")
    elif chose == "No":
        show_menu()
        enter()
    else:
        show_menu()
        enter()


print("***********************\n Welcome to Anonymous Bar\n***********************")
show_menu()
enter()
