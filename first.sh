#!/bin/sh

mkdir Archives
python ./gen.py
echo "alias tblock = \"python ~/.timeblock/main.py\"" >> ~/.bashrc
