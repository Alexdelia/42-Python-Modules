#!/bin/bash

t='main.py'

if [ $# -eq 0 ]; then
    e='loading.py'
else
    e=$1
fi

[ ! -f $e ] && printf "File $B$MAG$e$D not found\n" && exit 1
[ ! -f $t ] && printf "File $B$MAG$t$D not found\n" && exit 1

python3 $t
