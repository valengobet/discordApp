import requests
import json


def request_api_futbol(dia_str, mes_str):

    api_url = 'https://core-booking.wonasports.com/api/complejo/70222949cc0db89ab32c9969754d4758/availableDates'

    payload = {
        "filtros": {
            "deporte": 1,      
            "techada": 0       
        },
        "fecha": f"2024-{mes_str}-{dia_str}"  
    }

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'Origin': 'https://booking.wonasports.com',
        'Referer': 'https://booking.wonasports.com/',
        'Accept-Encoding': 'gzip, deflate, br, zstd', 
        'Accept-Language': 'en-US,en;q=0.9,es-AR;q=0.8,es-ES;q=0.7,es;q=0.6',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    }

    response = requests.post(api_url, json=payload, headers=headers)

    data_str = response.content.decode('utf-8')


    json_data = json.loads(data_str)
    
    return json_data