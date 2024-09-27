import aiohttp
import os
import json
import asyncio

async def discord_request(endpoint, options):
    # Define la URL base de la API de Discord
    url = 'https://discord.com/api/v10/' + endpoint

    # Si el cuerpo de la solicitud está presente, lo convierte a JSON
    if 'body' in options:
        options['body'] = json.dumps(options['body'])

    # Agregar encabezados obligatorios para la solicitud
    headers = {
        'Authorization': f'Bot {os.getenv("DISCORD_TOKEN")}',
        'Content-Type': 'application/json; charset=UTF-8',
        'User-Agent': 'DiscordBot (https://github.com/discord/discord-example-app, 1.0.0)'
    }

    # Realiza la solicitud asíncrona
    async with aiohttp.ClientSession() as session:
        async with session.request(
            method=options.get('method', 'GET'), 
            url=url,
            headers=headers,
            data=options.get('body')
        ) as res:

            # Si la respuesta no es exitosa, lanza un error
            if res.status != 200:
                data = await res.json()
                print(res.status)
                raise Exception(json.dumps(data))

            # Retorna la respuesta completa
            return res
        

async def install_global_commands(app_id, commands):
    # Endpoint para sobrescribir comandos globales
    endpoint = f'applications/{app_id}/commands'

    try:
        # Esta llamada usa el método PUT para sobrescribir en masa los comandos globales
        await discord_request(endpoint, {'method': 'PUT', 'body': commands})
    except Exception as err:
        print(f"Error: {err}")

