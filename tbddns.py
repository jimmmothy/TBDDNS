#!/usr/bin/python3

# Helpful links along the way
# https://pythonbasics.org/flask-rest-api/
# https://terminalcheatsheet.com/guides/curl-rest-api

'''
Media server hosted with a dynamic IP in differant location
Need to keep track of its IP so i can SSH in etc

Endpoints
POST /ip insert IP
GET /ip retreive latest IP

curl -X PUT -H 'Content-Type: application/json' -d '{"ip" : "1.1.1.1"}' http://127.0.0.1:5000/ip
curl -X GET -H 'Content-Type: application/json' http://127.0.0.1:5000/ip

Things to do-
HTTPS or authentication/security
Return differant status codes where appropriate
Verify that PUT inputs are actually IP addresses
Make a class to handle file IO
Simplify it and only use the one entry, do we really need history? probs not
Ditch basic bitch files and use a db
'''

import json
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)
IP_FILE = "/tmp/ip.txt"

@app.route('/')
def index():
    payload = {'brother' : '4 8 15 16 23 42'}
    return payload, 200

@app.route('/ip', methods=['GET'])
def get_ip():
    with open(IP_FILE, 'r') as f:
        q = f.readlines()

        if len(q) >= 1:
            ip = q[0].split('\t')[0]
            ip_time = q[0].split('\t')[1][:-1]
    f.close()

    payload = {'ip' : ip}
    return payload, 200

@app.route('/ip', methods=['PUT'])
def insert_ip():
    args = json.loads(request.data)
    input_ip = args['ip']
    timestamp = datetime.datetime.now()
    new_entry = input_ip + '\t' + str(timestamp) + '\n'

    try:
        f = open(IP_FILE, 'r')
        fchar = f.read(1)
        if fchar != '':
            f.seek(0)
            existing_entries = f.readlines()
        f.close()
    except:
        f = open(IP_FILE, "x")
        f.close()
        fchar = ''

    if fchar == '':
        f = open(IP_FILE, 'w')
        f.write(new_entry)
        f.close()

    else:
        f = open(IP_FILE, 'w')
        f.seek(0)
        f.write(new_entry)

        for line in existing_entries:
            print(line)
            f.write(line)
        f.close()

    return "Success\n", 200
    

if __name__ == '__main__':
    app.run()