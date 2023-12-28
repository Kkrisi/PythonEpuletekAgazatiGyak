





def Bekeres():
	nev, szerepkor, elet = "", "", 0
	while nev == "" or szerepkor == "":
		if nev == "":
			nev = str(input("Add meg a játékosneved: "))
		if szerepkor == "":
			szerepkor = str(input("Add meg a szerepköröd: "))
	if szerepkor == "varazslo" or szerepkor == "varázsló" :
		elet = 2
	elif szerepkor == "harcos":
		elet = 10
	else:
		elet = 8 

	return nev.capitalize(), szerepkor, elet







