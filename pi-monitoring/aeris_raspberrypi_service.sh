
[Unit]
Description=Aeris iperf test service

[Service]
WorkingDirectory=/home/pi/Aeris-raspberrypi
ExecStart=test_ping.sh

[Install]
WantedBy=multi-user.target
