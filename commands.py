import os
from utils import install_global_commands
import asyncio
from dotenv import load_dotenv

load_dotenv()

TEST_COMMAND = {
  'name': 'test',
  'description': 'Basic command',
  'type': 1,
  'integration_types': [0, 1],
  'contexts': [0, 1, 2],
}


RANDOM_TEAMS_COMMAND = {
  'name': 'crear_equipos',
  'description': 'Crea equipos aleatoriamente',
  'options': [
    {
      'type': 3,
      'name': 'jugadores',
      'description': 'Ingrese los jugadores separados por espacios :D',
      'required': True
    }
  ],
  'type': 1,
  'integration_types': [0, 1],
  'contexts': [0, 1, 2]
}

AVAILABLES_DATES = {
  'name': 'canchas_disponibles_mitre',
  'description': 'Canchas disponibles en mitre ⚽',
  'options': [
    {
      'type': 3,
      'name': 'dia',
      'description': 'Dia en el que queres ver horarios',
      'required': True
    },
    {
      'type': 3,
      'name': 'mes',
      'description': 'Mes en el que queres ver horarios',
      'required': True
    }
  ],
  'type': 1,
  'integration_types': [0, 1],
  'contexts': [0, 1, 2]
}

ALL_COMMANDS = [TEST_COMMAND, RANDOM_TEAMS_COMMAND, AVAILABLES_DATES]

async def main():
    app_id = os.getenv("APP_ID")
    await install_global_commands(app_id, ALL_COMMANDS)

# Ejecutar la función principal
if __name__ == "__main__":
    asyncio.run(main())