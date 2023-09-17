# open the file and read all the data
with open('Flag.jpg', 'rb') as f:
    data = f.read()

# search for 'CORRUPTED' and remove it
index = 0
while index < len(data) - 9:
    if data[index : index + 9] == b'CORRUPTED':
        data = data[ : index] + data[index + 9 : ]
    else:
        index += 1

# write the file
with open('Flag.remove.jpg', 'wb') as f:
    f.write(data)
