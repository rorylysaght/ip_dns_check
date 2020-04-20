# ip_dns_check
# Check validity and status of IP address

Open text file (iplist.txt) and iterate each line looking for IP address
Script should ignore ordinary text and comments
When we find an IP, ping it, then print response to file
Written by Rory MacLysaght rorylysaght[at]gmail[dot]com
With inspiration from these sources:
https://stackoverflow.com/questions/2953462/pinging-servers-in-python
https://www.regular-expressions.info/ip.html

# ####### ####### WARNING ####### #######
Use this ONLY on IP ranges that you are specifically authorized to test.
Running this script may get your IP blocked/flagged by Intrusion Detection systems.
May need to run as root or su to send pings via Python.
