from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\nMy message"
    endmsg = "\r\n.\r\n"  # End the message with a period on a new line.

    # Create a socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    # Receive the server's greeting message.
    recv = clientSocket.recv(1024).decode()
    #print(recv)  # Debugging: print the server response.
    #if recv[:3] != '220':
    #   print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)  # Debugging: print the server response.
    #if recv1[:3] != '250':
    #   print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    mailFrom = 'MAIL FROM:<sender@example.com>\r\n'
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print(recv2)  # Debugging: print the server response.
    #if recv2[:3] != '250':
    #    print('250 reply not received from server.')

    # Send RCPT TO command and handle server response.
    rcptTo = 'RCPT TO:<recipient@example.com>\r\n'
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print(recv3)  # Debugging: print the server response.
    #if recv3[:3] != '250':
    #    print('250 reply not received from server.')

    # Send DATA command and handle server response.
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    #print(recv4)  # Debugging: print the server response.
    #if recv4[:3] != '354':
    #   print('354 reply not received from server.')

    # Send message data (the content of the email).
    clientSocket.send(msg.encode())

    # Send the end of the message with a period on a new line.
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    #print(recv5)  # Debugging: print the server response.
    #if recv5[:3] != '250':
    #    print('250 reply not received from server.')

    # Send QUIT command and handle server response.
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv6 = clientSocket.recv(1024).decode()
    #print(recv6)  # Debugging: print the server response.
    #if recv6[:3] != '221':
    #    print('221 reply not received from server.')

    # Close the connection
    clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')

