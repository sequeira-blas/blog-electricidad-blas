from blog.datos import posts
from blog.menu import mostrar_menu, solicitar_tag_busqueda, solicitar_termino_busqueda
from blog.operaciones import (
    buscar_por_titulo,
    filtrar_por_tag,
    listar_posts,
    verificar_todos_los_posts,
)


def ejecutar_programa():
    """Bucle principal de coordinación del sistema."""
    while True:
        try:
            opcion = mostrar_menu()

            if opcion == "1":
                listar_posts(posts)
            elif opcion == "2":
                termino = solicitar_termino_busqueda()
                buscar_por_titulo(posts, termino)
            elif opcion == "3":
                tag = solicitar_tag_busqueda()
                filtrar_por_tag(posts, tag)
            elif opcion == "4":
                verificar_todos_los_posts(posts)
            elif opcion == "5":
                print("\nGracias por utilizar el programa. ¡Hasta pronto!")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")

        except Exception as e:
            print(f"\n[ERROR INESPERADO]: Ocurrió un error en el sistema: {e}")


if __name__ == "__main__":
    ejecutar_programa()