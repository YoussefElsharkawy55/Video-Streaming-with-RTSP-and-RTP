import time
import socket
import threading

class VideoServer:
    def __init__(self, server_ip, server_port, buffer_size):
        #initialize the server
        self.server_ip = server_ip
        self.server_port = server_port
        self.buffer_size = buffer_size
        self.seq_num = 0
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.server_ip, self.server_port))
# This function creates an RTP packet with a given frame
#hat constructs an RTP  packet header with a sequence number and combines it with a video frame
    def create_rtp_packet(self, frame):
        rtp_header = bytearray()
        rtp_header.extend((0x80, 0x60, self.seq_num >> 8, self.seq_num & 0xFF, 0, 0, 0, 0, 0, 0, 0, 0))
        self.seq_num += 1
        rtp_packet = rtp_header + frame
        return rtp_packet
#that sends the RTP packet through the server's UDP socket to the specified IP address and port..
    def send_rtp_packet(self, rtp_packet):
        self.server_socket.sendto(rtp_packet, (self.server_ip, self.server_port))
# This function opens a video file in binary read mode
    def open_video(self, video_file):
        self.video_file = open(video_file, 'rb')
# This function closes the video file.
    def close_video(self):
        self.video_file.close()
# This function starts a new thread to send the video
    def run(self, video_file):
        video_thread = threading.Thread(target=self.send_video, args=(video_file,))
        video_thread.start()
# This function reads frames from the video file, creates RTP packets, and sends them.
    def send_video(self,video_file):
        self.open_video(video_file)
        while True:
            frame = self.video_file.read(self.buffer_size)
            if not frame:
                break
            rtp_packet = self.create_rtp_packet(frame)
            self.send_rtp_packet(rtp_packet)
            time.sleep(0.05)
        self.close_video()
        print('Video transmission completed')
# This function starts the server and begins streaming the video.
def run(self, video_file):
    print("Starting video streaming server...")
    video_thread = threading.Thread(target=self.send_video, args=(video_file,))
    video_thread.start()
    print("Server is running.")
# This function opens a video file in binary read mode with error handling.
def open_video(self, video_file):
    try:
        self.video_file = open(video_file, 'rb')
    except FileNotFoundError:
        print("Error: File not found.")
        exit(1)
    except IOError:
        print("Error: Could not open the file.")
        exit(1)

        

server = VideoServer('127.0.0.1', 5000, 2048)
server.run('cat.mp4')