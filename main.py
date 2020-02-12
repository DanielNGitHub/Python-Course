clients='Daniel,Oscar,'

def new_client (client):
    global clients
    clients+=client
    _add_comma()

def _add_comma():
    global clients
    clients+=','

def clients_list():
    global clients
    print(clients)

if __name__ == "__main__":
  new_client ('Homero')
  clients_list()



