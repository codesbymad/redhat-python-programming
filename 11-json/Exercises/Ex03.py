import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")

if response.status_code != 200:
    print(f"ERRO: Código de status retornou {response.status_code}")
    exit(1)

taskList = response.json()

completo = []
incompleto = []

for task in taskList:
    if task["completed"]:
        completo.append(task)
    else:
        incompleto.append(task)

print(f"{len(completo)} de {len(taskList)} tarefas estão completas")

with open("11-json/Exercises/tasks_done.json", "w", encoding="utf-8") as done:
    json.dump(completo, done, separators=(",", ":"))

with open("11-json/Exercises/tasks_todo.json", "w", encoding="utf-8") as todo:
    json.dump(incompleto, todo, separators=(",", ":"))