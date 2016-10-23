print("To je program za pretvarjanje enot")

kilometri = int(raw_input("Vnesi stevilo kilometrov: "))
conv_fac = 0.621371
milje = kilometri * conv_fac
print("To je " + str(milje) +" milj")



while True:
    answer = raw_input("Zelis narediti novo pretvorbo? (yes/no)")
    if answer == "yes":
        kilometri = int(raw_input("Vnesi stevilo kilometrov: "))
        conv_fac = 0.621371
        milje = kilometri * conv_fac
        print("To je " + str(milje) + " milj")

    elif answer == "no":
        print ("adijo")
        break
    else:
        print("napaka, odgovori z yes ali no")
