from futbol_api_requests import request_api_futbol
from clima_api_requests import req_clima_dia, req_clima_hora
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

    json_data = request_api_futbol(dia_str, mes_str)

    horarios_disponibles = []
    for horario in json_data["horarios"]:
        hora = [horario["hora_inicio"][0:5], horario["disponibilidad"], horario["horas"][0]["tarifa"]["precio"], horario["horas"][0]["tarifa"]["sena"]]
        horarios_disponibles.append(hora)

    clima = req_clima_dia(dia, mes)["hour"]
    msj = f'Horarios Disponibles para el dia {dia}-{mes}-2024:\n'
    for horario in horarios_disponibles:
        lluvia = ''
        clima_hora = req_clima_hora(clima, horario[0], dia, mes)
        if(clima_hora["will_it_rain"] == 1):
            lluvia = ", Ojo! puede llover"
        msj += f'Hora: {horario[0]} | Valor: {horario[2]} | Reserva: {horario[3]} | Clima: {clima_hora["temp_c"]}{lluvia}\n'
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

def clima_fecha(dia, mes):
    response = req_clima_dia(dia, mes)["day"]
    msj = f""" 
📍 Ciudad Autonoma de Buenos Aires, CABA -  📅  {dia}-{mes}-2024
        🌡️  Temperatura  | Condicion: {response["condition"]["text"]}
        🔵 Minima: {response["mintemp_c"]}°C | 🌧️ Probabilidad de lluvia: {response["daily_chance_of_rain"]}
        🟠 Media: {response["avgtemp_c"]}°C  | 💧 Humedad: {response["avghumidity"]}
        🔴 Maxima: {response["maxtemp_c"]}°C | 🌪️ Viento: {response["maxwind_kph"]}

"""

    return msj











