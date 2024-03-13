
nom = input("quel est votre nom?")

age_prochain = 0


while age_prochain == 0:
    age = input("quel est votre âge? ")
        try:
                age_prochain = int(age) +1
                    except:
                            print("ERREUR vous devez metre les nombre pour l'age")
                            else:
                                print("vous vous appeller " + nom +", vous avez "+str(age) +"ans" )
                                    print("ans prochain vous aurais " + str(age_prochain))