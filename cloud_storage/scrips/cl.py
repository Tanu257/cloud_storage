import socket,threading,pickle,os

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_hostname = socket.gethostname()
local_ip = socket.gethostbyname(local_hostname)
port = 8080
sock.connect((local_ip, port))
pats = ["__path__+"]
def send_to_server():
    with open(pats[0],'rb') as f:
        readed = f.read()
        toSenPacket = [os.path.basename(pats[0]),readed]
        sock.send(pickle.dumps(toSenPacket))

def get_path():
    while True:
        a = input("Enter path :- ")
        pats[0] = a

        send_to_server()

threading.Thread(target=get_path).start()   