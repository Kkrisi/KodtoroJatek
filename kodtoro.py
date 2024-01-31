

# ------- Szükséges modulok meghívása -------
import os
import random







# ------- Játékhoz szükséges listák -------
def Szinek():
	szin = ["piros","zold","sarga","kek","lila","cian"]
	szinkod = ['\033[31m','\033[32m','\033[33m','\033[34m','\033[35m','\033[0;36m']
	hatterszinkod = ['\033[41m','\033[42m','\033[43m','\033[44m','\033[45m','\033[46m']

	címLista = ['Elso','Masodik','Harmadik','Negyedik','Otodik','Hatodik','Hetedik','Nyolcadik','Kilencedik']
	return szin, szinkod, hatterszinkod, címLista







# ------- Színes üdvözlő szöveg generálása -------
def Udvozles(szinkod):
	udvozles = "Üdvözöllek a Kódtörö játékban!", "Sok sikert! :)"
	udv1, udv2 = "", ""
	
	for x in udvozles[0]:
		udv1 += random.choice(szinkod) + x
	for y in udvozles[1]:
		udv2 += random.choice(szinkod) + y

	print(f"\n\t{udv1}\n\t\t{udv2}\033[37m \n\n")







# ------- Nyertes színek generálása ------- 
def NyertesSzinek(szin):
	nyertesSzinek = []
	while len(nyertesSzinek) != 4:
		i = random.randint(0,5)
		if szin[i] not in nyertesSzinek:
			nyertesSzinek.append(szin[i])
	return nyertesSzinek







# ------- Rejtett színek generálása -------
def Rejtett(szin,szinkod):
	rejtett = '\033[107m' + "     "
	rejtettLista = [rejtett,rejtett,rejtett,rejtett]

	kinalat = f"\n\n\t"
	for i in range(len(szin)):
			kinalat += szinkod[i] + szin[i] + " - "+ str(i+1) + " " +'\033[37m' + ""
	return rejtett, rejtettLista, kinalat







# ------- Nyertes színek elrejtése -------
def Elrejtes(rejtettLista):
	for nyertes in rejtettLista:
		print("\t",nyertes,end="")
		print('\033[40m'+"   ",end="")






		
# ------- A játék szíve, ő futtat mindent -------
def Motor(címLista,rejtettLista,kinalat,szin,nyertesSzinek,hatterszinkod):
	talalat = 0

	for kor in range(9):
		
		if talalat < 4:
			talalat = 0
			print(f"\n\t\t       [ ----- {címLista[kor]} kör ----- ]\n")

			Elrejtes(rejtettLista)

			print(kinalat)

			for z in range(4):
				valasztott = int(input(f"\n\tKérlek válaszd ki a {z+1}. tippedet: "))
				if szin[valasztott-1] == nyertesSzinek[z]:

					print(f"\t:) Eltaláltad, {nyertesSzinek[z]}")
					rejtettLista[z] = hatterszinkod[valasztott-1] + "     " + '\033[37m'+""
					if hatterszinkod[valasztott-1] not in rejtettLista:
						talalat += 1
			print("\n\n\n\n\n")
			if kor == 8:
				print(f"\n\t\tNem nyert!\n\tNe aggódj majd máskor összejön! :)\n")

		else:
			print(f"\n\t[ ----- Gratulálunk, Nyertél! :) ----- ]\n")
			break






























