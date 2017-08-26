import sys
import re
import json
import socket
from time import gmtime, strftime

def get_packet_loss_packets(str_source,packets,is_reversed):
	to_find="/"
	str_array=str_source.split(' ')
	for x in str_array:
		if to_find in x:
			temp=x.split('/')
	try:
		print(temp[0])
		print(temp[1])
		#return (temp[0],temp[1])
		return (int(temp[0]),int(temp[1]),int(packet_loss_percentage(int(temp[0]),int(temp[1]))))
	except NameError:
		print("iperf sent invalid string!, ignoring")
		return(0,0,0)

def packet_loss_percentage(dropped,sent):
	percent = int(100*(float(dropped)/float(sent)))
	print(percent)
	return percent
def parse_error(err_code,host,apn,ip,testlabel,mdm):
	if err_code == 101:
		push_json(0,host,testlabel,apn,None,0,0,"Device took too long to get IP address",0,0,mdm,0,0,"NA","NA")
	elif err_code == 404:
		push_json(0,host,testlabel,apn,ip,0,0,"IPerf server did not respond",0,0,mdm,0,0,"NA","NA")
	else:
		print ("unknown error code!!")
	return

def push_json(size,hostname,testlabel,apn,latency,packet_loss_norm,packet_loss_rev,msg,num_packets_forward,num_packets_reverse,mdm,percent_lost_forward,percent_lost_reverse,ip,ip_srv):
	str_time = strftime("%Y-%m-%d %H:%M:%S.", gmtime())
	data = {'time '+hostname:	str_time,'testlabel '+hostname:testlabel,'SIM MDM '+hostname:mdm,'SIM IP '+hostname:ip,'SERVER IP '+hostname:ip_srv,'Latency '+hostname:latency,'APN '+hostname:apn,'UDP packet size '+hostname:size,'forward packet loss '+hostname:int(packet_loss_norm),'reverse packet loss '+hostname:int(packet_loss_rev),'packets sent forward '+hostname:int(num_packets_forward),'packets sent reverse '+hostname:int(num_packets_reverse),'percentage loss forwards '+hostname:int(percent_lost_forward),'percentage loss reverse '+hostname:int(percent_lost_reverse),'error message ':msg}
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#replace locahost with IP of logstash server and also port
	sock.connect(('52.35.206.249',9600))
	print(json.dumps(data).encode('utf8'))
	sock.send(json.dumps(data).encode('utf8'))
	return

#SYSTEM ARGS:
#arg0=mdm number
#arg1=hostname
#arg2=apn
#arg3=latency
#arg4=result forward/error label
#arg5=result backward/error status code
#arg6=packet size
#arg7=testlabel
arg0=sys.argv[1]
arg1=sys.argv[2]
arg2=sys.argv[3]
arg3=sys.argv[4]
arg4=sys.argv[5]
arg5=sys.argv[6]
arg6=sys.argv[7]
if arg4 == "ERROR":
	parse_error(int(arg5),arg1,arg2,arg3,arg6,arg0)
else:
	arg7=sys.argv[8]
	arg3=arg3.rstrip(" ms")
	arg3=float(arg3)
	arg8=sys.argv[9]
	arg9=sys.argv[10]
	#True to indicate this is reversed ie: -R in iperf3
	forward = get_packet_loss_packets(arg4,arg5,False)
	backwards = get_packet_loss_packets(arg5,arg5,True)
	push_json(int(arg6),arg1,arg7,arg2,arg3,int(forward[0]),int(backwards[0]),None,int(forward[1]),int(backwards[1]),arg0,int(forward[2]),int(backwards[2]),arg8,arg9)
