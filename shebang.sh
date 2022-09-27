#!/bin/bash

[[ -z "$1" ]] && printf "usage:\t\033[1m./shebang \033[35m<file>\033[0m\n" && exit 1

sed -i '1 i\#!/usr/bin/env python3\
' "$1"