from multiprocessing import connection
from socket import *
import os 
import threading


users = {'admin':'1234'}


serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
serverSock.bind(('', 5000))
serverSock.listen()

fileSock = socket(AF_INET,SOCK_STREAM)
fileSock.bind(('',5001))
fileSock.listen()

def sendData(data):
    data = data.encode()
    length = len(data)
    connectionSock.sendall(length.to_bytes(4, byteorder="little"))
    connectionSock.sendall(data)

def recvData():
    data = connectionSock.recv(4)
    length = int.from_bytes(data, 'little')
    data = connectionSock.recv(length)
    data = data.decode()
    return data



def fu():
    while True:
        id = recvData()
        pw = recvData()
        print(id,users[id])
        if users[id]:
            if users[id] == pw:
                sendData("0")
                while True:
                    print("명령 받는 중...")
                    msg = recvData()
                    msg = msg.split(" ")
                    if len(msg) == 1:
                        msg.append("")                         
                    filename = msg[-1]
                    os.chdir("C:/Download")
                    filelist = os.listdir()
                    data_T = 0

                    if msg[0] == "/파일목록": # 파일 목록을 띄워 준다
                        if filelist:
                            sendData("%d"%len(filelist))
                            for i in filelist:
                                size = os.path.getsize(i)
                                a = "%10s"%i + "\t" + "%10d"%size + "b"
                                sendData(a)
                            continue
                        else:
                            sendData("파일이 없습니다.")
                            continue
                    if msg[0] == "/업로드": # 파일을 받아서 저장소에 저장한다.
                        size = int(recvData())
                        data = fileSock.recv(1024)
                        
                        if not data:
                            print('파일 %s 받는 중 에러 발생' %filename)
                            continue
                        
                        with open(filename,'wb') as f:
                            print("파일 받는 중...")
                            try:
                                a = recvData()
                                while data:
                                    f.write(data)
                                    print("데이터 씀")
                                    data_T += len(data)
                                    print("길이 구함")
                                    print(a)
                                    if a == "다보냄":
                                        sendData("")
                                        data = fileSock.recv(1024)
                                        a = recvData()
                                    print("데이터 받음")
                                    print("size : ",size," data_T : ",data_T)
                                    if a == "끝":
                                        f.write(data)
                                        print("끝내다")
                                        break
                                f.close()
                            except Exception as e:
                                print(e)
                                print("에러 남")
                        print("파일 받기 완료")
                        print("업로드")
                        continue
                    if msg[0] == "/다운로드": # 다운받을 파일을 담아 클라이언트로 보내준다
                        size = os.path.getsize(filename)
                        sendData("%d"%size)
                        if not os.path.exists(filename):
                            print("경로에 파일이 없습니다.")
                            continue
                        print("업로드를 시작합니다.",msg,filename)
                        with open(filename,"rb") as f:
                            print("파일을 열었습니다.")
                            try:
                                data = f.read(1024)
                                while data:
                                    data_T += fileSock.send(data)
                                    data = f.read(1024)
                                    if data_T == size:
                                        sendData("끝")
                                    else:
                                        sendData("다보냄")
                                        recvData()
                                f.close()
                            except Exception as e:
                                print(e)
                        print("파일 전송 완료 %10s 전송량 %10d"%(filename,data_T))
                        continue
                    if msg[0] == "/끝내기":
                        connectionSock.close()
                        fileSock.close()
                        break
            else:
                print("비밀번호")
                sendData("1")
                continue
        else:
            print("없다 아이디")
            sendData("2")
            continue
        


try:
    while True:
        connectionSock, caddr = serverSock.accept()
        fileSock, faddr = fileSock.accept()

        Thread = threading.Thread(target=fu,args=())
        Thread.start()
except Exception as e:
    print(e)