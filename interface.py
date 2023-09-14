import time
import flet as ft
from datetime import datetime

class Botao_feature(ft.UserControl):
    def criar(name, position=None):

        match position:
            case "Left":
                position = ft.LabelPosition.LEFT
            case "Right":
                position = ft.LabelPosition.RIGHT

        btn = ft.Checkbox(
        check_color="#0BE881",
        fill_color={ft.MaterialState.SELECTED: "#0BE881", ft.MaterialState.DEFAULT: "#485460"},
        width=124,
        height=39,
        label=name,
        label_position=position,
        )
        return btn

def main(page: ft.Page):

    page.title = "LCULeagueTools"
    page.fonts = {
        "Jomhuria": "assets\font\Jomhuria-Regular.ttf"
    }
    page.window_width = 500
    page.window_height = 430
    page.window_resizable = False
    page.window_maximizable = False
    page.bgcolor = "#1E272E"
    
    acceptbtn = Botao_feature.criar("AutoAceitar")  
    autorunebtn = Botao_feature.criar("AutoRuna")
    autospellsbtn = Botao_feature.criar("AutoSpells")
    
    autobanbtn = Botao_feature.criar("AutoBan", "Left")
    autododgebtn = Botao_feature.criar("AutoDodge", "Left")
    automatchmakingbtn = Botao_feature.criar("AutoMatchMaking", "Left")

    page.add(
        ft.Row(alignment=ft.MainAxisAlignment.END, width=400, height=400,
            controls=[
                ft.Column(
                    [
                        acceptbtn,
                        autorunebtn,
                        autospellsbtn,
                    ]
                ),
            
                ft.Column(
                    [
                        ft.Image(src="https://th.bing.com/th/id/R.1395d1b17397018e6916784c283a14f2?rik=bmfmSW7odc2D1A&pid=ImgRaw&r=0",width=114, height=100),
                        ft.Text(width=139, height=30, text_align=ft.TextAlign.CENTER, color="white", size=20, font_family="Jomhuria", value="Nickname"),
                        ft.Text("Level", width=139, height=30, text_align=ft.TextAlign.CENTER, color="0xFFFF0000", size=20, font_family="Jomhuria")
                    ]
                ),

                ft.Column(
                    controls=[
                        autobanbtn, 
                        autododgebtn, 
                        automatchmakingbtn
                    ],
                )
            ],
            
        )
    )

    # page.add(
    #     ft.Row(
    #         controls=[
    #             ft.Image(
    #                 width = 80.16,
    #                 height = 82.37,
    #                 src="https://th.bing.com/th/id/OIP.KeRduNXcbnI6lIpUsQzq3gHaFj?pid=ImgDet&rs=1"
    #             ),
    #             ft.Column(
    #                 [
    #                     ft.Text("Você geralmente ganha jogando com: "),
    #                     ft.Container(width=276, height=39),
    #                     ft.Text("Você geralmente perde jogando contra: "),
    #                     ft.Container(width=276, height=39) 
    #                 ]
    #             ),
    #             ft.Image(
    #                 width = 80.16,
    #                 height = 82.37,
    #                 src="https://th.bing.com/th/id/OIP.KeRduNXcbnI6lIpUsQzq3gHaFj?pid=ImgDet&rs=1"
    #             ),
    #         ]
    #     )
    # )

if __name__ == "__main__":
    ft.app(target=main)
