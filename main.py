from fonctions import *
import os
os.chdir("C:/Users/user/Desktop/python/projets/EPC")
fichier = open("prix.txt", "w")
l = {}
c = 0
continuer = True
while continuer == True:
	c += 1
	n = input("Nom de l'item n°" + str(c) + " : ")
	a = input("L'item est-t-il craftable (o/n) : ")
	if a == "n":
		p = float(input("Prix de l'item n°" + str(c) + " : "))
		l[n] = p
	if a == "o":
		nitem = int(input("Nombre d'item differents dans la recette"))
		r = []
		for x in range(nitem):
			a = []
			item = input("item n" + str(x))
			q = int(input("Quantité de l'item"))
			a.append(item)
			a.append(q)
			r.append(a)
		o = addObject(r,l)
	co = input("voulez vous ajouter un nouvel item (o/n)")
	if co == "o":
		continuer = True
	else:
		continuer = False


