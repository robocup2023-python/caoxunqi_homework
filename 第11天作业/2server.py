#热爱学习的CXQ

from socket import *
import socket
import requests
import threading


IP=''
Port=50000
Buflen=1024


def translate_text(text_to_translate, api_key):
    url = 'https://api.kertennet.com/live/translate'
    params = {
        'q': text_to_translate,
        'key': api_key,
        'target': 'en'  # 目标语言，这里以英语为例
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        translated_text = response.json()['data']['translations'][0]['translatedText']
        return translated_text
    else:
        return None

def handle_client(client_socket, api_key):
    request_data = client_socket.recv(1024).decode('utf-8')
    translated_text = translate_text(request_data, api_key)
    if translated_text:
        client_socket.send(translated_text.encode('utf-8'))
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 50000))
    server_socket.listen(5)
    print("Server listening on port 50000...")

    api_key = ''

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        client_thread = threading.Thread(target=handle_client, args=(client_socket, api_key))
        client_thread.start()

if __name__ == "__main__":
    main()