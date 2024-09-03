import flet as ft

def mostrar_nombre(text_field, page):
    
    nombre = text_field.value
    dialog = ft.AlertDialog(
        title=ft.text("Mostrar nombre"),
        content=ft.text(f"Tu nombre es: {nombre}" + " Bienvenido a flet"),
        actions=[
            ft.TextButton("Da clic para salir", on_click=lambda e: close_dialog(page))
        ],
    )
    
    page.dialog = dialog
    page.dialog.open = True
    page.update()
    
def close_dialog(page):
    page.dialog.open = False
    page.update()
    
def main(page: ft.Page):
    page.title=("Mostrar nombre")
    page.bgcolor="Blue"
    text_field = ft.TextField(label="Ingresa tu nombre")
    button = ft.ElevatedButton(
        text = "Di mi nombre",
        on_click=lambda e: mostrar_nombre(text_field, page)
    )
    page.add(
        ft.Row(controls=[
            text_field,
            button
        ])
    )
    
ft.app(target=main)