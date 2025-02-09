import argparse
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://userweb:567234@clustervel.dx48a.mongodb.net/?retryWrites=true&w=majority&appName=ClusterVel"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client.cats_web

parser = argparse.ArgumentParser(description='Server Cats')
parser.add_argument('--action', help=" update_age, update_feature, read, read_all, delete_by_name, delete_all")
parser.add_argument('--id')
parser.add_argument('--name')
parser.add_argument('--age')
parser.add_argument('--features', nargs='+')

arg = vars(parser.parse_args())

action = arg.get('action')
pk = arg.get('id')
name = arg.get('name')
age = arg.get('age')
features = arg.get('features')


def find_all():
    return db.cats.find()


def find(name):
    cat = db.cats.find_one({"name": name})
    return cat if cat else "There is no cat found."


def update_age(name, age):
    result = db.cats.update_one({"name": name}, {
        "$set": {
            "age": age
        }
    })
    return result


def update_feature(name, feature):
    result = db.cats.update_one({"name": name}, {
        "$push": {
            "feature": feature
        }
    })
    return result


def delete_by_name(name):
    return db.cats.delete_one({"name": name})

def delete_all():
    return db.cats.delete_many({})

def main():
    match action:
        case 'read_all':
            r = find_all()
            print([e for e in r])
        case 'read':
            r = find(name)
            print(r)
        case 'update_age':
            r = update_age(name, age)
            print(r)
        case 'update_feature':
            r = update_feature(name, features)
            print(r)
        case 'delete_by_name':
            r = delete_by_name(name)
            print(r)
        case 'delete_all':
            r = delete_all()
            print(r)
        case _:
            print('Unknown command')


if __name__ == '__main__':
    main()
