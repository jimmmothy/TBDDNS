#!/usr/bin/python3

from ipsanity import ipsanity
import json
from flask import Flask, request
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

    if ipsanity(input_ip).valid == False:
        return "Invalid IP address\n", 400

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