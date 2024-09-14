#!/bin/bash

if [ $# != 2 ]; then
  echo "Usage: ./setup.sh Year Day"
  exit
fi

echo "Setting up for new problem..."

Year=$1
Day=$2

if [ ! -d "$Year" ]; then
  mkdir "$Year"
fi

if [ ! -d "$Year/Day $Day" ]; then
  mkdir "$Year/Day $Day"
fi

cd "$Year" || exit
cd "Day $Day" || exit

touch "solution.py"
touch "input.txt"

sleep 0.2
echo "Happy, coding!"