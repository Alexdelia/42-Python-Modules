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
    e='whois.py'
else
    e=$1
fi

[ ! -f $e ] && printf "File $B$MAG$e$D not found\n" && exit 1

function test
{
    you=$(python3 $e $1 | cat -e)
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

test 12 "I'm Even.\n"
test 3 "I'm Odd.\n"
test 0 "I'm Zero.\n"
test 'Hello' '^[[1;31mAssertionError:^[[35m	Hello^[[0m ^[[31mis not an integer^[[0m\n'
test '12 3' '^[[1;31mAssertionError:^[[35m	2^[[0m ^[[31marguments provided, expected ^[[1;35m1^[[0m\n'
real=$(find "$(pwd)"/$e -type f)
test '' "usage:	^[[1m$real ^[[35m<number>^[[0m\n"
test '          42       ' "I'm Even.\n"
test '0000000000000000021' "I'm Odd.\n"
test '0,84' '^[[1;31mAssertionError:^[[35m	0,84^[[0m ^[[31mis not an integer^[[0m\n'
test '0.84' '^[[1;31mAssertionError:^[[35m	0.84^[[0m ^[[31mis not an integer^[[0m\n'
test 's42' '^[[1;31mAssertionError:^[[35m	s42^[[0m ^[[31mis not an integer^[[0m\n'
test '42s' '^[[1;31mAssertionError:^[[35m	42s^[[0m ^[[31mis not an integer^[[0m\n'
test '+42' "I'm Even.\n"
test '-42' "I'm Even.\n"
test '+21' "I'm Odd.\n"
test '-21' "I'm Odd.\n"
test '+0' "I'm Zero.\n"
test '-0' "I'm Zero.\n"
test '+-+42' '^[[1;31mAssertionError:^[[35m	+-+42^[[0m ^[[31mis not an integer^[[0m\n'
test '++42' '^[[1;31mAssertionError:^[[35m	++42^[[0m ^[[31mis not an integer^[[0m\n'
test '--42' '^[[1;31mAssertionError:^[[35m	--42^[[0m ^[[31mis not an integer^[[0m\n'

#test 'failing' 'failing\n'


printf "\n\t[ $B$GRE${g}$D|$B$RED${b}$D / $B$(($g + $b))$D]"
([ $b -eq 0 ] && printf "$B$GRE") || ([ $g -eq 0 ] && printf "$B$RED") || printf "$B$YEL"
p=$(echo "$g * 100 / ($g + $b)" | bc)
printf "\t$B${p}%%$D\t$B["
[ $b -eq 0 ] && printf "${GRE}OK" || printf "${RED}KO"
printf "$D$B]$D\n"
