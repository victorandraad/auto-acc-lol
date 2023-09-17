import flask
from tinydb import TinyDB

api = flask.Flask(__name__)
db = TinyDB("instance\db.json", indent=4)

@api.route("/accept/<string:validador>", methods=["POST"])
def getAccept(validador):
    return db.update({'value': f'{validador}'}, doc_ids=[1])

@api.route("/ban/<string:validador>", methods=["POST"])
def getBan(validador):
    return db.update({'value': f'{validador}'}, doc_ids=[2])

@api.route("/rune/<string:validador>", methods=["POST"])
def getRune(validador):
    return db.update({'value': f'{validador}'}, doc_ids=[3])

@api.route("/spells/<string:validador>", methods=["POST"])
def getSpell(validador):
    return db.update({'value': f'{validador}'}, doc_ids=[4])

@api.route("/dodge/<string:validador>", methods=["POST"])
def getDodge(validador):
    return db.update({'value': f'{validador}'}, doc_ids=[5])

@api.route("/matchmaking/<string:validador>", methods=["POST"])
def getMatchmaking(validador):
    return db.update({'value': f'{validador}'}, doc_ids=[6])
