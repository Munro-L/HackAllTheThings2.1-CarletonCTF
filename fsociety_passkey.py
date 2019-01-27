import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("34.209.135.233", 6043))     # ip was set up specifc to this event
#s.shutdown(socket.SHUT_WR)
data = s.recv(1024)

for i in range(1, 11):
    data = str(data)
    data = data.replace("\\n", " ")

    print(data)

    a = 0
    b = 0
    c = 0

    for word in data.split():
        if (word.isdigit()):
            if (word == "20" or word == "10"):
                continue
            if a == 0:
                a = int(word)
            elif b == 0:
                b = int(word)
            elif c == 0:
                c = int(word)

    print(str(a) + "^" + "x % " + str(b) + " = " + str(c))

    for i in range(1, 100000000):
        if ((pow(a, i, b)) == c):
            buffer = str(i) + "\n"
            print(buffer.encode())
            s.sendto(buffer.encode(), ("34.209.135.233", 6043))
            data = s.recv(1024)
            print(str(data))
            break
