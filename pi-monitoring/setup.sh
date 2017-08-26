#check for root!
if [[ $EUID -ne 0 ]]; then
	echo "This script must be run as root!"
	echo "run with sudo ./setup.sh"
	exit 1
fi
new() {
    clear
    echo "doing full system update, this will take a while"
    echo "sit back and have a coffee"
    sleep 2
    #install dependencies
    sudo apt -y update
    sudo apt -y upgrade
    echo "installing dependencies"
    sudo apt install -y vim samba libiperf0 gcc wvdial
    echo "cloning iperf"
    git clone https://github.com/UKSFM99/iperf
    cd iperf
    ./configure && make && sudo make install
    cd ..
    sudo apt remove -y libiperf0
    update
}

update(){
    echo ""
    echo ""
    clear
    echo "Modem Config Setup:"
    echo "Which type of modem do you have?"
    echo "t) telus LTE Modem"
    echo "c) sprint CDMA Modem"
    skip_apn=false
    while true; do
        read -p "" tc
        case $tc in
            [Tt]*	) echo "copying config across"; sudo cp etc/lte.conf /etc/wvdial.conf; break;;
            [Cc]*	) echo "copying config across";skip_apn=true; sudo cp etc/cdma.conf /etc/wvdial.conf; break;;
            *	) echo "invalid answer!, enter again";;
        esac
    done
    clear
    hostn=$(cat /etc/hostname)
    echo "enter Pi name, followed by [Enter]"
    read hostname
    sudo echo $hostname > /etc/hostname
    sudo sed -i "s/$hostn/$hostname/g" /etc/hosts
    apn=''
    if [ "$skip_apn" = true ]
    then
        apn="NA"
    else
        echo "enter APN to be used again, followed by [Enter]"
        read apn
        sudo sed -i "s/NANA/$apn/g" /etc/wvdial.conf
    fi

    echo "enter testlabel eg:GSM-Global-USDev_UKGGSN, followed by [Enter] "
    read testlabel
    mdn=''
    if [ "$skip_apn" = true ]
    then
        mdn="NA"
    else
        echo "enter SIM mdn number, if not know enter 123456789, followed by [Enter]"
        read mdn
    fi
    printf "test_addr=13.59.245.239\nsize=1400\napn=${apn}\nmdm=${mdn}\nhostname=${hostname}\ntestlabel=${testlabel}" > /home/pi/config
    #install systemd service
    cp aeris_raspberrypi.service /etc/systemd/system/aeris_raspberrypi.service
    echo ""
    echo ""
    echo ""
    echo "### IMPORTANT ###"
    echo "run sudo test_ping.sh"
    echo "Developed by Ashcon Mohseninia 2017"
    echo "Rebooting system now!"
    systemctl enable aeris_raspberrypi.service
    sleep 2
    reboot
}
clear
echo "is this a fresh install or update?"
echo "U) update - dont recompile iperf"
echo "N) new - do everything"
while true; do
    read -p "" un
    case $un in
        [Uu]*   ) update; break;;
        [Nn]*   ) new; break;;
        *   ) echo "invalid choice!, enter again";;
    esac
done
