import socket

socks = socket.socket()
socks.bind(('', 9080))
socks.listen(1)
conn, addr = socks.accept()

print('connected:', addr)

while True:
    inp = conn.recv(1024).decode()
    if not inp:
        break
    s= inp.split(' ')
    a=int(s[0])
    b=int(s[1])
    c=int(s[2])
    d=int(s[3])
    k=int(s[4])
    if b==0 or a==0:
        rez="Ошибка, неверно введены данные"
        conn.send(rez.encode())
    else:
        r=abs(((a**2-b**3-c**3 * a**2)*(b-c+c*(k-d/b**3))-(k/b-k/a)*c)**2-20000)
    rez = str(r)
    conn.send(rez.encode())

conn.close()