import socket
import sys
import threading as td

def display(conn):
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                print("Client disconnected")
                break
            if data.strip() == "exit":
                print("Chat ended by client")
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
    s.bind((HOST, PORT))
    s.listen(1)

    print("Waiting for connection...")
    connection, addr = s.accept()
    print(f"Connected to {addr}")

    t1 = td.Thread(target=display, args=(connection,))
    t2 = td.Thread(target=send, args=(connection,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    s.close()
    print("Server closed")
