#!/bin/sh

python gen.py
echo "alias tblock=\"python ~/.timeblock/main.py\"" >> ~/.bashrc
source ~/.bashrc
