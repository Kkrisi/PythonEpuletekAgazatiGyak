

from EpuletClass import Epulet





def fajlBeolvasas():
	fajl = open("epulet.txt","r",encoding="UTF-8")
	fajl.readline()
	sorokLista = fajl.readlines()
	fajl.close()

	epuletLista = []
	for i in range(0,len(sorokLista),1):
		aktElem = sorokLista[i]
		sorLista = aktElem.strip().split('$')
		nev = str(sorLista[0])
		varos = str(sorLista[1])
		orszag = str(sorLista[2])
		magassag = float(sorLista[3])
		emelet = int(sorLista[4])
		epult = int(sorLista[5])

		epulet=Epulet(nev,varos,orszag,magassag,emelet,epult)
		epuletLista.append(epulet)

	return epuletLista




def EpuletSzamolas():
	global lista
	lista = fajlBeolvasas()
	szamlalo = 0
	for epulet in lista:
		szamlalo += 1
	return szamlalo





def MagasEpuletek():
	szamlalo = 0
	kulonbseg = 3.280839895
	for i in range(0,len(lista),1):
		if lista[i].magassag * kulonbseg > 555:	
			szamlalo += 1
	return szamlalo





def LegoregebbEpulet():
	legoregebb = 2023
	for i in range(0,len(lista),1):
		if lista[i].epult < legoregebb:
			legoregebb = lista[i].epult
			orszag = lista[i].orszag
	return orszag
	 





















