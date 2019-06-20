import requests as req

server_address = "localhost:5000"

print(req.get(server_address + "/valve"))
