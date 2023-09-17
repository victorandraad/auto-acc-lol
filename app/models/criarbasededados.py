from tinydb import TinyDB

db = TinyDB("instance\db.json", indent=4)

db.insert({
    # autoaccept
    'value': False
})

db.insert({
    # autoban
    'value': False
})

db.insert({
    # autoruna
    'value': False
})

db.insert({
    # autospells
    'value': False
})

db.insert({
    # autododge
    'value': False
})

db.insert({
    # automatchmaking
    'value': False
})

db.insert({
    # champion1
    'champion1': 54
})

db.insert({
    # champion2
    'champion2': 43
})

db.insert({
    # champion3
    'champion3': 23
})

db.insert({
    # banChampion1
    'banChampion1': 123
})

db.insert({
    # banChampion2
    'banChampion2': 435
})

db.insert({
    # banChampion3
    'banChampion3': 123
})