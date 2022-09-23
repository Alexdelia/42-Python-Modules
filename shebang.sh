#!/bin/bash

[[ -z "$1" ]] && echo "usage:\n\t./shebang <file>" && exit 1

sed -i '1 i\#!/usr/bin/env python3' "$1"