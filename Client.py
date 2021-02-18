import socket

class Client:
    def __init_(self):
        pass
    def check_server(self,address, port) -> bool:
        # Create a TCP socket
        with socket.socket() as s:
            print("Attempting to connect to %s on port %s" % (address, port))
            try:
                s.connect((address, port))
                print("Connected.")
                return True
            except:
                print("Connection failed.")
                return False
