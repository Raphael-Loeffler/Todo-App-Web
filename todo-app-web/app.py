from flask import Flask, request, render_template

import json
import os

def run():
    data_path = 'data/task_data.json'
    initial_content = {"tasks": {}}
    if not os.path.exists(data_path):
        with open(data_path, 'w') as file:
                json.dump(initial_content, file, indent=4)
    
    app = Flask('/')

    
    def write_json_data_to_file(data: dict):
        with open(data_path, 'w') as file:
            file.write(json.dumps(data, indent=4))
        
    
    @app.route('/')
    def index():
        task_name: str = request.args.get('task_name')
        task_priority: str = request.args.get('task_priority')
        
        with open(data_path, 'r') as file:
            data_str: str = file.read()
        data_dict: dict = json.loads(data_str)
        if task_name and task_priority:
            data_dict['tasks'].update({
                f"{task_name}": {
                    "priority": f"{task_priority}"
                }
            })

        write_json_data_to_file(data_dict)
        
        return render_template('/index.html', task_data=data_dict)
    
    app.run()

if __name__ == "__main__":
    run()