from socket import *
import os
import sys

def sendData(data):
    data = data.encode()
    length = len(data)
    clientSock.sendall(length.to_bytes(4, byteorder="little"))
    clientSock.sendall(data)

def recvData():
    data = clientSock.recv(4)
    length = int.from_bytes(data, 'little')
    return clientSock.recv(length).decode()

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 5000))

fileSock = socket(AF_INET,SOCK_STREAM)
fileSock.connect(('127.0.0.1',5001))


while True:
    
    id = input("id를 입력해주세요 : ")
    pw = input("pw를 입력해주세요 : ")

    sendData(id); sendData(pw)
    res = recvData()


    if res == "0":
        sendData("연결성공")
        print('연결에 성공했습니다.')
        while True:

            # 명령어 입력
            msg = input("명령어를 입력해주세요 : ")
            print(msg)
            sendData(msg)
            msg = msg.split(" ")
            os.chdir("C:/Temp")
            data_T = 0
            if len(msg) == 1:
                msg.append(" ")
            if msg[1] != " " and msg[0] != "/다운로드":
                size = os.path.getsize(msg[1])

            if msg[0] == "/파일목록":
                t = recvData()
                if t != "파일이 없습니다.":
                    for _ in range(int(t)):
                        print(recvData())
                    continue
                else:
                    print(t)
            if msg[0] == "/업로드":
                if recvData() != "E":
                    sendData("go")
                else:
                    print("파일이 이미 존재합니다. 덮어쓰시겠습니까? Y / N")
                    l = input()
                    sendData(l)
                    if l == "N":
                        continue
                    

                sendData("%d"%size)
                if not os.path.exists(msg[1]):
                    print("경로에 파일이 없습니다.")
                    continue
                print("업로드를 시작합니다.",msg[1])
                with open(msg[1],"rb") as f:
                    print("파일을 열었습니다.")
                    try:
                        data = f.read(1024)
                        while data:
                            data_T += fileSock.send(data)
                            data = f.read(1024)
                            if data_T >= size:
                                sendData("끝")
                            else:
                                sendData("다보냄")
                                recvData()
                        f.close()
                    except Exception as e:
                        print(e)
                print("파일 전송 완료 %-10s 전송량 %-10d"%(msg[1],data_T))
                continue
            if msg[0] == "/다운로드":
                if os.listdir().count(msg[1].split("/")[-1]):
                    print("파일이 이미 존재합니다. 덮어쓰시겠습니까? Y / N")
                    l = input()
                    if l == "Y":
                        print("덮어씁니다.")
                        sendData("go")
                    if l == "N":
                        print("처음으로 돌아갑니다.")
                        sendData("E")
                        continue
                else:
                    sendData("go")

                
                size = int(recvData())
                data = fileSock.recv(1024)
                
                if not data:
                    print('파일 %s 받는 중 에러 발생' %msg[1])
                    continue
                
                with open(msg[1],'wb') as f:
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
                                print("끝내다")
                                break
                        f.close()
                    except Exception as e:
                        print(e)
                        print("에러 남 ㅠㅠ")
                print("파일 받기 완료")
                print("업로드")
                continue
            if msg[0] == "/접속종료":
                clientSock.close()
                sys.exit()
    elif res == "1":
        print("비밀번호가 틀렸습니다.")
        continue
    elif res == "2":
        print("아이디가 존재하지 않습니다.")
        continue
    else:
        print("아무일도 발생하지 않음")
        break
        
