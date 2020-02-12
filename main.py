clients='Daniel,Oscar,Ricardo,Oliver,'

def new_client (client):
    global clients
    if client not in clients:
       clients+=client
       _add_comma()
    else:
        print('The client is already in the list')

def delete_client(client):
    global clients    
    if client in clients:
       clients = clients.replace(client + ',','')
    
    else: 
     print('Client with name '+client+' was\'t fount please create a new one')

def uptodate_client(old,new):
    global clients
    if old in clients:
      clients = clients.replace(old + ',', new + ',')
    
    else: 
     print('Client with name '+old+' was\'t fount please create a new one')

def _add_comma():
    global clients
    clients+=','

def clients_list():
    global clients
    print(clients)

def _print_welcome():
    print('Welcome to our New Brand Interface')
    print('*'*50)
    print('What would you like to do today')
    print('[C]reate a Client')
    print('[D]elete a Client')
    print('[U]update client')

def get_client_name():
    return input('What is the client name')

if __name__ == "__main__":

    _print_welcome()
    command= input()
    command=command.upper()

    if command =='C': 
        client_name= get_client_name()
        new_client(client_name)
        clients_list()
    elif command =='D':
        client_name=input('What is the name of the client for Delete')
        delete_client(client_name)
        clients_list()

    elif command=='U':
        actual_client=get_client_name()
        update_client=input('What is the new client name')
        uptodate_client(actual_client,update_client)
        clients_list()
    else: 
        print('Ivalid command')


  





