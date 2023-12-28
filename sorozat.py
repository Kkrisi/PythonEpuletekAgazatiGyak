

import random



def PenzFeldobas():
	global lista
	lista = []
	for nyertes in range(0,7,1):
		eredmeny = random.randint(0,1)
		lista.append(eredmeny)
	return lista




def fejek_szama():
	szamlalo = 0
	for erme in lista:
		if erme == 1:
			szamlalo += 1
	return round(szamlalo)






def konzol_kiir():
	lista = PenzFeldobas()
	szamlalo = 0
	for eredmeny in lista:
		szamlalo += 1

		if eredmeny == 1:
			eredmeny = "FEJ"
		else:
			eredmeny = "ÍRÁS"

		if szamlalo == len(lista):
			print(eredmeny,end="")
		else:
			if szamlalo == 1:
				print("\t",eredmeny,end="-")
			else:
				print(eredmeny,end="-")






def file_kiir():
	f = open('fejek.txt','w')
	f.write(f"II/F:\n\tA fejek száma: {fejek_szama()}.")
	f.close()

























