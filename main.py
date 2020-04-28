from fonctions import *
import os
os.chdir("C:/Users/user/Desktop/python/projets/EPC")
fichier = open("prix.txt", "r")
l09 = ["0","1","2","3","4","5","6","7","8","9"]

liste = fichier.read()

l = {}

for x in range(len(liste)):
	modeNom = True
	nomIteml = []
	prixStrItem = ""
	nomItem = ""
	ligne = list(liste[x])
	for y in range(len(ligne)):
		print(ligne[y])
		if modeNom == True:
			if ligne [y] != ":":
				print("d3")
				nomIteml.append(ligne[y])
			if ligne [y] == ":":
				print("d2")
				modeNom = False
				del nomIteml[y-1]
				for z in range(nomIteml):
					nomItem = nomItem + nomIteml[a]
		if modeNom == False:
			print("d1")
			if ligne[y] in l09 or ligne[y] == ".":
				print(liste[x], " ", ligne[y])
				prixStrItem = prixStrItem + ligne[y]
	print("a")
	print(prixStrItem)
	print("a")
	prixItem = float(prixStrItem)
	l[nomItem] = prixItem
	print("Importation de " + " coutant " + prixStrItem)

fichier.close()
fichier = open("prix.txt", "a")


c = 0
continuer = True
while continuer == True:
	c += 1
	n = input("Nom de l'item n°" + str(c) + " : ")
	a = input("L'item est-t-il craftable (o/n) : ")
	if a == "n":
		p = float(input("Prix de l'item n°" + str(c) + " : "))
		l[n] = p
		print("création de l'objet " + n + " coutant " + str(p))
		fichier.write(n + " : " + str(p) + "\n")
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
		l[n] = o
		print("création de l'objet " + n + " coutant " + str(o))
		fichier.write(n + " : " + str(o)+ "\n")
	co = input("voulez vous ajouter un nouvel item (o/n)")
	if co == "o":
		continuer = True
	else:
		continuer = False

fichier.close()


