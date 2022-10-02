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
    e='operation.py'
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

test '10 3' \
'^[[1mSum:^[[0m		^[[1;35m13^[[0m
^[[1mDifference:^[[0m	^[[1;35m7^[[0m
^[[1mProduct:^[[0m	^[[1;35m30^[[0m
^[[1mQuotient:^[[0m	^[[1;35m3.3333333333333335^[[0m
^[[1mRemainder:^[[0m	^[[1;35m1^[[0m
'
test '42 10' \
'^[[1mSum:^[[0m		^[[1;35m52^[[0m
^[[1mDifference:^[[0m	^[[1;35m32^[[0m
^[[1mProduct:^[[0m	^[[1;35m420^[[0m
^[[1mQuotient:^[[0m	^[[1;35m4.2^[[0m
^[[1mRemainder:^[[0m	^[[1;35m2^[[0m
'
test '1 0' \
'^[[1mSum:^[[0m		^[[1;35m1^[[0m
^[[1mDifference:^[[0m	^[[1;35m1^[[0m
^[[1mProduct:^[[0m	^[[1;35m0^[[0m
^[[1mQuotient:^[[0m	^[[1;31mERROR^[[0m	^[[31m(division by zero)^[[0m
^[[1mRemainder:^[[0m	^[[1;31mERROR^[[0m	^[[31m(modulo by zero)^[[0m
'
test '0 1' \
'^[[1mSum:^[[0m		^[[1;35m1^[[0m
^[[1mDifference:^[[0m	^[[1;35m-1^[[0m
^[[1mProduct:^[[0m	^[[1;35m0^[[0m
^[[1mQuotient:^[[0m	^[[1;35m0.0^[[0m
^[[1mRemainder:^[[0m	^[[1;35m0^[[0m
'
real=$(find "$(pwd)"/$e -type f)
test '' "usage:	^[[1m$real ^[[35m<number1> <number2>^[[0m\n"
test '12 10 5' '^[[1;31mAssertionError:^[[35m	3^[[0m ^[[31marguments provided, expected ^[[1;35m2^[[0m\n'
test '42' '^[[1;31mAssertionError:^[[35m	1^[[0m ^[[31marguments provided, expected ^[[1;35m2^[[0m\n'
test 'one two' '^[[1;31mAssertionError:^[[35m	one^[[0m ^[[31mis not an integer^[[0m\n'
test '42 two' '^[[1;31mAssertionError:^[[35m	two^[[0m ^[[31mis not an integer^[[0m\n'
test '-42 10' \
'^[[1mSum:^[[0m		^[[1;35m-32^[[0m
^[[1mDifference:^[[0m	^[[1;35m-52^[[0m
^[[1mProduct:^[[0m	^[[1;35m-420^[[0m
^[[1mQuotient:^[[0m	^[[1;35m-4.2^[[0m
^[[1mRemainder:^[[0m	^[[1;35m8^[[0m
'

#test 'failing' 'failing\n'


printf "\n\t[ $B$GRE${g}$D|$B$RED${b}$D / $B$(($g + $b))$D]"
([ $b -eq 0 ] && printf "$B$GRE") || ([ $g -eq 0 ] && printf "$B$RED") || printf "$B$YEL"
p=$(echo "$g * 100 / ($g + $b)" | bc)
printf "\t$B${p}%%$D\t$B["
[ $b -eq 0 ] && printf "${GRE}OK" || printf "${RED}KO"
printf "$D$B]$D\n"
