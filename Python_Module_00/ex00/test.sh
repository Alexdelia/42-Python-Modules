#!/bin/bash

g=0
b=0

C=(`tput cols`)

B='\033[1m'
I='\033[3m'
RED='\033[31m'
GRE='\033[32m'
YEL='\033[33m'
MAG='\033[35m'
CYA='\033[36m'
D='\033[0m'

if [ $# -eq 0 ]; then
    e='exec.py'
else
    e=$1
fi

[ ! -f $e ] && printf "File $B$MAG$e$D not found\n" && exit 1

function test
{
    you=$(python $e $1 | cat -e)
    me=$(printf "$2" | cat -e)
    
    _size=${#1}
    (( _size = _size - 20 ))
    printf "$I\"$D$B$MAG${1}$D$I\"%*s-> \"$D$B$MAG${you}$D$I\"$D" "$_size"
    
    _size=$C
    (( _size = _size - (${#you} + 42) ))
    printf "%${_size}s" ""
    
    if diff <(echo $me) <(echo $you) > /dev/null ; then
        printf "$B[${GRE}✔$D$B]$D\n"
        ((g=g+1))
    else
        printf "$B[${RED}✗$D$B]$D\n"
        printf "you:      $you\n"
        printf "expected: $me\n\n"
        ((b=b+1))
    fi
}

echo

test 'Hello World!' '!DLROw OLLEh\n'
test 'Hello my Friend' 'DNEIRf YM OLLEh\n'
test '' ''
test 'basic' 'CISAB\n'
test 'BASIC' 'cisab\n'
test 'CISAB' 'basic\n'
test 'cisab' 'BASIC\n'
test '0123456789' '9876543210\n'
test ' a1  a2    a3      ' '3A 2A 1A\n'
test ' !\()*+,-./:;' ';:/.-,+*)(\!$'
test '<=>?@^_`{|}~/' '/~}|{`_^@?>=<$'

#test 'failing' 'failing\n'


printf "\n\t[ $B$GRE${g}$D|$B$RED${b}$D / $B$(($g + $b))$D]"
([ $b -eq 0 ] && printf "$B$GRE") || ([ $g -eq 0 ] && printf "$B$RED") || printf "$B$YEL"
p=$(echo "$g * 100 / ($g + $b)" | bc)
printf "\t$B${p}%%$D\t$B["
[ $b -eq 0 ] && printf "${GRE}OK" || printf "${RED}KO"
printf "$D$B]$D\n"
