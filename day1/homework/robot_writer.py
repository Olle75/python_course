# coding: utf-8

#Olles hemläxa!

<<<<<<< HEAD
total_unemployment_2009 = 2.9
total_unemployment_2014 = 1.9
riket_unemployment_2009 = 3.8
riket_unemployment_2014 = 10.9
diff_riket2014 = riket_unemployment_2014 - total_unemployment_2014
=======
total_unemployment_2009 = 5.9
total_unemployment_2014 = 8.0

def write_story(municipality, unemployment_2009, unemployment_2014):
    text = "Gör mig till en notis"
    print("Nu har jag löst uppfiften!")
    print(text)
    # Skriv kod här!
>>>>>>> 0b75cc4a73af7947e0872f98e2a85a320a992abd

name = "Olle Carlsson"
municipality = "Hägersten"

def write_story(municipality, unemployment_2009, unemployment_2014):
  diff = unemployment_2014 - unemployment_2009
  text = "Arbetslösheten i %s var 2009 %s procent. 2014 var den %s procent." % (municipality, unemployment_2009, unemployment_2014)
  print(text)

  if unemployment_2014 > unemployment_2009:
    print("Det var en ökning med %s procent.") % (abs(diff))
    print("Alltså kan man konstatera att finanskrisen drabbade %s hårt." % (municipality))
  elif unemployment_2014 < unemployment_2009:
    print("Det var en minskning med %s procent.") % (abs(diff))
    print("Alltså kan man konstatera att %s klarade finanskrisen alldeles utmärkt." % (municipality))
  elif unemployment_2014 == unemployment_2009:
    print("Det var ingen skillnad")
    print("Finanskrisen påverkade alltså inte %s alls." % (municipality))

  if unemployment_2014 > riket_unemployment_2014:
    print("Arbetslösheten i %s var %s procent högre jämfört med hela riket 2014.") % (municipality, abs(diff_riket2014)) 
  elif unemployment_2014 < riket_unemployment_2014:
    print("Arbetslösheten i %s var %s procent lägre jämfört med hela riket 2014.") % (municipality, abs(diff_riket2014))
  elif unemployment_2014 == riket_unemployment_2014:
      print("Arbetslösheten i %s låg på samma nivå som i hela riket." % (municipality))

  if unemployment_2014 < riket_unemployment_2014:
    print("%s står starkt i krisen.") % (municipality)
  elif unemployment_2014 > riket_unemployment_2014:
    print("%s är en förlorare i krisen.") % (municipality)
  elif unemployment_2014 == riket_unemployment_2014:
    print("%s klarar krisen som alla andra.") % (municipality)


write_story("Stockholm", 7.1, 6.6) 
print("%s / %s") % (name, municipality)
print("**************")

write_story("Kiruna", 7.6, 7.6) 
print("%s / %s") % (name, municipality)
print("**************")

write_story("Lessebo", 9.5, 13.2) 
print("%s / %s") % (name, municipality)
print("**************")