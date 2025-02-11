from .fb_db import db

def obtener_usuarios():
    """Obtiene todos los usuarios de la colección 'usuarios' en Firestore."""
    docs = db.collection("usuarios").get()
    return {doc.id: doc.to_dict() for doc in docs}

def agregar_usuario(user_id, data):
    """Agrega o actualiza un usuario en la base de datos."""
    db.collection("usuarios").document(user_id).set(data)
    return f"Usuario {user_id} agregado correctamente"

# Ejemplo de prueba (descomentar para probar)
print(agregar_usuario("test_user", {"nombre": "Isaac", "saldo": 1000}))
print(obtener_usuarios())
