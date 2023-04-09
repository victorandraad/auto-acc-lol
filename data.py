import requests

def get_champs():
    # specify the URL of the JSON to be requested
    versionJSON = 'https://ddragon.leagueoflegends.com/api/versions.json'

    # send an HTTP request to the URL and get the response
    version  = requests.get(versionJSON)
    dataVersion = version.json()

    #get champs
    champsJSON = f'http://ddragon.leagueoflegends.com/cdn/{dataVersion[0]}/data/en_US/champion.json'
    champs = requests.get(champsJSON)
    dataChamps = champs.json()
    
    #champ list
    champList = []
    for champ in dataChamps['data']:
        champList.append(champ)
    
    return champList, dataVersion[0]

def get_image():
    champs, version = get_champs()
    imageList = []
    for champ in champs:
        imageList.append(f'http://ddragon.leagueoflegends.com/cdn/{version}/img/champion/{champ}.png')
    return imageList