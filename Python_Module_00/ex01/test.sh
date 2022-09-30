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
    e='count.py'
else
    e=$1
fi

[ ! -f $e ] && printf "File $B$MAG$e$D not found\n" && exit 1

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
    you=$(echo "$3" | python3 $e "$1" | cat -e)
    me=$(printf "$2" | cat -e)
    
    [ $# -eq 3 ] && printf "${I}piping: \"$D$B$CYA$3$D$I\"\n"
    
    test_res "$1" "$you" "$me"
}

function cli_test
{
    you=$(printf "$1" | python3 | cat -e)
    me=$(printf "$2" | cat -e)
    
    test_res "$1" "$you" "$me"
}

echo

test 'Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.' \
'The text contains 143 character(s):
- 2 upper letter(s)
- 113 lower letter(s)
- 4 punctuation mark(s)
- 18 space(s)
'
test "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace." \
'The text contains 234 character(s):
- 5 upper letter(s)
- 187 lower letter(s)
- 8 punctuation mark(s)
- 30 space(s)
'
test '' 'What is the text to analyse?
>> The text contains 12 character(s):
- 1 upper letter(s)
- 9 lower letter(s)
- 1 punctuation mark(s)
- 1 space(s)
' \
'Hello world!'

printf "\n$B$CYA\tcli test:$D\n"

cli_test "from count import text_analyzer
text_analyzer(\"Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.\")" \
'The text contains 143 character(s):
- 2 upper letter(s)
- 113 lower letter(s)
- 4 punctuation mark(s)
- 18 space(s)
'
cli_test "from count import text_analyzer
text_analyzer(\"Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.\")" \
'The text contains 234 character(s):
- 5 upper letter(s)
- 187 lower letter(s)
- 8 punctuation mark(s)
- 30 space(s)
'

cli_test "from count import text_analyzer
text_analyzer(42)" \
'^[[1;31mAssertionError:^[[35m	42^[[0m ^[[31mis not a string^[[0m\n'

cli_test "from count import text_analyzer
print(text_analyzer.__doc__)" \
'\t
	This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text.
\n\t'

#test 'failing' 'failing\n'


printf "\n\t[ $B$GRE${g}$D|$B$RED${b}$D / $B$(($g + $b))$D]"
([ $b -eq 0 ] && printf "$B$GRE") || ([ $g -eq 0 ] && printf "$B$RED") || printf "$B$YEL"
p=$(echo "$g * 100 / ($g + $b)" | bc)
printf "\t$B${p}%%$D\t$B["
[ $b -eq 0 ] && printf "${GRE}OK" || printf "${RED}KO"
printf "$D$B]$D\n"
