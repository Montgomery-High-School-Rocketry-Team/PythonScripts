#!/bin/sh 
# script to execute file
cd "$(dirname "$0")"
echo "----RUNNING SCRIPTS----"

python "$(pwd)/main.py"
echo "----DONE----"
echo "look for data.csv in your directory :D"