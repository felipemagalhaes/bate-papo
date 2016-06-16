# encoding: utf-8

import os, sys, socket, select

RECV_BUFFER = 4096

def chat_client():
    if(len(sys.argv) < 3) :
        print 'Utilize : python chat_client.py localhost numero_da_porta'
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # Conectar ao servidor remoto
    try :
        s.connect((host, port))
    except :
        print 'Impossível conectar'
        sys.exit()
    
    os.system('cls' if os.name == 'nt' else 'clear') #limpar a tela
    nome =raw_input("\nOlá, seja bem vindo! Digite seu nome: ") 
    print 'Conectado a um servidor remoto. Você pode começar a enviar mensagens'
    print
    sys.stdout.write(nome+': '); sys.stdout.flush()
    while 1:
        socket_list = [sys.stdin, s]
         
        # Pega lista de sockets que são legíveis
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:            
            if sock == s:
                # Recebendo mensagem de um servidor remoto, s
                data = sock.recv(RECV_BUFFER)
                if not data :
                    print '\nDesconectado do servidor do chat'
                    sys.exit()
                else :
                    #Imprime dado
                    sys.stdout.write(data)
                    sys.stdout.write(nome+': '); sys.stdout.flush()     
            
            else :
                # user entered a message
                msg = sys.stdin.readline()
                s.send(msg)
                sys.stdout.write(nome+': '); sys.stdout.flush() 

if __name__ == "__main__":

    sys.exit(chat_client())
