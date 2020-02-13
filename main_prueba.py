import sys
clients='Daniel,Oscar,Alvaro,Miguel,'


def _welcome_options():
    print('welcome to my first CRUD please choose the below options')
    print('[C]reate a new client')
    print('[U]update a client from our client list')
    print('[D]elete a client')
    print('[L]ist of clients')
    print('[S]earche a client')

def get_client_name():
    client_name=None
    while not client_name:
      client_name= input('What is the client name')
      if client_name == 'exit':
          client_name=None
          break
    if not client_name:
        sys.exit() 
    return client_name 


def add_comma():
    global clients 
    clients+=','

def clients_list():
    global clients
    print(clients)

def create_client(client):
    global clients 
    if client not in clients:
     clients+=client
     add_comma()
    else:
      print('The client was created before')

def uptodate_clients(old_client,new_client):
    global clients
    if old_client in clients:
        clients=clients.replace(old_client+',',new_client+',')
        print('The client {} was replace for the client {}'.format(old_client,new_client)) 
    else:
        print('The client doesn\'t exist in our list please select create a client')

def delete_client(client):
    global clients
    if client in clients:
        clients=clients.replace(client +',','')
    else:
        print('The client doesn\'t exist in our list please select create a client')
    
def search_client(client):
    global clients
    clients=clients.split(',')
    for customer in clients:
        if customer==client:
            return True
        else:
            continue

if __name__ == "__main__":
    _welcome_options()

    command=input()
    command=command.upper()
    if command == 'C':
        client_name=get_client_name()
        create_client(client_name)
        clients_list()
    
    if command == 'U':
        client_name=get_client_name()
        uptodate_client =input('What is the new client name')
        uptodate_clients(client_name,uptodate_client)
        clients_list()

    if command == 'D':
        client_name=get_client_name()
        delete_client(client_name)
        clients_list()

    if command == 'L':
        clients_list()
    
    if command == 'S':
        client_name=get_client_name()
        found=search_client(client_name)
        if found:
            print('The client is in our list')
        else:
            print('The client wasn\'t found in our list')    
        


