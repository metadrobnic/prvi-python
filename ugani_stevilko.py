skrita_stevilka = 57
stevilka = skrita_stevilka + 1

"""
while stevilka != skrita_stevilka:
    stevilka = int(raw_input("Vpisi stevilko med 40 in 60"))
    if stevilka == skrita_stevilka:
        print ("Cestitamo")
    else:
        print("St ni prava, ugibaj naprej")
"""

while True:
    stevilka = int(raw_input("Vpisi stevilko med 40 in 60"))
    if stevilka == skrita_stevilka:
        print ("Cestitamo")
        break
    else:
        print("St ni prava, ugibaj naprej")

"""
skrita_stevilka = 57

while True:
    stevilka = int(raw_input("Vpisi stevilko med 40 in 60 "))

    if stevilka == skrita_stevilka:
        print "Cestitamo!"
        break
    elif stevilka > skrita_stevilka:
        print ("St ni prava, mora biti manjsa, ugibaj naprej")
    elif stevilka < skrita_stevilka:
        print ("St ni prava, mora biti vecja, ugibaj naprej")
"""