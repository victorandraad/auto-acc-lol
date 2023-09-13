import time

import flet as ft
from datetime import datetime


def main(page: ft.Page):

    page.title = "LCULeagueTools"
    page.fonts = {
        "Jomhuria": "https://fonts.googleapis.com/css?family=Jomhuria"
    }
    page.window_width = 468
    page.window_height = 403
    page.bgcolor = "#1E272E"

    acceptbtn = ft.Checkbox(check_color="#0BE881", fill_color="#485460", width=124, height=39, label="AutoAccept")
    autorunebtn = ft.Checkbox(check_color="#0BE881", fill_color="#485460", width=124, height=39, label="AutoRuna")
    autospellsbtn = ft.Checkbox(check_color="#0BE881", fill_color="#485460", width=124, height=39, label="AutoSpells")
    autobanbtn = ft.Checkbox(check_color="#0BE881", fill_color="#485460", width=124, height=39, label="AutoBan")
    autododgebtn = ft.Checkbox(check_color="#0BE881", fill_color="#485460", width=124, height=39, label="AutoDodge")
    automatchmakingbtn = ft.Checkbox(check_color="#0BE881", fill_color="#485460", width=124, height=39, label="AutoMatchMaking")
    page.add(
        ft.Row(
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
                        autobanbtn,
                        autododgebtn,
                        automatchmakingbtn,
                    ]
                )
            ]
        )
    )

    pass


if __name__ =="__main__":
    ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)