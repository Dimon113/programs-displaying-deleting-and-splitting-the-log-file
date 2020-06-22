import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('127.0.0.1', 53210))
print("Для прочтения файла с логами введите 1")
print("Для нахождения конкретной строки нажмите 2 и введите строку ")
"""
data = input("Введите значение: ")
client_sock.sendall(data.encode())
print("<Timestap>           <Message Type>            <Source of message>:Log message itself>")
if data == '2':
     data =input("Введите слово: ")
     client_sock.sendall(data.encode())
client_sock.sendall(data.encode())
"""

lines_index = []

client_sock.settimeout(1.0)
data1 = client_sock.settimeout(300)


def sandMessage():  #объявляем функцию для отправки и приема сообщений
    data = input("Введите значение: ")
    client_sock.sendall(data.encode())  
    #print("<Timestap>           <Message Type>            <Source of message>:Log message itself>")
    if data == '2':  #если введеное значение равно 2 то начинаем новый алгоритм для поискового запроса
        data = input("Введите слово: ")
        client_sock.sendall(data.encode())  #отправляем серверу поисковой запрос
    print("<Timestap>           <Message Type>            <Source of message>:Log message itself>")
    while data != "":  #пока полученные сообщения от сервера не пусты клиент прослушивает их
           data = client_sock.recv(1024)  #прием сообщений
           print(data.decode("utf-8"))  #вывод их в терминал
    return sandMessage()  #вызываем заново sandMessage для отправки значения и поскового запроса 

while True:
    sandMessage()  #вызываем функцию sandMessage
client_sock.close()
