import speech_recognition as sr
import socket, threading, _thread, json, pickle
from threading import *
from _thread import *
from deep_translator import GoogleTranslator


def client_thread(conn):
    global dialogue
    while True:
        # data[0] = language
        # data[1] = text
        data = pickle.loads(conn.recv(1024))
        dialogue[conn] = data
        print(dialogue)
        for keys in dialogue.keys():
            if keys != conn:
                translated = GoogleTranslator(str(data[0]), str(data[1]))
                print(translated)
                conn.sendall(bytes(translated))


if __name__ == '__main__':
    dialogue = {}

    ServerSocket = socket.socket()
    host = '127.0.0.1'
    port = 6000
    ThreadCount = 0
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))

    print('Waiting for a Connection..')
    ServerSocket.listen(5)

    while True:
        conn, address = ServerSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(client_thread, (conn,))

        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
