import requests
import json
import math
import numpy as np

def getHorariosDisponibles(dia, mes):
    # Validar entrada
    if not (1 <= mes <= 12):
        raise ValueError("El mes debe estar entre 1 y 12.")
    if not (1 <= dia <= 31): 
        raise ValueError("El día debe estar entre 1 y 31.")

    dia_str = f"{dia:02d}"
    mes_str = f"{mes:02d}"

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
    horarios_disponibles = []
    for horario in json_data["horarios"]:
        hora = [horario["hora_inicio"][0:5], horario["disponibilidad"], horario["horas"][0]["tarifa"]["precio"], horario["horas"][0]["tarifa"]["sena"]]
        horarios_disponibles.append(hora)

    msj = f'Horarios Disponibles para el dia {dia}-{mes}-2024:\n'
    for horario in horarios_disponibles:
        msj += f'Hora: {horario[0]} | Valor: {horario[2]} | Reserva: {horario[3]}\n'
    msj += f'Link para reservar: https://booking.wonasports.com/reservation-calendar/Canchas-Club-Mitre/70222949cc0db89ab32c9969754d4758?fieldType=1&roofType=0&day=2024-{mes}-{dia}'
    return msj

def getRandomTeams(jugadores):
    namesArray = jugadores.split(" ")
    jugadores_por_equipo = math.floor(len(namesArray) / 2)
    equipo1 = []
    equipo1_str = ''

    while(len(equipo1) < jugadores_por_equipo):
        randNum = np.random.randint(0, jugadores_por_equipo +1)
        if(namesArray[randNum] not in equipo1):
            equipo1.append(namesArray[randNum])
            equipo1_str += f' {namesArray[randNum]}'
            if(len(equipo1) < jugadores_por_equipo):
                equipo1_str += ','

    equipo2 = []
    equipo2_str = ''
    for jugador in namesArray:
        if jugador not in equipo1:
            equipo2.append(jugador)
            equipo2_str += f' {jugador}'
            if(len(equipo2) < jugadores_por_equipo):
                equipo2_str += ','

    
    msj = f"Equipo 1:{equipo1_str}. \nEquipo 2:{equipo2_str}."
    return msj

res = getRandomTeams('valen vanik maxi pollo agus mate igna tomi')
print(res)











