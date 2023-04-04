import json
from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Open a list of roles
roles = ['W', 'I', 'F', 'FR', 'Open']

# Render the template
@app.route('/', methods=['GET', 'POST'])
def index():
    # Create an empty tables.json file if it doesn't exist
    if not os.path.exists('tables.json'):
        with open('tables.json', 'w') as f:
            json.dump({}, f)

    if request.method == 'POST':
        # Get table data from form submission
        table_data = {}
        for chair_name in request.form:
            chair_role = request.form[chair_name]
            table_data[chair_name] = chair_role

        # Increment table number
        with open('tables.json', 'r') as f:
            tables = json.load(f)
            table_number = len(tables)
        table_name = f'T{table_number}'

        # Add new table to tables.json
        tables[table_name] = table_data
        with open('tables.json', 'w') as f:
            json.dump(tables, f)

    # Render the template with table data
    with open('tables.json', 'r') as f:
        tables = json.load(f)
    table_list = []
    for table_name, table_data in tables.items():
        table_dict = {'name': table_name, 'chairs': []}
        for chair_name, chair_role in table_data.items():
            chair_dict = {'name': chair_name, 'role': chair_role}
            table_dict['chairs'].append(chair_dict)
        table_list.append(table_dict)

    return render_template('index.html', table_list=table_list, roles=roles)

if __name__ == '__main__':
    app.run(debug=True)
