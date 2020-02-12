clients='Daniel,Oscar,Ricardo,Oliver,'

def new_client (client):
    '''
    Tuve inconvenientes el refundir client con clients
    '''
    global clients
    if client not in clients:
       clients+=client
       _add_comma()
    else:
        print('The client is already in the list')

def delete_client(client):
    '''
    Al igual que la anterior no habia declarado clients como global y esta 
    evaluando client en clients, mas de 15 min tratando de resolver el problema
    '''
    global clients    
    if client in clients:
       clients = clients.replace(client + ',','')
    
    else: 
     print('Client with name '+client+' was\'t fount please create a new one')

def uptodate_client(old,new):
    '''
    El comando es replace y se debe colocar los dos argumentos separados por ',' y colocar
    la coma seguido del nombre debido a que esta se pierde cuando re remplaza o elimina 
    un nombre
    '''
    global clients
    if old in clients:
      clients = clients.replace(old + ',', new + ',')
    
    else: 
     print('Client with name '+old+' was\'t fount please create a new one')

def search_client(client_name):
    clients_list=clients.split(',')
    for client in clients_list:
        if client == client_name:
            return True
        else:
            continue

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
    print('[L]ist of Clients')
    print('[C]reate a Client')
    print('[D]elete a Client')
    print('[U]update client')
    print('[S]earch a Client')

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
    elif command == 'S':
        client_name=get_client_name()
        found=search_client(client_name)
        if found:
            print('The client {} is in our list'.format(client_name))
        else:
            print('The client {} wasn\'t found' .format(client_name))

    elif command=='U':
        actual_client=get_client_name()
        update_client=input('What is the new client name')
        uptodate_client(actual_client,update_client)
        clients_list()
    elif command == 'L':
        clients_list()
    else: 
        print('Ivalid command')


  





