def mostrar_menu():
    """Muestra el menú principal y retorna la opción ingresada por el usuario."""
    print("\n===== MENÚ DEL BLOG =====")
    print("1 - Ver todos los posts válidos")
    print("2 - Buscar por título")
    print("3 - Filtrar por tag")
    print("4 - Validar integridad de los posts")
    print("5 - Salir")
    return input("Seleccione una opción: ").strip()

def solicitar_termino_busqueda():
    """Solicita al usuario una palabra o parte del título."""
    return input("Ingrese una palabra o parte del título: ")


def solicitar_tag_busqueda():
    """Solicita al usuario una etiqueta para filtrar posts."""
    return input("Ingrese la etiqueta que desea buscar: ")