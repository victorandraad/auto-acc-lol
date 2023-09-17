import flet as ft
import concurrent.futures
from app import target




if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        interface = executor.submit(ft.app, target=target)