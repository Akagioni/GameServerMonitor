import time
from typing import TYPE_CHECKING

import aiohttp

if TYPE_CHECKING:
    from discordgsm.gamedig import GamedigResult


class Terraria:
    def __init__(self, address: str, query_port: int, token: str):
        self.address = address
        self.query_port = query_port
        self.token = token

    async def query(self):
        url = f'http://{self.address}:{self.query_port}/v2/server/status?players=true&rules=false&token={self.token}'
        start = time.time()

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                end = time.time()

        result: GamedigResult = {
            'name': data['name'],
            'map': data['world'],
            'password': data['serverpassword'],
            'maxplayers': data['maxplayers'],
            'players': [{'name': player['nickname'], 'raw': player} for player in data['players']],
            'bots': [],
            'connect': f"{self.address}:{data['port']}",
            'ping': int((end - start) * 1000),
            'raw': {}
        }

        return result
