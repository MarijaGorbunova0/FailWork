from os import system
from gtts import *
def loe_failist(fail:str):
    """ Loeme failist read ja salvestame järjendisse. Funktsioon
    tagastab järjend
    :param str faili
    :rtype: list
    """
    f = open(fail, "r", encoding="utf-8")#try
    järjend = []
    for rida in f:
        järjend.append(rida.strip())
    f.close()
    return järjend
def kirjuta_failisse(fail:str, jarjend =[]):
    n = int(input("sisesta mitu elemendid"))
    for i in range (n):
        jarjend.append(input(f"{i+1}.element "))
        f = open(fail, "w", encoding="utf-8")
        for el in jarjend:
            f.write(el+"\n")
        f.close()
def heli(tekst:str, keel:str):
    obj = gTTS(text = tekst, lang = keel, slow = False).save("heli.mp3")
    system("heli.mp3")

tekst = input("Sisesta tekst ")
heli(tekst, "et")

kirjuta_failisse("Text.txt")


paevad  = loe_failist("paevad.txt")
print(paevad)
