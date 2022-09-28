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
    e='.'
else
    e=$1
fi

#[ ! -f $e ] && printf "File $B$MAG$e$D not found\n" && exit 1

function test
{
    printf "$B${CYA}$1$D\n"
    
    you=$(python $1 $2 | cat -e)
    me=$(printf "$3" | cat -e)
    
    _size=${#2}
    (( _size = _size - 20 ))
    printf "$I\"$D$B$MAG${2}$D$I\"%*s-> \"$D$B$MAG${you}$D$I\"$D" "$_size"
    
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

test "${e}/kata00.py" '' 'The 3 numbers are: 19, 42, 21\n'
test "${e}/kata01.py" '' \
'Python was created by Guido van Rossum
Ruby was created by Yukihiro Matsumoto
PHP was created by Rasmus Lerdorf
'

#test 'failing' 'failing\n'


printf "\n\t[ $B$GRE${g}$D|$B$RED${b}$D / $B$(($g + $b))$D]"
([ $b -eq 0 ] && printf "$B$GRE") || ([ $g -eq 0 ] && printf "$B$RED") || printf "$B$YEL"
p=$(echo "$g * 100 / ($g + $b)" | bc)
printf "\t$B${p}%%$D\t$B["
[ $b -eq 0 ] && printf "${GRE}OK" || printf "${RED}KO"
printf "$D$B]$D\n"
