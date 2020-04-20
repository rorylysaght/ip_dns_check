# Open text file (iplist.txt) and iterate each line looking for IP address
# Script should ignore ordinary text and comments
# When we find an IP, ping it, then print response to file
# Written by Rory MacLysaght rorylysaght[at]gmail[dot]com
# With inspiration from these sources:
# https://stackoverflow.com/questions/2953462/pinging-servers-in-python
# https://www.regular-expressions.info/ip.html

# ####### ####### WARNING ####### #######
# Use this ONLY on IP ranges that you are specifically authorized to test.
# Running this script may get your IP blocked/flagged by Intrusion Detection.
# May need to run as root or su to send pings.

import os, datetime, re # regex module

# Pick best Regex filter, based on how clean your input file is and how much you want to validate IPs
#IPRegex = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b') # allows any octets
#IPRegex = re.compile(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b')  # allows leading zeros
IPRegex = re.compile(r'\b(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\b') # disallow leading zeros

responses = open('ping_response.txt', 'w') # will overwrite, if file already exists
responses.write('PING responses on {:%b-%d-%Y %H:%M:%S}'.format(datetime.datetime.now()) + '\n\n')


def pingit(IP):
    #response = os.system("ping -c 1 " + IP) # verbose output for debugging
    response = os.system("ping -c 1 " + IP + " > /dev/null 2>&1") # suppress statistics
    # check the response...
    if response == 0:
        return('up')
    else:
        return('DOWN!')

# iterate through text file and if we find an IP, ping it and record response
def pingResponse():
    for line in iter(inputFile):
        if len(line) > 1:
            ip = IPRegex.search(line)
            if ip:      # if we find a valid IP on the line
                # print to screen, formatted in columns
                print('%15s' % ip.group() + '     is ' + pingit(ip.group()))
                # print to file
                responses.write('%15s' % ip.group() + '     is ' + pingit(ip.group()) + '\n')

    inputFile.close()

# Open a text file that contains IP addresses, along with random other text
try:
    #inputFile = open("sf.office.twttr.net")
    inputFile = open('iplist.txt')
    pingResponse()
except IOError:
    print('ERROR - File Does Not Exist')

responses.close()
