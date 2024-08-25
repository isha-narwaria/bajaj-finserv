from flask import Flask, request, jsonify

app = Flask(__name__)

def process_data(data):
    numbers = []
    alphabets = []
    highest_lowercase_alphabet = []

    for item in data:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            alphabets.append(item)
            if item.islower():
                highest_lowercase_alphabet.append(item)

    return {
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": sorted(highest_lowercase_alphabet)[-1:] if highest_lowercase_alphabet else []
    }

@app.route('/bfhl', methods=['POST'])
def bfhl_post():
    data = request.json.get('data')
    result = process_data(data)
    response = {
        "is_success": True,
        "user_id": "your_name_ddmmyyyy",
        "email": "your_email@domain.com",
        "roll_number": "21BCE8774",
        **result
    }
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
