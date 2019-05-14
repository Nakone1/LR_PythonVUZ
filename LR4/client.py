import socket

sock = socket.socket()
sock.connect(('localhost', 9080))
mission = input('Введите значения a,b,c,d,k по шаблону: 1 2 3 4 5:\n')
sock.send(mission.encode())

answer= sock.recv(1024).decode()
sock.close()
print('Результат: ', answer)