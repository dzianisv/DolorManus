#!/bin/sh
sudo apt-get install python-dev libusb-1.0-0-dev libudev-dev
pip install hidapi
pip install git+https://github.com/andrewda/xarmservocontroller.git#subdirectory=Python
echo 'SUBSYSTEM=="usb", ATTR{idVendor}=="0483", ATTR{idProduct}=="5750", MODE="0660", GROUP="plugdev"' | sudo tee /usr/lib/udev/rules.d/99-xarm.rules
echo 'SUBSYSTEM=="usb", ATTR{idVendor}=="0483", ATTR{idProduct}=="5750", MODE="0660", GROUP="plugdev"' | sudo tee /etc/udev/rules.d/99-xarm.rules
sudo gpasswd -a $USER plugdev
sudo udevadm control --reload-rules && udevadm trigger
