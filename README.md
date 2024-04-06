# log-parser
Checks suspicious activities in Netwok log example

# Output expected
Log lines from log file:

['192.168.0.1:22 >> 192.168.55.22:443', '192.168.33.1:80 >> 192.168.55.22:80', '192.168.35.1:80 >> 192.168.55.22:53', '192.168.0.2:6738 >> 192.168.55.22:443', '192.168.33.1:80 >> 192.168.55.23:80', '192.168.35.1:80 >> 192.168.55.22:53', '192.168.0.55:22 >> 192.168.55.42:443', '192.168.0.55:553 >> 192.168.55.45:443', '192.168.0.55:553 >> 192.168.55.45:80']

There is a suspicious activity from 192.168.0.55 IP address

This source IP 192.168.0.55:553 is trying to access 443 and 80 ports