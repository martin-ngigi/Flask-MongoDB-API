# FLASK API IN Mongo DB 
## Prerequisites
- Python 3.6 and above installed on your computer.
- Postman installed on your computer.
- Mongo Atlas(online db).
- Favourite code editor installed. I use Pycharm community edition which is free.
- Some knowledge of the Python programming language.  
## Steps:
- Create and activate a virtual environment named .venv:

           
            py -3 -m venv .venv
            .venv\scripts\activate
- Update pip in the virtual environment:


            python -m pip install --upgrade pip
- Install Flask in the virtual environment:

            python -m pip install flask
- Install required libraries from the requirements file:

            pip install -r requirements.txt
- Create a new file in your project folder named app.py
- Runs the Flask development server(i.e. app.py):

            flask run
 - Create new dabase in MYSQL xampp database named "flask_mysql_db":

            flask_mysql_db

## API
1. POST -> Create Person
- endpoint -> http://127.0.0.1:5000//api/register
- body ->

            {
                "first_name": "Simon",
                "last_name": "Kimani",
                "age": 13,
                "role": "IT",
                "games": "Coding",
                "contacts": "078763"
            }

- response:

            {
                "message": "User added on $<pymongo.results.InsertOneResult object at 0x000001B3A336A800>",
                "user": "{'first_name': 'Simon', 'last_name': 'Kimani', 'age': 13, 'role': 'IT', 'games': 'Coding', 'contacts': '078763', '_id': ObjectId('63b548d349324c190a97e884')}"
            }

2. GET -> Get all users
- endpoint -> http://127.0.0.1:5000/api/users
- response:

            "[{'_id': ObjectId('63b51705cd441e946a5b0a40'), 'first_name': 'Martin', 'last_name': 'Ngigi', 'age': 23, 'role': 'IT', 'games': 'Coding', 'contacts': '078763'}, {'_id': ObjectId('63b548a3c8687b97249a95d6'), 'first_name': 'Simon', 'last_name': 'Kimani', 'age': 13, 'role': 'IT', 'games': 'Coding', 'contacts': '078763'}]"