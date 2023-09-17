from lcu_driver import Connector
from tinydb import TinyDB

connector = Connector()

db = TinyDB("instance\db.json")

@connector.ready
async def connect(connection):
    summoner = await connection.request("get", "/lol-summoner/v1/current-summoner")

@connector.ws.register("/lol-matchmaking/v1/ready-check", event_types=("UPDATE", "CREATE"))
async def accept(connection, event):
    if db.get(doc_ids=[1])[0]['value'] == "True":
        return await connection.request("POST", "/lol-matchmaking/v1/ready-check/accept")

# @connector.ws.register("")
