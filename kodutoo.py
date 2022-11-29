if int(otvet)==1:
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

