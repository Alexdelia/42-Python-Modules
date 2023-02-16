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
    e='game.py'
else
    e=$1
fi

[ ! -f $e ] && printf "File $B$MAG$e$D not found\n" && exit 1

function test_res
{
    printf "$I\"$D$B$MAG${1}$D$I\"\n\tv\n\"$D$B$MAG${2}$D$I\"$D\n"
    
    if diff <(echo $3) <(echo $2) > /dev/null ; then
        printf "\t$B[${GRE}✔$D$B]$D\n"
        ((g=g+1))
    else
        printf "\t$B[${RED}✗$D$B]$D\n"
        printf "you:      $2\n"
        printf "expected: $3\n\n"
        ((b=b+1))
    fi
}

function cli_test
{
    you=$(printf "$1" | python3 | cat -e)
    me=$(printf "$2" | cat -e)
    
    test_res "$1" "$you" "$me"
}

echo

cli_test 'from game import Stark
arya = Stark("Arya")
print(arya.__dict__)
arya.print_house_words()
print(arya.is_alive)
arya.die()
print(arya.is_alive)' \
"{'first_name': 'Arya', 'is_alive': True, 'family_name': 'Stark', 'house_words': 'Winter is Coming'}
Winter is Coming
True
False
"

cli_test 'from game import Stark
arya = Stark("Arya")
print(arya.__doc__)
' \
'A class representing the Stark family. Or when bad things happen to good people.
'

#test 'failing' 'failing\n'


printf "\n\t[ $B$GRE${g}$D|$B$RED${b}$D / $B$(($g + $b))$D]"
([ $b -eq 0 ] && printf "$B$GRE") || ([ $g -eq 0 ] && printf "$B$RED") || printf "$B$YEL"
p=$(echo "$g * 100 / ($g + $b)" | bc)
printf "\t$B${p}%%$D\t$B["
[ $b -eq 0 ] && printf "${GRE}OK" || printf "${RED}KO"
printf "$D$B]$D\n"
