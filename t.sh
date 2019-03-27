#!/bin/sh

echo "-- pid:$$ start --" `date '+%y/%m/%d %H:%M:%S'`

/Users/mn/.pyenv/shims/python /Users/work/futaba/FutaWatcher/src/main.py

echo "-- pid:$$  end  --" `date '+%y/%m/%d %H:%M:%S'`
