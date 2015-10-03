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
	if "son," in row["name"] or "son " in row["name"]:
		print("Wow, ett son-namn!")
		counter = counter + 1

print("Det finns %s ledamöter med son-namn i listan.") % (counter)
"""



# Här följer ett försök att räkna antalet son-namn per parti.
# När jag kör dem en och en får jag fram det totala antalet namn för varje parti (ej S och M som bråkar).
# Kör jag dem tillsammans blir siffrorna galna - pga loopningen antar jag).
# Nästa steg blir att sålla ut son-namnen i varje parti...
 
"""

"""
for row in data:
	if "V" in row["party"]:	
		if "son," in row["name"] or "son " in row["name"]:
			counter = counter + 1
print("Det finns %s son-namn i listan.") % (counter)
"""

"""
for row in data:
	if "S" == "S" in row["party"]:
		if "son," in row["name"] or "son " in row["name"]:
			counter = counter + 1
print("Det finns %s son-namn i listan.") % (counter)
"""
"""
for row in data:
	if "MP" in row["party"]:
		if "son," in row["name"] or "son " in row["name"]:
			counter = counter + 1
print("Det finns %s son-namn i listan.") % (counter)

"""

"""
for row in data:
	if "C" in row["party"]:
		if "son," in row["name"] or "son " in row["name"]:
			counter = counter + 1

print("Det finns %s son-namn i listan.") % (counter)
"""

"""
for row in data:
	if "FP" in row["party"]:
		if "son," in row["name"] or "son " in row["name"]:
			counter = counter + 1
print("Det finns %s son-namn i listan.") % (counter)
"""
"""
for row in data:
	if "KD" in row["party"]:
		if "son," in row["name"] or "son " in row["name"]:
			counter = counter + 1
print("Det finns %s son-namn i listan.") % (counter)
"""
"""
for row in data:
	if "M" == "M" in row["party"]:
		if "son," in row["name"] or "son " in row["name"]:
		counter = counter + 1
print("Det finns %s son-namn i listan.") % (counter)
"""
"""
for row in data:
	if "SD" in row["party"]:
		if "son," in row["name"] or "son " in row["name"]:
			counter = counter + 1
print("Det finns %s son-namn i listan.") % (counter)
"""