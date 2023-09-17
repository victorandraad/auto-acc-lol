import flet as ft
import requests
import threading
from tinydb import TinyDB
from app.controllers.internalApi import api
from app.controllers.functions import connector


class Botao_feature(ft.UserControl):
    def criar(name, func=None):
        btn = ft.Checkbox(
        check_color="#0BE881",
        fill_color={ft.MaterialState.SELECTED: "#0BE881", ft.MaterialState.DEFAULT: "#485460"},
        width=124,
        height=39,
        label=name,
        value=False,
        on_change=func
        )
        return btn



def main(page: ft.Page):

    page.title = "LCULeagueTools"
    page.fonts = {
        "Jomhuria": "assets\font\Jomhuria-Regular.ttf"
    }
    page.window_width = 469
    page.window_height = 403
    page.padding = 10
    page.window_resizable = False
    page.window_maximizable = False
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "#1E272E"

    
    db = TinyDB("instance\db.json", indent=4)
    localhost = "http://localhost:5000/"
     
    for c in range(1, 7):
        db.update({"value": "False"}, doc_ids=[c])
        

    def aceitar(e):
        value = acceptbtn.value
        return requests.post((localhost + f"accept/{value}"))
        
    def banir(e):
        value = autobanbtn.value
        return requests.post((localhost + f"ban/{value}"))
    
    def rune(e):
        value = autorunebtn.value
        return requests.post((localhost + f"rune/{value}"))
    
    def spells(e):
        value = autospellsbtn.value
        return requests.post((localhost + f"spells/{value}"))

    def dodge(e):
        value = autododgebtn.value
        return requests.post((localhost + f"dodge/{value}"))
    
    def matchmaking(e):
        value = automatchmakingbtn.value
        return requests.post((localhost + f"matchmaking/{value}"))


    acceptbtn = Botao_feature.criar("AutoAceitar", aceitar)
    autorunebtn = Botao_feature.criar("AutoRuna", rune)
    autospellsbtn = Botao_feature.criar("AutoSpells", spells)
    autobanbtn = Botao_feature.criar("AutoBan", banir)
    autododgebtn = Botao_feature.criar("AutoDodge", dodge)
    automatchmakingbtn = Botao_feature.criar("AutoMatchMaking", matchmaking)

    threading.Thread(target=api.run).start()
    threading.Thread(target=connector.start).start()
    


    page.add(
        ft.Row(
            controls=[
                ft.Column(
                    [
                        acceptbtn,
                        autorunebtn,
                        autospellsbtn,
                        autobanbtn, 
                        autododgebtn, 
                        automatchmakingbtn
                    ]
                ),
            ],  
        )
    )
