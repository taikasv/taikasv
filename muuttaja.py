# Yksinkertainen koodi, joka muuntaa ajanmääreitä yhdestä toiseen käyttäjän toiveiden mukaisesti.
def tunneiksi(paivat):
    tunnit = paivat*24
    return tunnit

def minuuteiksi(tunnit):
    minuutit = tunnit*60
    return minuutit

print("Tervetuloa ajanmääreitä muuntavaan laskuriin! Tämän laskurin avulla voit selvittää kuinka monta minuuttia tietyssä tuntimäärässä tai kuinka monta tuntia tietyssä päivämäärässä on.")

ans = int(input("Anna muunnettava ajanmääre (joko päiviä tai tunteja)"))
tyyppi = input("Onko antamasi määre päiviä vai tunteja (vastaa joko h tai d)")

if tyyppi == "h":
    minuutit = minuuteiksi(ans)
   #minuuteiksi(ans)
    print(f"Minuuttien määrä {minuutit}")

elif tyyppi == "d":
    tunneiksi(ans)
    print(f"Tuntien määrä")

else: 
    print('Virheellinen syöte, vastaa joko "d" tai "h"')

print(ans)