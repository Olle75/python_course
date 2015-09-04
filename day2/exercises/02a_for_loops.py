# -*- coding: utf-8 -*-

""" ÖVNING:
	Hur många riksdagsledamöter har ett -son-namn?
	Skriv en for-loop som kolla om riksdagsledamotens namn innehåller "son"
	och i så fall plussar på 1 till variabeln count.

"""

mps = ['Abdu, Said (FP)','Abrahamsson, Maria (M)','Acketoft, Tina (FP)','Adan, Amir (M)','Ahl, Jeff (SD)','Ahlberg, Ann-Christin (S)','Ahlgren, Anders (C)','Alm Ericson, Janine (MP)','Amin, Jabar (MP)','Andersson Willner, Maria (S)','Andersson, Erik (M)','Andersson, Jan R (M)','Andersson, Johan (S)','Andersson, Jörgen (M)','Andersson, Phia (S)','Andersson, Ulla (V)','Arkelsten, Sofia (M)','Arnholm, Maria (FP)','Ask, Beatrice (M)','Asplund, Lena (M)','Avsan, Anti (M)','Axelsson, Lennart (S)','Bali, Hanif (M)','Bengtsson, Angelika (SD)','Bengtsson, Finn (M)','Bengtzboe, Erik (M)','Berg, Ulf (M)','Bergheden, Sten (M)','Bergman, Håkan (S)','Bergstedt, Hannah (S)','Bergström, Stina (MP)','Bieler, Paula (SD)','Bill, Per (M)','Billström, Tobias (M)','Bjälkö, Sara-Lena (SD)','Björck, Patrik (S)','Björklund, Jan (FP)','Björlund, Torbjörn (V)','Bohlin, Carl-Oskar (M)','Bouveng, Helena (M)','Bråkenhielm, Catharina (S)','Brännström, Katarina (M)','Bylund, Linus (SD)','Büser, Johan (S)','Bäckström Johansson, Mattias (SD)','Bäckström, Daniel (C)','Börjesson, Agneta (MP)','Carlson, Andreas (KD)','Carlsson Löfdahl, Emma (FP)','Carlsson, Gunilla (S)','Carlsson, Ulrika i Skövde (C)','Carvalho, Teresa (S)','Cederbratt, Mikael (M)','Cederfelt, Margareta (M)','Christensson, Fredrik (C)','Coenraads, Åsa (M)','Dadgostar, Nooshi (V)','Dahlqvist, Mikael (S)','Dalunde, Jakop (MP)','Damm, Sofia (KD)','Danielsson, Staffan (C)','Delis, Sotiris (M)','Dibrani, Adnan (S)','Dinamarca, Rossana (V)','Dingizian, Esabelle (MP)','Dioukarev, Dennis (SD)','Drougge, Ida (M)','Eberstein, Susanne (S)','Eclund, Annika (KD)','Ekeroth, Kent (SD)','Ekström, Hans (S)','Eliasson, Bengt (FP)','Emilsson, Aron (SD)','Emilsson, Lena (S)','Eneroth, Tomas (S)','Engblom, Annicka (M)','Engström, Patrik (S)','Enström, Karin (M)','Ericson, Jan (M)','Eriksson, Fredrik (SD)','Eriksson, Jonas (MP)','Eriksson, Lars (S)','Eriksson, Sanne (S)','Erlandsson, Eskil (C)','Ernkrans, Matilda (S)','Esbati, Ali (V)','Eskilandersson, Mikael (SD)','Ezelius, Erik (S)','Felten, Olle (SD)','Filper, Runar (SD)','Finnborg, Thomas (M)','Finstorp, Lotta (M)','Forsberg, Anders (SD)','Forslund, Kenneth G (S)','Forssell, Johan (M)','Forssmed, Jakob (KD)','Fransson, Josef (SD)','From, Isak (S)','Fölster, Sofia (M)','Gamov, Pavel (SD)','Ghasemi, Tina (M)','Gille, Agneta (S)','Granlund, Marie (S)','Green, Mats (M)','Green, Monica (S)','Gunnarsson, Jonas (S)','Gunther, Penilla (KD)','Güclü Hedin, Roza (S)','Haddad, Roger (FP)','Hagwall, Anna (SD)','Haider, Monica (S)','Halef, Robert (KD)','Hallengren, Lena (S)','Hallström, Pia (M)','Hamednaca, Arhe (S)','Hammar Johnsson, Ann-Charlotte (M)','Hammarbergh, Krister (M)','Hannah, Robert (FP)','Hansson, Anders (M)','Haraldsson, Johanna (S)','Hedin, Johan (C)','Hedlund, Roger (SD)','Hellman, Jörgen (S)','Helmersson Olsson, Caroline (S)','Henriksson, Emma (KD)','Henriksson, Stig (V)','Herrstedt, Carina (SD)','Heydari, Shadiye (S)','Hirvonen, Annika (MP)','Hjälmered, Lars (M)','Hoff, Hans (S)','Holm, Christian (M)','Holm, Jens (V)','Holmqvist, Paula (S)','Hult, Emma (MP)','Hultberg, Johan (M)','Håkansson, Per-Arne (S)','Härstedt, Kent (S)','Högman, Berit (S)','Höj Larsen, Christina (V)','Hökmark, Isabella (M)','Jacobsson Gjörtler, Jonas (M)','Jakobsson, Leif (S)','Jakobsson, Stefan (SD)','Jansson, Eva-Lena (S)','Jansson, Mikael (SD)','Jeppsson, Peter (S)','Johansson, Ola (C)','Johansson, Wiwi-Anne (V)','Johnsson Fornarve, Lotta (V)','Johnsson, Per-Ingvar (C)','Johnsson, Peter (S)','Jomshof, Richard (SD)','W Jonsson, Anders (C)','Jonsson, Mattias (S)','Juholt, Håkan (S)','Juntti, Ellen (M)','Jämtin, Carin (S)','Jönsson, Johanna (C)','Kain, Nina (SD)','Kakabaveh, Amineh (V)','Karkiainen, Ida (S)','Karlsson, Annelie (S)','Karlsson, Maj (V)','Karlsson, Mattias (SD)','Karlsson, Niklas (S)','Karlsson, Sara (S)','Karlsson, Ulrika i Uppsala (M)','Kerimo, Yilmaz (S)','Kinberg Batra, Anna (M)','Kinnunen, Martin (SD)','Kjellin, Margareta B (M)','Klackenberg, Dag (M)','Klarberg, Per (SD)','Knutsson, Elisabet (MP)','Kristersson, Ulf (M)','Kronlid, Julia (SD)','Källström, Emil (C)','Köhler, Katarina (S)','Köse, Serkan (S)','Lahti, Birger (V)','Larsson, Hillevi (S)','Larsson, Jan-Olof (S)','Larsson, Lars Mejern (S)','Larsson, Margareta (SD)','Larsson, Rikard (S)','Larsson, Yasmine (S)','Lavesson, Olof (M)','Lillemets, Annika (MP)','Lindahl, Helena (C)','Lindberg, Teres (S)','Linde, Hans (V)','Lindestam, Åsa (S)','Lindholm, Jan (MP)','Lindholm, Veronica (S)','Ling, Rasmus (MP)','Lodenius, Per (C)','Lohman, Eva (M)','Lundgren, Elin (S)','Lundgren, Kerstin (C)','Lundh Sammeli, Fredrik (S)','Lundqvist, Patrik (S)','Lång, David (SD)','Löberg, Petter (S)','Löfstrand, Johan (S)','Lööf, Annie (C)','Magnusson, Cecilia (M)','Malm, Fredrik (FP)','Malmberg, Betty (M)','Malmberg, Niclas (MP)','Malmer Stenergard, Maria (M)','Manhammar, Magnus (S)','Marttinen, Adam (SD)','Millard, Jonas (SD)','Modig, Aron (KD)','Mutt, Valter (MP)','Niemi, Pyry (S)','Nilsson, Ingemar (S)','Nilsson, Jennie (S)','Nilsson, Kerstin (S)','Nilsson, Kristina (S)','Nilsson, Pia (S)','Nilsson, Stefan (MP)','Nissinen, Johan (SD)','Nohrén, Emma (MP)','Nordell, Lars-Axel (KD)','Nordgren, Gunilla (M)','Nordin, Lise (MP)','Nordin, Rickard (C)','Norlén, Andreas (M)','Nylander, Christer (FP)','Nylund Watz, Ingela (S)','Nysmed, Leif (S)','Ohlsson, Birgitta (FP)','Ohlsson, Carina (S)','Olovsson, Fredrik (S)','Olsson, Kalle (S)','Olsson, Lotta (M)','Omanovic, Jasenko (S)','Oscarsson, Magnus (KD)','Oscarsson, Mikael (KD)','Ottoson, Erik (M)','Ottosson, Mattias (S)','Palm, Veronica (S)','Persson, Magnus (SD)','Persson, Mats (FP)','Persson, Peter (S)','Persson, Rickard (MP)','Petersson, Helene i Stockaryd (S)','Petersson, Jenny (M)','Pethrus, Désirée (KD)','Pettersson, Göran (M)','Pettersson, Helén i Umeå (S)','Pettersson, Leif (S)','Pettersson, Marianne (S)','Plass, Maria (M)','Polfjärd, Jessica (M)','Pärssinen, Raimo (S)','Qarlsson, Annika (C)','Quicklund, Saila (M)','Ramhorn, Per (SD)','Rasmusson, Magda (MP)','Redar, Lawen (S)','Reslow, Patrick (M)','Riazat, Daniel (V)','Richtoff, Roger (SD)','Riedl, Edward (M)','Rojhan Gustafsson, Azadeh (S)','Rosencrantz, Jessica (M)','Roswall, Jessika (M)','Rothenberg, Hans (M)','Rågsjö, Karin (V)','Schlyter, Carl (MP)','Schröder, Anders (MP)','Schulte, Fredrik (M)','Sestrajcic, Daniel (V)','Sjöstedt, Jonas (V)','Sjöstedt, Oscar (SD)','Skalberg Karlsson, Jesper (M)','Skalin, Johnny (SD)','Skånberg, Tuve (KD)','Sonidsson, Eva (S)','Staxäng, Lars-Arne (M)','Stenkvist, Robert (SD)','Stockhaus, Maria (M)','Strand, Thomas (S)','Strömkvist, Maria (S)','Ståhl, Jimmy (SD)','Stålhammar, Pernilla (MP)','Sundén Andersson, Lisbeth (M)','Sundin, Cassandra (SD)','Sundin, Mathias (FP)','Svantesson, Elisabeth (M)','Svantorp, Gunilla (S)','Svenneling, Håkan (V)','Svensson Smith, Karin (MP)','Svensson, Michael (M)','Svensson, Suzanne (S)','Sydow Mölleby, Mia (V)','von Sydow, Björn (S)','Szyber, Caroline (KD)','Sällström, Sven-Olof (SD)','Sätherberg, Anna-Caren (S)','Söder, Björn (SD)','Söder, Larry (KD)','Sörenson, Anna-Lena (S)','Tegnér, Mathias (S)','Tenfjord-Toftby, Cecilie (M)','Thalén Finné, Ewa (M)','Thorell, Olle (S)','Tobé, Tomas (M)','Tysklind, Lars (FP)','Töyrä, Emilia (S)','Ullenhag, Erik (FP)','Unander, Hans (S)','Utbult, Roland (KD)','Wallén, Anna (S)','Wallentheim, Anna (S)','Wallmark, Hans (M)','Wallrup, Emma (V)','Waltersson Grönvall, Camilla (M)','Warborn, Jörgen (M)','Weimer, Maria (FP)','Venegas, Marco (MP)','Westerén, Hanna (S)','Westerholm, Barbro (FP)','Vestlund, Börje (S)','Westlund, Åsa (S)','Widegren, Cecilia (M)','Widman, Allan (FP)','Wiechel, Björn (S)','Wiechel, Markus (SD)','Wigh, Hanna (SD)','Wiklander, Tony (SD)','Wykman, Niklas (M)','Völker, Alexandra (S)','Yngwe, Kristina (C)','Zander, Solveig (C)','Åberg, Boriana (M)','Åfeldt, Jennie (SD)','Åkerlund, Jonas (SD)','Åkesson, Anders (C)','Åkesson, Anette (M)','Åkesson, Jimmie (SD)','Åsling, Per (C)','Örnebjär, Christina (FP)','Örnfjäder, Krister (S)','Östberg, Christina (SD)','Öz, Emanuel (S)']
count = 0

# Skriv en for-loop här!


print("Antal sonnare i riksdagen: %s" % count)