import requests, folium, webbrowser

ip = input("Enter an IP address: ")  #zadanie ip adresy

url = f"http://ip-api.com/json/{ip}" #API URL pre geolokaciu zadanej IP adresy
response = requests.get(url)         #Vykonanie GET požiadavky na API
data = response.json()               #Spracovanie JSON odpovede  

m = folium.Map(location=[data["lat"], data["lon"]], zoom_start=10)     #Vytvorenie mapy s centrom na zadaných súradniciach
folium.Marker([data["lat"], data["lon"]], popup="Location").add_to(m)  #Pridanie značky na mapu s popisom

m.save("map.html")                  #Uloženie mapy do HTML súboru
webbrowser.open("map.html")         #Otvorenie mapy v predvolenom webovom prehliadači
