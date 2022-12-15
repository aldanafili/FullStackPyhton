from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://root:root@cluster0.h2okbaa.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_productos_app"]
    except ConnectionError:
        print('Error de conexion con la bdd')
    return db            