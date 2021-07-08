import urllib.parse
import requests


def sorgula():

        main_api="https://api.collectapi.com/health/dutyPharmacy?"    
        url = main_api + urllib.parse.urlencode({"ilce":ilce, "il":il})
        headers = {
            'content-type': "application/json",
            'authorization': "apikey 6lAwcrDHJBhFNmTr3Fc51d:0YoE6c6Bk9MPQo3a0ihbBV"
            }
        return  requests.post(url,headers=headers).json()

while True:
    il = input("İli Girin: ")
    if il == "çıkış" or il == "çık" or il == "ç":
        break
    ilce = input("İlçeyi griniz: ")
    if ilce == "çıkış" or ilce == "çık" or ilce == "ç":
        break        
    gelen=sorgula()

    for each in gelen["result"]:
        print (each["name"]+" - "+ each["address"])
        print("https://maps.google.com/maps?q="+each["loc"]+"&hl=es&z=14")

