from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://userweb:567234@clustervel.dx48a.mongodb.net/?retryWrites=true&w=majority&appName=ClusterVel"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client.cats_web

try:
    db.cats.insert_many([
        {
            'name': 'Lama',
            'age': 2,
            'features': ['ходить в лоток', 'не дає себе гладити', 'сірий'],
        },
        {
            'name': 'Liza',
            'age': 4,
            'features': ['ходить в лоток', 'дає себе гладити', 'білий'],
        },
        {
            'name': 'Boris',
            'age': 12,
            'features': ['ходить в лоток', 'не дає себе гладити', 'сірий'],
        },
        {
            'name': 'Murzik',
            'age': 1,
            'features': ['ходить в лоток', 'дає себе гладити', 'чорний'],
        },
    ])
except Exception as e:
    print(e)
