import flet as ft

def main(page: ft.Page):
    page.title = 'p e g g a p e p p a'
    page.window_width = 400
    page.window_height = 400
    page.bgcolor = '#181823'

    pick_button = ft.FilledButton(text='Auto Pick (desativado)', on_click=alterar_pick)
    queue_button = ft.FilledButton(text='Queue Accept (desativado)', on_click=queue_accept)
    
    page.add(pick_button, queue_button)

def alterar_pick(self, page: ft.Page):
    pick_button = ft.FilledButton(text='Auto Pick (Ativado)')
    page.add(pick_button)
def queue_accept(self):
    print

ft.app(target=main)