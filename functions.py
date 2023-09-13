import json
from lcu_driver import Connector
connector = Connector()

async def champselect(connection):
    champSelect = await connection.request('get', 'lol/-champ-select/v1/session')
    if champSelect.status != 200:
        pass
    else: test = json.loads(await champSelect.read())
    print(test)


@connector.ready
async def connect(connection):
    print("It has connected to league")

@connector.close
async def disconnect(connection):
    print("It has disconnected from league")

@connector.ws.register("/lol-champ-select/v1/session", event_types=("UPDATE",))
async def updated(connection, event):
    await champSelect(connection)



@connector.ws.register("/lol-pre-end-of-game/v1/currentSequenceEvent", event_types=("UPDATE",))
async def updated(connection, event):
    print()
    end = await connection.request("get", "/lol-pre-end-of-game/v1/currentSequenceEvent")
    end = json.loads(await end.read())
    print(end)

@connector.ws.register("/lol-matchmaking/search", event_types=("UPDATE",))
async def updated(connection, event):
    print()
    end = await connection.request("get", "/lol-matchmaking/search")
    end = json.loads(await end.read())
    print(end)

@connector.ws.register("/lol-matchmaking/v1/ready-check", event_types=("UPDATE",))
@connector.ws.register("/lol-matchmaking/v1/ready-check/decline", event_types=("CREATE",))
async def decline(connection, event):
    print()
    end = await connection.request("get", "/lol-matchmaking/v1/ready-check")
    end = json.loads(await end.read())
    print(end)
    if end['state'] == "InProgress":
        end = await connection.request("post", "/lol-matchmaking/v1/ready-check/accept")
        end = json.loads(await end.read())
        print(end)



connector.start()