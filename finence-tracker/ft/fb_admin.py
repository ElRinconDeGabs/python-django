import firebase_admin
from firebase_admin import credentials, firestore

# Cargar las credenciales (ajusta la ruta según sea necesario)
cred = credentials.Certificate("fb_admin.json")

# Inicializar Firebase
firebase_admin.initialize_app(cred)

# Obtener referencia a Firestore
db = firestore.client()
