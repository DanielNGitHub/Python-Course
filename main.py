clients='Daniel,Oscar,'

def new_client (client):
    global clients
    if client not in clients:
       clients+=client
       _add_comma()
    else:
        print('The client is already in the list')

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

if __name__ == "__main__":
    _print_welcome()
    command= input()
    if command =='C':
        client_name= input('What is the client Name?')
        new_client(client_name)
        clients_list()
    elif command =='D':
        pass
    else: 
        print('Ivalid command')


  





