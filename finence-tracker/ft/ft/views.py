from django.http import JsonResponse
from ft.utils.fb_db import obtener_usuarios, agregar_usuario

def listar_usuarios(request):
    """Retorna todos los usuarios almacenados en Firestore."""
    usuarios = obtener_usuarios()
    return JsonResponse({"mensaje": "Usuarios obtenidos correctamente"})

def crear_usuario(request):
    """Crea un nuevo usuario en Firestore."""
    data = {"nombre": "Nuevo Usuario", "saldo": 500}
    mensaje = agregar_usuario("nuevo_user", data)
    return JsonResponse({"mensaje": mensaje})
