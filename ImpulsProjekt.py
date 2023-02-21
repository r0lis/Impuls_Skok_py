# importování potřebných knihoven
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('data.xlsx', usecols = "H"); #načtení sloupce H z xlsx souboru

maxV = data.values.max() # uložení maximální hodnoty do proměnné

# pro jednodušší práci s daty jsou hodnoty uloženy v poli
vsechny = []
for values in data.values:
    vsechny.extend(values)

indexMax = vsechny.index(maxV) # najdutí indexu maximální hodnoty
mensiJakMax = vsechny[0:indexMax] # zkrácení pole po index maximální hodnoty



def Average(lst): # funkce pro zjištění průměrné hladiny hodnot
    return sum(lst) / len(lst)
prvnichPetset = []
prvnichPetset = mensiJakMax[0:500] #vytvoření pole s hodnotami pole mensiJakMax po index 500 pro zjištění průměrné hladiny
prumerPrvnichPetset = Average(prvnichPetset) # použití funkce Average

poZadu = []

poZadu = mensiJakMax[::-1] # s hodnotami pracujeme pozadu, hodnoty pole mensiJakMax jsou přidány do pole poZadu

# vykreslení grafu
x = np.arange(0,len(mensiJakMax))
y = np.array(mensiJakMax)

plt.title("Line graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.plot(x, y, color="green")
plt.hlines(prumerPrvnichPetset, 1, len(x), color='r')
plt.show()

idx = np.argwhere(np.diff(np.sign(y - prumerPrvnichPetset))).flatten() #vyhledání bodů které protínají průměrnou hladinu
arr = []
# načtení bodů do pole
for i in idx:
    arr.append(i)

hi = arr[-2] #3
mi = arr[-3] #2
li = arr[-4] #1

g = 9.81
fvz = 1000
m = prumerPrvnichPetset/g
S1 = np.trapz(y[li:mi])
S2 = (mi - li) * prumerPrvnichPetset - S1
S3 = np.trapz(y[mi:hi])
S4 = S3-(hi-mi)* prumerPrvnichPetset
I = (S4-S2)/fvz
h = I**2/(2*g*m**2)

print("max hodnota je",+ maxV)
print("prumerna hodnota 500 vzorku",+prumerPrvnichPetset)
print()
print("impuls = ", round(I,4))
print("vyska vyskoku = ",round(h,4))





