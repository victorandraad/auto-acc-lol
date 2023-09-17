import flet as ft
import requests
from tinydb import TinyDB

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

    db = TinyDB("app\models\db.json", indent=4)
    localhost = "http://localhost:5000/"

    for c in range(1, 6):
        db.update({"value": "False"}, doc_ids=[c])

    def aceitar(e):
        value = acceptbtn.value
        requests.post((localhost + f"accept/{value}"))


    acceptbtn = Botao_feature.criar("AutoAceitar", aceitar)
    autorunebtn = Botao_feature.criar("AutoRuna")
    autospellsbtn = Botao_feature.criar("AutoSpells")
    autobanbtn = Botao_feature.criar("AutoBan")
    autododgebtn = Botao_feature.criar("AutoDodge")
    automatchmakingbtn = Botao_feature.criar("AutoMatchMaking")


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
