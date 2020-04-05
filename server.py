import socket

host = socket.gethostname()
port = 9337


# define server
sock_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # address family_internet for iPV4, TCP connection
sock_.bind((host, port))

# listen for connections

sock_.listen(1) # backlog - number of unnaccepted connections before server starts to refuse new connections
print('\n Server Started...\n')
conn,addr = sock_.accept() # we accepted connections from the client socket conn and its address addr once connection is established

print('COnnection established with: ' + str(addr))
message = '\n Thank you for connecting ' + str(addr)

conn.send(message.encode('ascii'))
conn.close()
