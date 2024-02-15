@echo off
title data
.venv\scripts\activate
echo make sure you have pyserial installed! (pip install pyserial)
echo data coming in soon -> press enter to start data transfer (will be around 20 seconds)
python main.py
echo done, please exit :D and find data.csv somewhere in the directory!
python visualize.py
exit
