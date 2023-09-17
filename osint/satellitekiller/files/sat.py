from dateutil.parser import parse

# keep a lit of all the lines that contain our satellite name
lines = []

# open the file
with open('currentcat.tsv') as f:
    # read in one line at a time
    for line in f.readlines():
        # check if the line contains our satellite name
        if 'P78-1' in line:
            # add it to the lines
            lines.append(line)

# now we will sort the lines by the 13th tab separated value in each line
# the 13th value is the de-orbit data
lines.sort(key=lambda x: parse(x.split('\t')[13]))

# show the information we want for each line
for line in lines:
    date = line.split('\t')[13]
    id = line.split('\t')[3]
    print(f'{date} - {id}')
