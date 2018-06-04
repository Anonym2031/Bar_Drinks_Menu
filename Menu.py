def show_menu(db1, db2):
    print("       Our Menu \n|_____________________|\n|                     |")
    for _ in range(len(db1)):
        print("  " + str(db1[_]) + "    -     " + str(db2[_]) + "\n")


def price(db1, db2):
    name = str(input("  Please chose drink   -  "))
    for i in range(len(db1)):
        if name == db1[i]:
            print("Buy " + db1[i] + " For Price  " + str(db2[i]) + "?   -   ")
            chose = str(input())
            if chose == "Yes":
                print("Thanks for buying\n")
            elif chose == "No":
                show_menu(db1, db2)
                price(drink, dr_price)
            else:
                show_menu(db1, db2)
                price(drink, dr_price)


drink = ["Cola", "Fanta", "Wine"]
dr_price = [250, 250, 1500]
print("***********************\n Welcome to Anonym Bar\n***********************")
show_menu(drink, dr_price)
price(drink, dr_price)
