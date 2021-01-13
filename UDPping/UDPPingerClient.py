import sys, time
from socket import *

# Get the server hostname and port as command line arguments
argv = sys.argv                      
host = argv[1]
port = argv[2]
timeout = 1 # in second

# Create UDP client socket
# Note the use of SOCK_DGRAM for UDP datagram packet
clientsocket = socket(AF_INET, SOCK_DGRAM)
# Set socket timeout as 1 second
clientsocket.settimeout(timeout)

# Command line argument is a string, change the port into integer
port = int(port)  
# Sequence number of the ping message
ptime = 0  

maxRTT = 0
minRTT = 0
avgRTT = 0
sumRTT = 0
loss = 0

# Ping for 10 times
while ptime < 10: 
	ptime += 1
	# Format the message to be sent
	data = "Ping " + str(ptime) + " " + time.asctime()
    
	try:
	# Sent time
		RTTb = time.time()
	# Send the UDP packet with the ping message
		clientsocket.sendto(data.encode(),(host, port))
	# Receive the server response
		message, address = clientsocket.recvfrom(1024)  
	# Received time
		RTTa = time.time()
	# Round trip time is the difference between sent and received time
		RTT = (RTTa - RTTb)*1000
		maxRTT = max(RTT, maxRTT)
		minRTT = min(RTT, minRTT)
		sumRTT = sumRTT + RTT
	# Display the server response as an output
		print("Reply from " + address[0] + ": " + message.decode() + ", " + "RTT = %.4fms" % (RTT))       
	except:
		# Server does not response
	# Assume the packet is lost
		print ("Request timed out.")
		loss += 1
		continue

print("\n----------Statistical information:----------")
print("Loss percent = {:.2%}".format(loss/10))
print("minRTT = %.4fms, maxRTT = %.4fms, avgRTT = %.4fms" %(minRTT, maxRTT, sumRTT/10))
# Close the client socket
clientsocket.close()
 




