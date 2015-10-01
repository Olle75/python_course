# coding: utf-8
from riksdagsledamoter import data

"""
HEMUPPGIFT 1
============
Hur många riksdagsledamöter har ett son-namn?

1) Loopa listan med riksdagsledamöter
2) Kolla om personen har ett "son"-namn
3) Räkna många riksdagsledamöter som har son-namn.

Bonus:
 Räkna hur stor andel av ledamöterna i varje parti som har son-namn.

Den översta raden (from ... import ...) hämtar en lista med riksdagsledamöter
från riksdagsledamoter.py.
"""

#counter_son_names = 0
#total_number_of_mps = len(data)

#for row in data:
    # Skriv kod här!

#print("Av %s ledamöter har %s son-namn" % (total_number_of_mps, counter_son_names))

counter = 0

for row in data:
	if "son" in row["name"]:
		print("Wow, ett son-namn!")
		counter = counter + 1

print("Det finns %s ledamöter med son-namn i listan.") % (counter)

"""
# Här följer ett försök att räkna antalet son-namn per parti.
# När jag kör dem en och en får jag fram det totala antalet namn för varje parti (ej S och M som bråkar).
# Kör jag dem till sammans blir siffrorna galna - pga loopningen antar jag).
# Nästa steg blir att sålla ut son-namnen i varje parti...
 
for row in data:
	if "V" in row["party"]:
		counter = counter + 1
print("Det finns %s V i listan.") % (counter)

for row in data:
	if "S" in row["party"]:
		counter = counter + 1
print("Det finns %s S i listan.") % (counter) #Här blir det ju knasigt då även SD räknas in.

for row in data:
	if "MP" in row["party"]:
		counter = counter + 1
print("Det finns %s MP i listan.") % (counter)

for row in data:
	if "C" in row["party"]:
		counter = counter + 1
print("Det finns %s C i listan.") % (counter)

for row in data:
	if "FP" in row["party"]:
		counter = counter + 1
print("Det finns %s FP i listan.") % (counter)

for row in data:
	if "KD" in row["party"]:
		counter = counter + 1
print("Det finns %s KD i listan.") % (counter)

for row in data:
	if "M" in row["party"]:
		counter = counter + 1
print("Det finns %s M i listan.") % (counter) #Här blir det också knasigt då även MP räknas in.

for row in data:
	if "SD" in row["party"]:
		counter = counter + 1
print("Det finns %s SD i listan.") % (counter)
"""