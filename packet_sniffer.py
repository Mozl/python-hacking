# open scapy
sudo ./run_scapy

# see all interfaces for machine, like wifi, bluetooth etc
conf.iface

# looks at your wifi interface, looks at 15 packets
sniffer_ = sniff(iface='en0',count=15)
sniffer_.show()

# look at specific packet, shows source and destination
sniffer_[4].show()

# get the IP address of a website eg. google.com
ping google.com

# listens for you connecting to the host on port 443 then returns summary. Prn runs for each packet
sniffer = sniff(filter="port 443 and host 18.203.216.206",count=15,prn=lambda x:x.summary())

# lambda functions are small anonymous functions
# A lambda function can take any number of arguments, but can only have one expression
# Syntax: lambda arguments : expression

# can write the sniff session to file wrpcap (write packet). (name of the file, what to write)
wrpcap("dgt.cap",sniffer)

#read the packets
rcpcap('dgt.cap')

#sending and receiving packets

packet_t = IP(dst="dgtsec.com")/ICMP()/"You are not secured"

resp = sr(packet_t)
resp.summary()




