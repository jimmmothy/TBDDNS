## TBDDNS
terribly basic dynamic dns - "doesn't even have anything to do with dns"


Media server hosted with a dynamic IP in differant location

Need to keep track of its IP so i can SSH/VNC in etc.

Playing around with a basic FLASK REST-API to see how its done

#### Endpoints

POST /ip insert IP

GET /ip retreive latest IP

#### USAGE-
Cronjob on media server running a bash script similar (obviously chance the localhost address to the 
location the flask script is running):

ENTRY=$(curl -s ifconfig.co) && curl -X PUT -H 'Content-Type: application/json' -d "{\"ip\" : \"${ENTRY}\"}" http://127.0.0.1:5000/ip

Use something like this to obtain the IP when you need it

curl -X GET -H 'Content-Type: application/json' http://127.0.0.1:5000/ip

#### Things to do
Stop double ups

HTTPS or authentication/security

Return differant status codes where appropriate

Make a class to handle file IO

Simplify it and only use the one entry, do we really need history? probs not

Ditch basic bitch files and use a db



#### Helpful links along the way
https://pythonbasics.org/flask-rest-api/

https://terminalcheatsheet.com/guides/curl-rest-api