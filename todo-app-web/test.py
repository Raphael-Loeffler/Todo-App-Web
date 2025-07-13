import os
import json

task_name: str = "asdf"
task_priority: str = "high"

with open('data/task_data.json', 'r') as file:
    data_str: str = file.read()

data_dict: dict = json.loads(data_str)

data_dict['tasks'].update({
    f"{task_name}": {
        "priority": f"{task_priority}"
    }
})

print(data_dict)

for task_name, task_properties in data_dict['tasks'].items():
    print(task_name)
    print(task_properties['priority'])