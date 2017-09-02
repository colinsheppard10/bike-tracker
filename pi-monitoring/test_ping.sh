#!/usr/bin/env bash
if [[ $EUID -ne 0 ]]; then
	echo "this script must be run as root!"
	echo "run with sudo ./test_ping.sh"
	exit 1
fi



test_addr=13.59.104.218
size=$(cat /home/pi/config | grep size | cut -d '=' -f2)
apn=$(cat /home/pi/config | grep apn | cut -d '=' -f2)
mdn=$(cat /home/pi/config | grep mdm| cut -d '=' -f2)
hostname=$(cat /etc/hostname)
testlabel=$(cat /home/pi/config | grep testlabel | cut -d '=' -f2)
id=$(cat /etc/hostname | cut -c 8-)
base_port=8000
port_num=$(($id + $base_port))
clear
#Add test_addr IP to use modem not ethernet or wlan
#eth1 = Modem, eth0 = ethernet, wlan0 = WIFI, ppp0 = modem
while true; do
    date=$(date)
	#switch APN's
	pkill wvdial
    printf "\n NEW TEST BEGIN AT $date ! \n" >> /home/pi/aerislog.txt
	sleep 100
	wvdial 3gconnect >>/home/pi/aerislog.txt 2>&1 &
	echo waiting 5 mins
	sleep 200 #5 mins sleep time
	ip=$(ifconfig ppp0 | grep 'inet addr:' | cut -d ':' -f2 | cut -d ' ' -f 1)
	ip_srv=$(ifconfig ppp0 | grep 'P-t-P:' | cut -d ':' -f3 | cut -d ' ' -f 1)
	if [ -z "$ip" ] #if IP is null then dont continue testing
	then
		printf "ERROR: device took too long to get IP \n" >> /home/pi/aerislog.txt 
		python /home/pi/Aeris-raspberrypi/result_parse.py "$mdm" "$hostname" "$apn" "NULL" "ERROR" "101" "$testlabel" >> /home/pi/aerislog.txt
	else
		#check server IP first. No point trying to waste 20 packets if we can check first with 1 packet
		ping -c 1 ${test_addr} &> /dev/null
		if [ "$?" = 0 ]
		then
			printf "added IP to routetable for ppp0 \n" >> /home/pi/aerislog.txt
			ip route add ${test_addr} dev ppp0
            printf "testing latency to server \n" >> /home/pi/aerislog.txt
			latency=$(ping -c 4 ${test_addr} -I ppp0 | tail -1| awk '{print $4}' | cut -d '/' -f 2)
			echo "average latency = $latency ms" >> /home/pi/aerislog.txt
			printf "testing with Iperf3 \n" >> /home/pi/aerislog.txt
			#test 1: Normal mode
			cmd1=$(iperf3 -b 10K -t 10 -u -y -l 1400B -c ${test_addr} -p ${port_num})
            echo ${cmd1} >> /home/pi/aerislog.txt
            res1=$(echo ${cmd1} | grep % | grep receiver)
			#Test 2: Reverse mode
			cmd2=$(iperf3 -R -b 10K -t 10 -u -y -l 1400B -c ${test_addr} -p ${port_num})
            echo ${cmd2} >> /home/pi/aerislog.txt
            res2=$(echo ${cmd2} | grep % | grep receiver)
			#parse both summery outputs into python script
			python /home/pi/Aeris-raspberrypi/result_parse.py "$mdm" "$hostname" "$apn" "$latency" "$res1" "$res2" "$size" "$testlabel" "$ip" "$ip_srv">> /home/pi/aerislog.txt
		else
			printf "ERROR: test address is not valid or responding \n" >>/home/pi/aerislog.txt
			python /home/pi/Aeris-raspberrypi/result_parse.py "$mdm" "$hostname" "$apn" "$latency" "ERROR" "404" "$testlabel" "$ip" "$ip_srv" >> /home/pi/aerislog.txt
		fi
	fi

done
