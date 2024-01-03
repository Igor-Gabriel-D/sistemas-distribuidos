import socket
import time
import threading

host = "localhost"  # Endereço do servidor
port = 12345  # Porta do servidor
# client_socket.recv(1024).decode('utf-8')
# client_socket.send(str(f"Usuario {pid} enviou: {num1}").encode('utf-8'))

saldo = 2000
queue= [] 
lock = True

def saque(valor):
  global saldo
  saldo = saldo - valor
  return saldo
  

def client_req(client_socket):
  global queue
  global lock
  
  pid = client_socket.recv(1024).decode('utf-8')
  pid = int(pid)
  print(f"\nConexão com o cliente {pid} estabelecida.\n=================")
  time.sleep(1)
  queue.append(pid)

  if lock and queue[0] == pid:
    lock = False
    print(f"\nCliente {pid} solicitou saque.\n=================")
  
  client_socket.send(str(f'''=================
  Conexão estabelecida com o servidor, seu PID é {pid}''').encode('utf-8'))
  
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((host, port))

server_socket.listen(1)

print(f"Servidor ouvindo em {host}:{port}")


while True:
  client_socket, client_address = server_socket.accept()


  client_thread = threading.Thread(target=client_req, args=(client_socket,))


  client_thread.start()


