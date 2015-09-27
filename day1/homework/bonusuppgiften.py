# -*- coding: utf-8 -*-




# -*- coding: utf-8 -*-
"""
Skriv en funktion som skriver ut matchomgången i söndagens Hockeyetta.

"""

"""
def setup_game(team1, team2):
    new_name = "%s-%s" % (team1.upper(), team2.upper())
    swedish_name = new_name.replace("å", "Å").replace("ä", "Ä").replace("ö", "Ö")
    final_name = swedish_name.replace("AIK", "GNAGET")


    print final_name


    #text = "%s'-'%s" % (team1, team2)



setup_game("aik","härnösand vännäs hc")
setup_game("brunflo ik","kalix hc")
setup_game("enköpings sk","forshaga if")
setup_game("grästorps ik","borlänge hf")
setup_game("hammarby if if","visby/roma hk")
setup_game("haninge anchors hc","södertälje sk")
setup_game("helsingborgs hc","nybro vikings if")
setup_game("huddinge ik","wings hc arlanda")
setup_game("if vallentuna bk ishockey","sollentuna hc")
setup_game("kallinge ronneby if","halmstad hf")
setup_game("kristianstads ik","hc dalen")
setup_game("köping hc","kumla hc")
setup_game("mariestad bois hc","tranås aif")
setup_game("skövde ik","lindlövens if")
setup_game("sollefteå hk","sk lejon")
setup_game("tierps hk","hudiksvalls hc")
setup_game("åker/strängnäs hc","väsby ik hk")
setup_game("örnsköldsvik hf","piteå hc")
setup_game("östersunds ik","kiruna if")

def result(resultat):



result("3–2")
result("4–7")
result("1–3")
result("3–2")
result("4–7")
result("1–3")
result("3–2")
result("4–7")
result("1–3")
result("3–2")
result("4–7")
result("1–3")
result("3–2")
result("4–7")
result("1–3")
result("3–2")
result("4–7")
result("1–3")
result("5–2")
"""


def emailify(name, domain):
    name = "%s" % (name)
    small_name = "%s@%s" % (name.lower(), domain.lower())
    english_name = small_name.replace("å", "a").replace("ä", "a").replace("ö", "o").replace("Ö", "o").replace("é", "e").replace("É", "e")
    no_dot_name = english_name.replace(" ", ".")

    print no_dot_name


"""
     Koden ska göra följande:
     1) Ersätta mellanslag med punkter i namnet.
     2) Göra alla tecken till små bokstäver
     3) Ersätta specialtecken (å,ä,ö,é) med tecken som funkar
     i en e-postadress.
     4) Printa den kompletta adressen! 
    """

emailify("Annie Lööf", "riksdagen.se")
emailify("David Lång", "riksdagen.se")
emailify("Emma Nohrén", "riksdagen.se")
emailify("阿部慎太郎", "asahi.co.jp")
emailify("Östen Rubin", "dn.se")



"""
# Vi börjar med att spara ett namn i en variabel
name = "Jens Finnäs”

# Gör om till gemener
small_name = name.lower()

# Ersätt ä => a
english_name = name.replace("ä", "a”)

# Det går även att rada fler .lower() och .replace() på varandra
small_english_name = name.lower().replace("ä", "a”)
"""