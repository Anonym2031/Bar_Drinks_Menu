def adm_or_clt():
    user = str(input("If you Admin enter \"Admin\" else enter \"Client\"    -  "))
    if user == "Admin":
        print("Welcome To Administration,  You can add new drink and her Price\n ")
        y_or_n = str(input("Add new drink  ?  -  "))
        if y_or_n == "Yes":
            new_name = str(input("\n Please enter the new drink Name   -  "))
            new_price = str(input("\nPlease enter the new drink Price  - "))
            add_new_drink(new_name, new_price)
            show_menu(drink, dr_price)
            print("Thanks for editing , Please chose \"Client\" if you want buy Drink ")
            adm_or_clt()
        if y_or_n == "No":
            print("Thanks for editing , Please chose \"Client\" if you want buy Drink ")
            adm_or_clt()
    elif user == "Client":
        show_menu(drink, dr_price)
        price(drink, dr_price)

    else:
        return print("Error")


def add_new_drink(new_name, new_price):
    drink.append(new_name)
    dr_price.append(new_price)


def show_menu(db1, db2):
    print("       Our Menu \n|_____________________|\n|                     |")
    for _ in range(len(db1)):
        print("  " + str(db1[_]) + "    -     " + str(db2[_]) + "\n")


def price(db1, db2):
    name = str(input("  Please enter drink   -  "))
    for i in range(len(db1)):
        if name == db1[i]:
            print("Buy " + db1[i] + " For Price  " + str(db2[i]) + "?   -   ")
            chose = str(input())
            if chose == "Yes":
                print("Thanks for buying\n")
            elif chose == "No":
                show_menu(db1, db2)
                price(db1, db2)
            else:
                show_menu(db1, db2)
                price(db1, db2)


drink = ["Coca-Cola", "Fanta", "Wine", "Sprite"]
dr_price = [250, 250, 1500, 250]
print("***********************\n Welcome to Anonymous Bar\n***********************")
adm_or_clt()
