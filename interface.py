import time
import flet as ft
import functions
from datetime import datetime

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
    page.padding = 0
    page.window_resizable = False
    page.window_maximizable = False
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "#1E272E"
    ft.Icon()
    

    def accept(e):
        pass

    def ban(e):
        pass
    
    def rune(e):
        pass

    def spells(e):
        pass

    def dodge(e):
        pass

    def matchmaking(e):
        pass

    acceptbtn = Botao_feature.criar("AutoAceitar", accept)
    autorunebtn = Botao_feature.criar("AutoRuna", rune)
    autospellsbtn = Botao_feature.criar("AutoSpells", spells)
    autobanbtn = Botao_feature.criar("AutoBan", ban)
    autododgebtn = Botao_feature.criar("AutoDodge", dodge)
    automatchmakingbtn = Botao_feature.criar("AutoMatchMaking", matchmaking)


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


if __name__ == "__main__":
    ft.app(target=main)
