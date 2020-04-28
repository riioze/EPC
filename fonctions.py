


def addObject(recipe, l):
	pi = []
	pf = 0
	for x in range(len(recipe)):
		ingrédient = recipe[x][0]
		n = recipe[x][1]
		p = l[ingrédient]
		prix = n*p
		pi.append(prix)
	for x in range(len(pi)):
		pf = pi[x] + pf
	return pf