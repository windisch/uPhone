from uphone import Client


url = input('URL of uPhone: ')
port = int(input("Port [9999]: ") or "9999")

client = Client(url=url, port=port)
client.connect()
