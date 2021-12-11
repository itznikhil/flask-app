from flask import Flask, request, jsonify

app = Flask(__name__)

contacts = [
    {
        "Contact": "9987644456",
        "Name": "Raju",
        "done": False,
        "id": 1
    },
    {
        "Contact": "9876543222",
        "Name": "Rahul",
        "done": False,
        "id": 2
    }
]


@app.route("/add-data", methods=['POST'])
def add_contact():
    if(not request.json):
        return jsonify({'status': 'error',
                        'message': 'Please provide data!'}, 400)
    contact = {
        'id': contacts[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get("Contact", ""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({'status': 'success', 'message': "contact added"})


@app.route("/get-data", methods=['GET'])
def get_contacts():
    return jsonify({'data': contacts})


if __name__ == "__main__":
    app.run(debug=True)
