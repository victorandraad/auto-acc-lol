from tinydb import TinyDB

db = TinyDB("app\models\db.json", indent=4)

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
    'value': 54
})

db.insert({
    # champion2
    'value': 43
})

db.insert({
    # champion3
    'value': 23
})

db.insert({
    # banChampion1
    'value': 123
})

db.insert({
    # banChampion2
    'value': 435
})

db.insert({
    # banChampion3
    'value': 123
})