from flask import Flask, request
import modules.tasks as tasks
from flask_cors import CORS, cross_origin

ids = tasks.idGenerator()

app = Flask(__name__)
CORS(app)

# {
# 	"payload": {
# 		"name": "Instalación Sr Daniel",
# 		"location": {
# 			"lat": 212.12314,
# 			"long": 100.24223
# 		},
# 		"technician": "Ricardo",
# 		"done": 0
# 	}
# }


@app.route('/tasksList', methods=['GET'])
def sendList():
    taskList = tasks.getList()
    return taskList

@app.route('/newTask', methods=['POST'])
def receiveTask():
    data = request.json
    task = data['payload']
    task['id'] = next(ids)
    try:
        tasks.newTask(task)
        return {"success": 201, "status": "Task created"}
    except ValueError as error:
        return {"success": 400, "error": error.args[0]}
    return task

@app.route('/rmTask', methods=['DELETE'])
def deleteTask():
    data = request.json
    if (tasks.rmTask(int(data['id']))):
        return {"success": 204, "status": "Task deleted"}
    else:
        return {"success": 404, "status": "Task not found"}

if __name__ == '__main__':
    app.run()