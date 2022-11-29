print ("Tere! Olen sinu uus sõber - Python!")
nimi=input("Mis su nimi on?\n")
print(f"{nimi}, oi kui ilus nimi!")
otvet=input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah =>")
if otvet=="1":
    try:
        pikkus=input("Enter your pikkus \n")
        try:
            pikkus=int(pikkus)
        except:
            print("An exception occurred")
    except:
        print("An exception occurred")
    try:
        mass=input("Enter your mass \n")
        try:
            mass=float(mass)
        except:
            print("An exception occurred")
    except:
        print("An exception occurred")
    mass=int(mass)
    index=mass/((0.01*pikkus)**2)
    index=int(index)
    print (f"Your index is {index}")
    if index<16:
        print("Tervisele ohtlik alakaal")
    elif index>=16 and index <19:
        print("Alakaal")
    elif index>=19 and index <25:
        print("Normaalkaal")
    elif index>=25 and index <30:
        print("Ulekaal")
    elif index>=30 and index <35:
        print("Rasvumine")
    elif index>=35 and index <40:
        print("Tugev rasvumine")
    elif index>=40:
        print("Tervisele ohtlik rasvumine")       
else:
    print("Kahju! See on väga kasulik info!\n")
    print(f"Kohtumiseni, {nimi}! Igavesti Sinu, Python!")
    
