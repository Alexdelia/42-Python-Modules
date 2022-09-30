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
    e='recipe.py'
else
    e=$1
fi

[ ! -f $e ] && printf "File $B$MAG$e$D not found\n" && exit 1

function test
{
    you=$(echo "$1" | python3 $e | cat -e)
    me=$(printf "$2" | cat -e)
    
    printf "$I\"$D$B$MAG${1}$D$I\"\n\t$B$CYA| python3 $e$D\n$I\"$D$B$MAG${you}$D$I\"$D\n"
    
    _size=$C
    (( _size = _size - 8 ))
    printf "%${_size}s" ""
    
    if diff <(echo $me) <(echo $you) > /dev/null ; then
        printf "$B[${GRE}✔$D$B]$D\n"
        ((g=g+1))
    else
        printf "$B[${RED}✗$D$B]$D\n"
        printf "you:      $you\n\n"
        printf "expected: $me\n\n"
        ((b=b+1))
    fi
}

echo

test '4
5
' \
"Welcome to the Python Cookbook !
List of available options:
	1: Add a recipe
	2: Delete a recipe
	3: Print a recipe
	4: Print the cookbook
	5: Quit

Please select an option:
>> \nRecipe for sandwich:
	Ingredients list: ['ham', 'bread', 'cheese', 'tomatoes']
	To be eaten for lunch.
	Takes 10 minutes of cooking.
Recipe for cake:
	Ingredients list: ['flour', 'sugar', 'eggs']
	To be eaten for dessert.
	Takes 60 minutes of cooking.
Recipe for salad:
	Ingredients list: ['avocado', 'arugula', 'tomatoes', 'spinach']
	To be eaten for lunch.
	Takes 15 minutes of cooking.

Please select an option:
>> \nCookbook closed. Goodbye !
"

test '1
chips
potatoes
oil
salt

lunch
15
3
chips
5
' \
"Welcome to the Python Cookbook !
List of available options:
	1: Add a recipe
	2: Delete a recipe
	3: Print a recipe
	4: Print the cookbook
	5: Quit

Please select an option:
>> \nEnter a name:
Enter ingredients:
Enter a meal type:
Enter a preparation time:

Please select an option:
>> \nRecipe name:
>> \nRecipe for chips:
	Ingredients list: ['potatoes', 'oil', 'salt']
	To be eaten for lunch.
	Takes 15 minutes of cooking.

Please select an option:
>> \nCookbook closed. Goodbye !
"

test 'Hello
5
' \
"Welcome to the Python Cookbook !
List of available options:
	1: Add a recipe
	2: Delete a recipe
	3: Print a recipe
	4: Print the cookbook
	5: Quit

Please select an option:
>> \nSorry, this option does not exist.
List of available options:
	1: Add a recipe
	2: Delete a recipe
	3: Print a recipe
	4: Print the cookbook
	5: Quit

Please select an option:
>> \nCookbook closed. Goodbye !
"

#test 'failing' 'failing\n'


printf "\n\t[ $B$GRE${g}$D|$B$RED${b}$D / $B$(($g + $b))$D]"
([ $b -eq 0 ] && printf "$B$GRE") || ([ $g -eq 0 ] && printf "$B$RED") || printf "$B$YEL"
p=$(echo "$g * 100 / ($g + $b)" | bc)
printf "\t$B${p}%%$D\t$B["
[ $b -eq 0 ] && printf "${GRE}OK" || printf "${RED}KO"
printf "$D$B]$D\n"
