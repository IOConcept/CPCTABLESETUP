# Table with Chairs and Roles
This is a Flask application that allows you to create tables with chairs and assign roles to them.

Setup
Clone this repository to your local machine
Install the required dependencies by running pip install -r requirements.txt
Run the Flask application by running python main.py
Navigate to http://localhost:5000 in your web browser
Usage
Creating Tables
To create a new table, click the "Create Table" button on the homepage. This will take you to a page where you can enter the name of the table and the number of chairs it will have. Once you have entered this information, click the "Create" button to create the table.

Assigning Roles
To assign roles to the chairs in a table, select the role from the dropdown list next to the chair's name. Once you have assigned roles to all the chairs, click the "Submit" button to save your changes.

Viewing Tables
To view a table, navigate to the homepage and click on the name of the table you want to view. This will take you to a page that displays the chairs in the table and the roles assigned to them.

Data Storage
Table and chair data is stored in a tables.json file in the root directory of the application. This file is automatically created when you create your first table, and is updated every time you make changes to the chairs in a table.
