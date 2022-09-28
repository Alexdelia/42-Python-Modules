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

function test_res
{
    _size=${#1}
    (( _size = _size - 20 ))
    printf "$I\"$D$B$MAG${1}$D$I\"%*s-> \"$D$B$MAG${2}$D$I\"$D" "$_size"
    
    _size=$C
    (( _size = _size - (${#2} + 42) ))
    printf "%${_size}s" ""
    
    if diff <(echo $3) <(echo $2) > /dev/null ; then
        printf "$B[${GRE}✔$D$B]$D\n"
        ((g=g+1))
    else
        printf "$B[${RED}✗$D$B]$D\n"
        printf "you:      $2\n"
        printf "expected: $3\n\n"
        ((b=b+1))
    fi
}

function test
{
    printf "$B${CYA}$1$D\n"
    
    [ ! -f $1 ] && printf "$B[${RED}✗$D$B]$D\t${RED}File $B$MAG$1$D$RED not found$D\n" && ((b=b+1)) && return
    
    you=$(python $1 $2 | cat -e)
    me=$(printf -- "$3" | cat -e)
    
    test_res "$2" "$you" "$me"
}

function test_wc
{
    printf "$B${CYA}$1 wc$D\n"
    
    [ ! -f $1 ] && printf "$B[${RED}✗$D$B]$D\t${RED}File $B$MAG$1$D$RED not found$D\n" && ((b=b+1)) && return
    
    you=$(python $1 $2 | wc -c)
    me=$3
    
    test_res "$2" "$you" "$me"
}

echo

test "${e}/kata00.py" '' 'The 3 numbers are: 19, 42, 21\n'
test "${e}/kata01.py" '' \
'Python was created by Guido van Rossum
Ruby was created by Yukihiro Matsumoto
PHP was created by Rasmus Lerdorf
'
test "${e}/kata02.py" '' '09/25/2019 03:30\n'
test_wc "${e}/kata02.py" '' '17'
test "${e}/kata03.py" '' '--------------------------The right format'
test_wc "${e}/kata03.py" '' '42'
test "${e}/kata04.py" '' '42 - The meaning of life, the universe and everything'


#test 'failing' 'failing\n'


printf "\n\t[ $B$GRE${g}$D|$B$RED${b}$D / $B$(($g + $b))$D]"
([ $b -eq 0 ] && printf "$B$GRE") || ([ $g -eq 0 ] && printf "$B$RED") || printf "$B$YEL"
p=$(echo "$g * 100 / ($g + $b)" | bc)
printf "\t$B${p}%%$D\t$B["
[ $b -eq 0 ] && printf "${GRE}OK" || printf "${RED}KO"
printf "$D$B]$D\n"
