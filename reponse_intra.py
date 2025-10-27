##########################################
# Robert, Juliette, <6293478>
##########################################
#question 1
import random

def question_1 ():
    jour=0
    temperature=[round(random.uniform(20,35),1) for i in range(10)]
    for t in temperature :
        if t <24:
            resultat="Trop froid"
        elif t >30:
            resultat="Trop chaud"
        else:
            resultat="ok"
        jour +=1
        print("Jour",jour, ":",t,"C",resultat)
question_1()
# je ne suis pas capable de mettre le degré devant le c pour degrés celsius



#question 2
import numpy as np
import matplotlib.pyplot as plt
heure=0
def question_2():
    quantite_initiale_bacterie=(input("Entrez la population initiale de bactérie"))
    quantite_initiale_bacterie= quantite_initiale_bacterie *np.pi/1.5
    heure=heure+1
plt.figure(figsize=(4,4))
plt.ylabel("Population")
plt.xlabel("Heure")
plt.tittle("Croissance bactérienne")
plt.grid()
plt.show()
plt.plot([0,50000], ".r-")






