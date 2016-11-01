#! /bin/bash
cd "$(dirname "$0")"
while true
do
printf « Start DAB »
python3 discordab.py
printf " End of DAB »
sleep 3
done