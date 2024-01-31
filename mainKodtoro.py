
# Kodtoro jatek

from kodtoro import *



def Jatek():
	os.system("")

	szin, szinkod, hatterszinkod, címLista = Szinek()

	Udvozles(szinkod)

	nyertesSzinek = NyertesSzinek(szin)

	rejtett, rejtettLista, kinalat = Rejtett(szin,szinkod)

	Motor(címLista,rejtettLista,kinalat,szin,nyertesSzinek,hatterszinkod)


Jatek()