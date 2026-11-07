import json

with open("following.json", "r", encoding="utf-8") as file:
    dati_seguiti = json.load(file)

lista_persone_seguite = dati_seguiti["relationships_following"]

nomi_utente_seguiti = set()
for persona in lista_persone_seguite:
    nomi_utente_seguiti.add(persona["title"])

with open("followers_1.json", "r", encoding="utf-8") as file:
    dati_followers = json.load(file)

nomi_utente_followers = set()
for persona in dati_followers:
    nomi_utente_followers.add(persona["string_list_data"][0]["value"])

solo_seguiti_non_follower = nomi_utente_seguiti - nomi_utente_followers
print(f"persone che segui ma che non ti seguono:\n{solo_seguiti_non_follower}")
solo_follower_non_seguiti = nomi_utente_followers - nomi_utente_seguiti
print(f"\npersone che ti seguono ma che non segui:\n{solo_follower_non_seguiti}")
