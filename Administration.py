import sqlite3

conn = sqlite3.connect("Menu.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

try:

    cursor.execute("""CREATE TABLE Menu (ID text, Name text,Price text)""")

except:
    pass


print("Welcome to Admin Page")


def menu():
    ch = str(input("If You want add new Drink in Menu please enter Yes  \n"
                   "If You Want see Menu please enter - See Menu \n"
                   "Else If You wont exit enter any word    -   "))
    if ch == "yes":
        print("\nPlease Input New Drink 1.ID \n 2.Name \n 3.Price")
        new_drink = list([str(input(str(_ + 1) + ".  ")) for _ in range(3)])
        cursor.executemany("""INSERT INTO main.Menu (ID, Name,Price) VALUES (?,?,?)""", (new_drink,))
        conn.commit()
        cursor.execute("""SELECT * FROM main.Menu order by Name""")
        row = cursor.fetchone()
        print("****************\n       New Menu \n")
        while row is not None:
            print(str(row[0]) + "." + str(row[1]) + "  -  " + str(row[2] + " AMD"))
            print("\n")
            row = cursor.fetchone()

        menu()
    elif ch == "See Menu":
        cursor.execute("""SELECT * FROM main.Menu order by Name""")
        row = cursor.fetchone()
        while row is not None:
            print(str(row[0]) + "." + str(row[1]) + "  -  " + str(row[2] + "AMD"))
            print("\n")
            row = cursor.fetchone()
        menu()
    else:
        pass
    conn.close()


menu()
