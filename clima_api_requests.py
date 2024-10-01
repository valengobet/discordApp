import requests
from dotenv import load_dotenv
import os

load_dotenv()

KEY = os.getenv("CLIMA_API_KEY")

def req_clima_dia(dia, mes):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={KEY}&q=-34.61315,-58.37723&days=7&aqi=no&alerts=no&lang=es"
    clima_dias = requests.get(url).json()["forecast"]["forecastday"]
    dia_str = f"{dia:02d}"
    mes_str = f"{mes:02d}"
    for dia in clima_dias:
        if(dia["date"] == f"2024-{mes_str}-{dia_str}"):
            return dia
    
        

def req_clima_hora(request, cancha, dia, mes):
    if(cancha[3:] == "30"):
        if(cancha[0:1] == "0" and int(cancha[1:2]) < 9):
            cancha = "0" + str(int(cancha[1:2]) + 1) + ":00"
        else:
            cancha = str(int(cancha[0:2]) + 1) + ":00"
    dia_str = f"{dia:02d}"
    mes_str = f"{mes:02d}"
    for hora in request:
        if(hora["time"] == f"2024-{mes_str}-{dia_str} {cancha}"):
                return hora

