#!/bin/sh 
# script to execute file
cd "$(dirname "$0")"
echo "make sure you have pyserial installed! (pip install pyserial)"
echo "----RUNNING SCRIPTS----"
echo "~~~~~This may take up to ~20 seconds to offload~~~~~"
python "$(pwd)/main.py"
echo "----DONE----"
echo "look for data.csv in your directory :D"