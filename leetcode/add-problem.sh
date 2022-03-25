#!/bin/bash

if [[ -z "${1}" ]] ; then
    echo "usage: add-problem <problem-name>"
    exit 1
fi

for lang in python go rust erlang ;
do
    mkdir -p $1/$lang
done 
echo "| [${1}](https://leetcode.com/problems/${1}) | null | null | null | null |" >> README.md
