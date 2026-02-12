import  socket
import sys
import  threading as th

if len(sys.argv) != 4:
    print(f"Usage : python port_scanner.py Target Start_port End_port")
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print(f"Hostname could not be resolved. Exiting")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

def scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target,port))
    if result == 0:
        print(f"Port {port} is open")

for port in range(start_port, end_port):
    t1 = th.Thread(target=scan, args=(port,))
    t1.start()
