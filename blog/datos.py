# ==========================================
# DEFINICIÓN DE DATOS Y CONSTANTES
# ==========================================

perfil_autor = {
    "nombre": "Blas Sequeira",
    "bio": "Electricista automotor",
    "especialidad": "Burros de arranque y Alternadores",
    "redes_sociales": ["@blas_seq", "@blas_94"]
}

estados_post = ("borrador", "publicado", "archivado")

etiquetas_blog = {"Burros de arranque", "Alternadores", "Bateria", "Lamparas"}

posts = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Burros de arranque",
        "contenido": "Desarme y partes de Burros de arranque",
        "autor": perfil_autor,
        "tags": ["Burros de arranque", "Principiantes"],
        "estado": "publicado",
    },
    {
        "id": 2,
        "titulo": "Qué es un Alternador",
        "contenido": "Desarme y partes de alternador",
        "autor": perfil_autor,
        "tags": ["Burros de arranque", "Alternador", "Bateria"],
        "estado": "borrador",
    },
    {
        "id": 3,
        "titulo": "Organizando valores de carga Bateria",
        "contenido": "Revision de carga de bateria",
        "autor": perfil_autor,
        "tags": ["Burros de arranque", "Bateria"],
        "estado": "archivado",
    },
    {
        # Post con datos incompletos/erróneos para probar validaciones
        "id": 4,
        "titulo": "",  # Título vacío deliberado
        "contenido": "Prueba de error en validación",
        "autor": "Blas Sequeira",  # Error: debería ser un diccionario
        "tags": [],
        "estado": "invalido",  # Estado no permitido
    }
]