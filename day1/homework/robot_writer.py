# -*- coding: utf-8 -*-

""" Se robot_writer.md för instruktioner
"""

# coding: utf-8

kommun = "Hägersten"
total_unemployment_2009 = 2.9
total_unemployment_2014 = 5.9
diff = total_unemployment_2014 - total_unemployment_2009
name = "Olle Carlsson"

def write_story(kommun, unemployment_2009, unemployment_2014):
   text = "Arbetslösheten i %s var 2009 %s procent. 2014 var den %s procent." % (kommun, unemployment_2009, unemployment_2014)
   print(text)

write_story(kommun, total_unemployment_2009, total_unemployment_2014)

if total_unemployment_2014 > total_unemployment_2009:
    print("Det var en ökning med %s procent" % (diff))   
elif total_unemployment_2014 < total_unemployment_2009:
	print("Det var en minskning med %s procent" % (diff))
elif total_unemployment_2014 == total_unemployment_2009:
   print("Det var ingen skillnad")

print("%s, %s") % (name, kommun) 

    # Skriv kod här!



write_story("Stockholm", 7.1, 6.6) 
print("**************")

write_story("Kiruna", 7.6, 4.2) 
print("**************")

write_story("Lessebo", 9.5, 13.2) 
print("**************")

"""Källa: http://www.ekonomifakta.se/sv/Fakta/Regional-statistik/Din-kommun-i-siffror/"""