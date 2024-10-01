import aiohttp
import os
import json
import asyncio

async def discord_request(endpoint, options):
    url = 'https://discord.com/api/v10/' + endpoint

    if 'body' in options:
        options['body'] = json.dumps(options['body'])

    headers = {
        'Authorization': f'Bot {os.getenv("DISCORD_TOKEN")}',
        'Content-Type': 'application/json; charset=UTF-8',
        'User-Agent': 'DiscordBot (https://github.com/discord/discord-example-app, 1.0.0)'
    }

    async with aiohttp.ClientSession() as session:
        async with session.request(
            method=options.get('method', 'GET'), 
            url=url,
            headers=headers,
            data=options.get('body')
        ) as res:

            if res.status != 200:
                data = await res.json()
                print(res.status)
                raise Exception(json.dumps(data))
            
            return res
        

async def install_global_commands(app_id, commands):
    endpoint = f'applications/{app_id}/commands'

    try:
        await discord_request(endpoint, {'method': 'PUT', 'body': commands})
    except Exception as err:
        print(f"Error: {err}")

