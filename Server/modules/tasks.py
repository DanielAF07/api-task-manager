import json

model = ['id', 'name', 'location', 'technician', 'done']

def idGenerator(offset = 0):
    try:
        db = json.load(open('tasks.json'))
        if db['tasks']:
            id = int(db['tasks'][len(db['tasks'])-1]['id'])
        else:
            id = 0
    except:
        id = 0
    while True:
        id += 1
        yield id

def newTask(task):
    try:
        db = json.load(open('tasks.json'))
    except:
        db = {"tasks": []}
    missingParams = []
    for param in model:
        if param not in task:
            missingParams.append(param)
    if missingParams:
        raise ValueError(f'Missing Params: {", ".join(missingParams)}')
    db["tasks"].append(task)
    with open('tasks.json', 'w+') as f:
        json.dump(db, f)

def getList():
    db = json.load(open('tasks.json'))
    return { "success": 200, "payload": {"tasks":db["tasks"]}}

def rmTask(id):
    db = json.load(open('tasks.json'))
    for index, task in enumerate(db['tasks']):
        if task['id'] == id:
            db['tasks'].pop(index)
            with open('tasks.json', 'w+') as f:
                json.dump(db, f)
            return True
    return False
            