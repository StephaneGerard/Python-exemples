# Test de vairable sous Pyhton
#----------------------------
i=12
my_text="test de texte avec boucle"
my_list=[10,20,30,40]
my_tuple=('Stephane',28,True)
my_dict = {"Car":"Corvette","Age":2,"Power":350}
x=range(10)
y=range(10)
z=[1,2]

for lettre in my_text:
    print (lettre)
print ("Integer i=",i)
print ("Liste, élément n°",my_list)
print ("Nombre d'éléments de la liste",len(my_list))
print ("Utilisation de la fonction Range")

print ("Valeur de x : ",x)
for i in x:
    print ("Liste, élément n°",i,"contenu",x[i])

print ("Valeur de x : ",x)

for i in y:
    print ("Liste, élément n°",i,"contenu",y[i])

print ("Valeur de y : ",y)

print ("Valeur de z : ",z)
z5=z*5
print ("Valeur de z5 : ",z5)
for i in z5:
    print ("Liste, élément n°",i,"contenu",z5[i])

print ("Test sur les dictionnaires")
# Ne pas ouvblier d'uitliser les quotes !
print ("La voiture est :",my_dict["Car"],"de puissance :", my_dict["Power"])
