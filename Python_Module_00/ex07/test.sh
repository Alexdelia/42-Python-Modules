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
    e='filterwords.py'
else
    e=$1
fi

[ ! -f $e ] && printf "File $B$MAG$e$D not found\n" && exit 1

function test
{
    you=$(python3 $e "$1" $2 | cat -e)
    me=$(printf "$3" | cat -e)
    
    _size=${#1}
    (( _size = _size + ${#2} - 20 ))
    printf "$I\"$D$B$MAG'${1}' ${2}$D$I\"%*s-> \"$D$B$MAG${you}$D$I\"$D" "$_size"
    
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

test 'Hello, my friend' '3' "['Hello', 'friend']\n"
test 'Hello, my friend' '10' "[]\n"
test 'A robot must protect its own existence as long as such protection does not conflict with the First or Second Law' '6' \
"['protect', 'existence', 'protection', 'conflict']\n"
test 'Hello' 'World' "ERROR\n"
test 'Hello, my friend' '3 4' "ERROR\n"
test '3' 'Hello, my friend' "ERROR\n"
test '' '' "ERROR\n"
test 'Hello, my friend' '0' "['Hello', 'my', 'friend']\n"
test 'Hello, my friend' '-1' "['Hello', 'my', 'friend']\n"

#test 'failing' 'failing\n'


printf "\n\t[ $B$GRE${g}$D|$B$RED${b}$D / $B$(($g + $b))$D]"
([ $b -eq 0 ] && printf "$B$GRE") || ([ $g -eq 0 ] && printf "$B$RED") || printf "$B$YEL"
p=$(echo "$g * 100 / ($g + $b)" | bc)
printf "\t$B${p}%%$D\t$B["
[ $b -eq 0 ] && printf "${GRE}OK" || printf "${RED}KO"
printf "$D$B]$D\n"
