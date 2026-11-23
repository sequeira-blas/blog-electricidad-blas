from blog.validaciones import validar_post

def listar_posts(lista):
    """Recorre la lista de posts, valida cada uno y formatea la salida."""
    print("\n===== TODOS LOS POSTS =====")
    encontrados = 0
    
    for post in lista:
        es_valido, mensaje = validar_post(post)
        if es_valido:
            encontrados += 1
            print(f"ID: {post.get('id')}")
            print(f"Título: {post.get('titulo')}")
            print(f"Autor: {post.get('autor', {}).get('nombre', 'Desconocido')}")
            print(f"Estado: {post.get('estado')}")
            print(f"Tags: {', '.join(post.get('tags', []))}")
            print("-------------------------")
        else:
            print(f"[ADVERTENCIA] Post ID {post.get('id', 'Desconocido')} omitido por error: {mensaje}")
            
    if encontrados == 0:
        print("No hay posts válidos para mostrar.")


def buscar_por_titulo(lista, termino):
    """Busca posts cuyo título contenga el término ingresado (case-insensitive)."""
    print(f"\n===== BUSCAR POR TÍTULO: '{termino}' =====")
    resultados = []
    
    termino_limpio = termino.strip().lower()
    for post in lista:
        es_valido, _ = validar_post(post)
        if es_valido and termino_limpio in post["titulo"].strip().lower():
            resultados.append(post)
            
    if resultados:
        for post in resultados:
            print(f"Título: {post['titulo']}")
            print(f"Autor: {post['autor']['nombre']}")
            print(f"Estado: {post['estado']}")
            print("-------------------------")
    else:
        print("No se encontraron posts válidos con ese título.")

from blog.validaciones import validar_post


def listar_posts(lista):
    """Recorre la lista de posts, valida cada uno y formatea la salida."""
    print("\n===== TODOS LOS POSTS =====")
    encontrados = 0

    for post in lista:
        es_valido, mensaje = validar_post(post)
        if es_valido:
            encontrados += 1
            print(f"ID: {post.get('id')}")
            print(f"Título: {post.get('titulo')}")
            print(f"Autor: {post.get('autor', {}).get('nombre', 'Desconocido')}")
            print(f"Estado: {post.get('estado')}")
            print(f"Tags: {', '.join(post.get('tags', []))}")
            print("-------------------------")
        else:
            print(f"[ADVERTENCIA] Post ID {post.get('id', 'Desconocido')} omitido por error: {mensaje}")

    if encontrados == 0:
        print("No hay posts válidos para mostrar.")


def buscar_por_titulo(lista, termino):
    """Busca posts cuyo título contenga el término ingresado (case-insensitive)."""
    termino_limpio = termino.strip().lower()
    print(f"\n===== BUSCAR POR TÍTULO: '{termino_limpio}' =====")

    if not termino_limpio:
        print("Debe ingresar un término de búsqueda no vacío.")
        return

    resultados = []
    for post in lista:
        es_valido, _ = validar_post(post)
        if es_valido and termino_limpio in post["titulo"].strip().lower():
            resultados.append(post)

    if resultados:
        for post in resultados:
            print(f"Título: {post['titulo']}")
            print(f"Autor: {post['autor']['nombre']}")
            print(f"Estado: {post['estado']}")
            print("-------------------------")
    else:
        print("No se encontraron posts válidos con ese título.")


def filtrar_por_tag(lista, tag):
    """Filtra y muestra los posts que contienen un tag específico (case-insensitive)."""
    tag_limpio = tag.strip().lower()
    print(f"\n===== FILTRAR POR TAG: '{tag_limpio}' =====")

    if not tag_limpio:
        print("Debe ingresar una etiqueta no vacía.")
        return

    resultados = []
    for post in lista:
        es_valido, _ = validar_post(post)
        if es_valido:
            tags_minusculas = [t.strip().lower() for t in post["tags"]]
            if tag_limpio in tags_minusculas:
                resultados.append(post)

    if resultados:
        for post in resultados:
            print(f"Título: {post['titulo']}")
            print(f"Autor: {post['autor']['nombre']}")
            print(f"Tags: {', '.join(post['tags'])}")
            print("-------------------------")
    else:
        print("No se encontraron posts válidos con esa etiqueta.")


def verificar_todos_los_posts(lista):
    """Función de auditoría para revisar el estado de salud de todos los posts."""
    print("\n===== AUDITORÍA DE POSTS =====")
    for i, post in enumerate(lista):
        es_valido, mensaje = validar_post(post)
        estado_str = "VÁLIDO" if es_valido else f"INVÁLIDO -> {mensaje}"
        print(f"Índice {i} (ID: {post.get('id', 'N/A')}): {estado_str}")