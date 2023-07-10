import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port
host = '127.0.0.1'  # localhost
port = 12345

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)

print('Server is listening for connections...')

# Accept a client connection
client_socket, addr = server_socket.accept()
print('Connected to:', addr)

# Receive data from the client
data = client_socket.recv(1024).decode()
print('Received from client:', data)

# Send a response back to the client
response = 'Hello from the server!'
client_socket.send(response.encode())

# Close the connection
client_socket.close()
server_socket.close()


#######################################################
#######################################################
#######################################################


import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port
host = '127.0.0.1'  # localhost
port = 12345

# Connect to the server
client_socket.connect((host, port))
print('Connected to server')

# Send data to the server
message = 'Hello from the client!'
client_socket.send(message.encode())

# Receive the response from the server
response = client_socket.recv(1024).decode()
print('Received from server:', response)

# Close the connection
client_socket.close()
