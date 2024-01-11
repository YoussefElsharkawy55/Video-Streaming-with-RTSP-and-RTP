import socket

class VideoClient:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client_socket.connect((self.server_ip, self.server_port))

    def send_play_command(self):
        self.client_socket.sendall(b'PLAY')

    def send_pause_command(self):
        self.client_socket.sendall(b'PAUSE')
    

    def connect(self):
        try:
            self.client_socket.connect((self.server_ip, self.server_port))
        except ConnectionRefusedError:
            print("قشطه.")
            exit(1)
    def send_play_command(self):
        self.client_socket.sendall(b'PLAY')
        print("Play command sent to the server.")
    def send_pause_command(self):
        self.client_socket.sendall(b'PAUSE')
        print("Pause command sent to the server.")



client = VideoClient('127.0.0.1', 5000)
client.connect()
client.send_play_command()
client.send_pause_command()