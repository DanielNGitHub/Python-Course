import sys
clients=[{'name':'Pablo','company':'Google','email':'plablo@google.com',
'position':'Software Enginner'}
,{
'name':'Ricardo','company':'Facebook','email':'ricardo@facebook.com','position':'Date Engineer'
}]


def _welcome_options():
    print('welcome to my first CRUD please choose the below options')
    print('[C]reate a new client')
    print('[U]update a client from our client list')
    print('[D]elete a client')
    print('[L]ist of clients')
    print('[S]earche a client')

def _get_client_field(field_name):
    field=None
    while not field:
        field=input('What is the client {}?'.format(field_name))
    return field

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

def clients_list():
    '''
    Usamos la funcion enumerate e inmediatamente queda a siganda a index,
    demanera que podemos mostrar el index con su cliente usanto format()
    '''
    global clients
    for index,client in enumerate(clients): 
        print('{uid} | {name} | {company} | {email} | {email} |{position}'.format(
            uid=index,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))

def create_client(client):
    global clients
    '''
    Usamos el metodo append para añadir al cliente en nuestra lista
    ''' 
    if client not in clientcs:
       
     clients.update(client)
    else:
      print('The client was created before')

def uptodate_clients(old_client,new_client):
    '''
    Buscamos el index que tiene un parametro dentro de una lista con elmetodo index()
    luego lo usamos para reemplazar el old_client por el new_client en la misma posicion
    '''
    global clients
    if old_client in clients:
       index=clients.index(old_client)
       clients[index]=new_client

    else:
        print('The client doesn\'t exist in our list please select create a client')

def delete_client(client):
    '''
    Al igual que en uptodate_client con el index usamos la funcion del, aunque otra opcion sería remove() pues no requiere
    sino unicamente el valor lo caul lo hace mas simple.
    '''
    global clients
    if client in clients:
     index=clients.index(client)
     del clients[index]
        
    else:
        print('The client doesn\'t exist in our list please select create a client')
    
def search_client(client):
    global clients
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
        client ={
            'name':_get_client_field('name'),
            'company':_get_client_field('company'),
            'email':_get_client_field('email'),
            'position':_get_client_field('position'),
        }
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

  





