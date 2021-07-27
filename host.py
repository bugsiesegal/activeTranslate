import speech_recognition as sr
import socket, threading, _thread, json

def client_thread(clientsocket):
    HOST = '127.0.0.1'
    PORT = 6000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print("connection accepted")
            while True:
                pass

HOST = '127.0.0.1'
PORT = 6000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("connection accepted")
        while True:
            file = open('translate-321018-b1e69ccd7eeb.json')
            apijson = json.load(file)
            data = conn.recv(2048)
            print(sr.Recognizer().recognize_google_cloud(data, apijson))