# Aeris Raspberry Pi project

## Instructions
1. Run setup.sh in directory - this will prompt you to modify your wvdial.conf to enter the APN details (only on GSM/LTE)
2. Then modify the config file in user directory (~/config) in order to enter the piname as hostname and the APN details. If using CDMA then enter NA as APN
3. Now modify the Pi hostname in samaba in order to allow SSH connections by hostname
4. run sudo raspiconfig -> advanced -> allow SSH connections (yes) in order to allow SSH to Pi
5. then run sudo ./test_ping.sh to start script
