import socket,threading,pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_hostname = socket.gethostname()
local_ip = socket.gethostbyname(local_hostname)
port = 8080
s.bind((local_ip, port))

s.listen(5)

# vars

socks = []
storage_path = "F:\Tirth\Serius\cloud_storage\storg\\"


def accepter():
    while True:
        sock_obj,addr=s.accept()
        socks.append(sock_obj)
def listen():
    
    while True:
        if len(socks) > 0:
            got = pickle.loads(socks[0].recv(511627776))

            with open(storage_path+got[0],'wb') as f:
                f.write(got[1])
if __name__ == "__main__":
    threading.Thread(target=accepter).start()
    threading.Thread(target=listen).start()
