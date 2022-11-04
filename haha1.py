import random
import json

FILE_PATH = '/home/hello/evening25/hahaton/haha.json'
ID_FILEPATH ='/home/hello/evening25/hahaton/id.txt'


def get_data():
    with open(FILE_PATH) as file:
            return json.load(file)

def save_data(data):
    with open(FILE_PATH, 'w') as file:
        json.dump(data,file)

# CRUD
def list_of_products():
    data = get_data()
    return f'список всех товаров: {data}'

def detail_product():
    data = get_data()
    try:
        id = int(input('enter id of product'))
        product = list(filter(lambda x: id == x ['id'], data))
        return product[0]
    except:
        return 'wrong id!'
    


def get_id():
    with open(ID_FILEPATH, 'r') as file:
        id = int(file.read())
        id +=1
    with open(ID_FILEPATH,'w') as file:
        file.write(str(id))
    return id

def craete_product():
    data = get_data()
    try:
        product = {
            'id': get_id(),
            'marka': input('Vvedite marku noutbuka: '),
            'model': input('Vvedite model noutbuka: '),
            'vipusk': int(input('Vvedite god vipuska: ')),
            'opisanie': input('Dobavte opisanie: '),
            'price': round(float(input('Price: ')), 2)

        }
    except Exception as e:
        print(e)
        return 'неверные данные'
    data.append(product)
    save_data(data)
    return 'создан новый товар'

def update_product():
    data = get_data()
    try:
        id = int(input('enter the id of product'))
        product = list(filter(lambda x : x['id'] == id, data))[0]
        print(f'товар для обновления {product["title"]} ')
    except:
        return 'wrong id!'


    index = data.index(product)
    choise = input('what do y wanna change?(1 - title),(2- price),(3 description)')
    if choise.lower().strip() == '1':
        data[index]['title'] = input('enter the new name')
    elif choise.strip() == '2':
        try:
            data[index]['price'] = float(input('enter the new ptice'))
        except:
            return 'wrong price'
    elif choise.strip() == '3':
        data[index]['description'] = input('enter new description')
    else:
        return 'wrong! znachenie for update'

    save_data(data)
    return 'staff secsasfully updated'


def delete_product():
    data = get_data()
    try:
        id = int(input('enter the id of product'))
        product = list(filter(lambda x: x ['id'] == id, data))[0]
        print(f' stagg for deelete {product["title"]}')
    except:
        return ' wrong id'
    choise = input('are y sure? yes/no?')
    if choise.lower().strip() != 'yes':
        return 'i get y its okay'
    data.remove(product)
    save_data(data)
    return'deleted'


