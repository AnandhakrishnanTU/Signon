import socket

def test():
    try:
        socket.create_connection(('google.com',80))
        return True
    except OSError:
        return False

print(test())