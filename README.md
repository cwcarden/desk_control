[![GitHub license](https://img.shields.io/badge/Build-passing-green)](https://github.com/equineranch/desk_control)
Program updated on 12-2-2019

This is a simple flask web app that I use to control two gpio pins for my motorized standup desk.  
One pin controls up and the other controls down. This is very simple, time.sleep function is specific for my desk height presets.

To install, simply:

1.git clone https://github.com/equineranch/desk_control.git
2. cd desk_control
3. pipenv install (Will install dependencies)
4. sudo apt-get update
5. sudo apt-get -y install python-dev python3-rpi.gpio
6. Then run flask application by "flask app.py"



