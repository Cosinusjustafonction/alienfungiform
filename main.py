from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

# Load existing email data from the file
email_list = []
with open("email_data.txt", "r") as file:
    for line in file:
        email_list.append(line.strip())

# Load existing Twitter data from the file
twitter_list = []
with open("twitter_data.txt", "r") as file:
    for line in file:
        twitter_list.append(line.strip())

# Load existing Discord data from the file
discord_list = []
with open("discord_data.txt", "r") as file:
    for line in file:
        discord_list.append(line.strip())

@app.route('/check_email', methods=['POST', 'GET'])
def check_email():
    data = request.get_json()

    if 'email' not in data:
        return jsonify({"found": False}), 400

    email_to_check = data['email']

    time.sleep(2)

    if email_to_check in email_list:
        return jsonify({"valid": False})
    else:
        return jsonify({"valid": True})

@app.route('/add_email', methods=['POST', 'GET'])
def add_email():
    data = request.get_json()

    if 'email' not in data:
        return jsonify({"found": False}), 400

    email_to_add = data['email']

    if email_to_add in email_list:
        return jsonify({"added": False})
    else:
        email_list.append(email_to_add)
        with open("email_data.txt", "a") as file:
            file.write(email_to_add + "\n")
        return jsonify({"added": True})

@app.route('/check_twitter', methods=['POST', 'GET'])
def check_twitter():
    data = request.get_json()

    if 'twitter' not in data:
        return jsonify({"found": False}), 400

    twitter_to_check = data['twitter']

    time.sleep(2)

    if twitter_to_check in twitter_list:
        return jsonify({"valid": False})
    else:
        return jsonify({"valid": True})

@app.route('/add_twitter', methods=['POST', 'GET'])
def add_twitter():
    data = request.get_json()

    if 'twitter' not in data:
        return jsonify({"found": False}), 400

    twitter_to_add = data['twitter']

    if twitter_to_add in twitter_list:
        return jsonify({"added": False})
    else:
        twitter_list.append(twitter_to_add)
        with open("twitter_data.txt", "a") as file:
            file.write(twitter_to_add + "\n")
        return jsonify({"added": True})

@app.route('/check_discord', methods=['POST', 'GET'])
def check_discord():
    data = request.get_json()

    if 'discord' not in data:
        return jsonify({"found": False}), 400

    discord_to_check = data['discord']

    time.sleep(2)

    if discord_to_check in discord_list:
        return jsonify({"valid": False})
    else:
        return jsonify({"valid": True})

@app.route('/add_discord', methods=['POST', 'GET'])
def add_discord():
    data = request.get_json()

    if 'discord' not in data:
        return jsonify({"found": False}), 400

    discord_to_add = data['discord']

    if discord_to_add in discord_list:
        return jsonify({"added": False})
    else:
        discord_list.append(discord_to_add)
        with open("discord_data.txt", "a") as file:
            file.write(discord_to_add + "\n")
        return jsonify({"added": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
