from fastapi import FastAPI, Request, HTTPException
import os
import json
from discord_interactions import verify_key_decorator, InteractionType, InteractionResponseType
import uvicorn
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from funciones import getHorariosDisponibles, getRandomTeams
from dotenv import load_dotenv

load_dotenv()

PUBLIC_KEY = os.getenv("PUBLIC_KEY")

app = FastAPI()

@app.get("/")
async def root2():
    return {"message": "Hello World"}


@app.post("/interactions")

async def root(req: Request):
    verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))

    signature = req.headers["X-Signature-Ed25519"]
    timestamp = req.headers["X-Signature-Timestamp"]
    body = await req.body()
    body_str = body.decode("utf-8")

    try:
        verify_key.verify(f'{timestamp}{body_str}'.encode(), bytes.fromhex(signature))
    except BadSignatureError:
        raise HTTPException(status_code=401, detail="Invalid request signature")


    body = await req.json()

    type = body["type"]
    if (type == 1):
        return {"type": 1}
    
    if (type == InteractionType.APPLICATION_COMMAND):
        name = body["data"]["name"]

        if(name == 'test'):
            return {
                "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
                "data": {
                "content": "hello world :D"
                }
            }
        
        if(name == 'canchas_disponibles_mitre'):
            dia = int(body["data"]["options"][0]["value"])
            mes = int(body["data"]["options"][1]["value"])

            return {
                "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
                "data": {
                    "content": getHorariosDisponibles(dia,mes)
                }
            }
        
        if(name == 'crear_equipos'):
            jugadores = body["data"]["options"][0]["value"]
            return {
                "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
                "data": {
                    "content": getRandomTeams(jugadores)
                }
            }
        
        raise HTTPException(status_code=400, detail=f"unknown command: {name}")
    
if __name__ == "__main__":
    PORT = 3000
    print(f"Listening on port {PORT}")
    uvicorn.run("app:app", host="0.0.0.0", port=PORT, reload=True)