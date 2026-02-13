import socket
import sys
import threading as td

def display(conn):
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                print("Server disconnected")
                break
            if data.strip() == "exit":
                print("Chat ended by server")
                break
            # Clear current input line
            sys.stdout.write("\r" + " " * 50 + "\r")
            print(f"Received: {data}")
            print("Enter Message: ", end="", flush=True)
        except Exception:
            break
    conn.close()

def send(conn):
    while True:
        try:
            msg_send = input("Enter Message: ")
            conn.send(msg_send.encode())
            if msg_send.strip() == "exit":
                break
        except Exception:
            break

if __name__ == "__main__":
    HOST, PORT = "localhost", 8080
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    t1 = td.Thread(target=display, args=(s,))
    t2 = td.Thread(target=send, args=(s,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    s.close()
    print("Client closed")
