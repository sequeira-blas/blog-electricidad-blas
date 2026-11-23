from blog.datos import estados_post


def validar_post(post):
    """
    Verifica las reglas de negocio de un post.
    Retorna una tupla (es_valido, mensaje_error).
    """
    campos_requeridos = ["id", "titulo", "contenido", "autor", "tags", "estado"]

    if not isinstance(post, dict):
        return False, "El post debe ser un diccionario."

    for campo in campos_requeridos:
        if campo not in post:
            return False, f"Falta la clave obligatoria: '{campo}'"

    if not isinstance(post["titulo"], str) or not post["titulo"].strip():
        return False, "El título no puede estar vacío."

    if not isinstance(post["contenido"], str) or not post["contenido"].strip():
        return False, "El contenido no puede estar vacío."

    if not isinstance(post["autor"], dict) or "nombre" not in post["autor"]:
        return False, "El autor debe ser un diccionario con al menos la clave 'nombre'."

    if not isinstance(post["tags"], list):
        return False, "El campo 'tags' debe ser una lista."

    if post["estado"] not in estados_post:
        return False, f"El estado '{post['estado']}' no es válido. Opciones: {estados_post}"

    return True, "Post válido"