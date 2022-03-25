#!/bin/bash

if [[ -z "${1}" ]] ; then
    echo "usage: add-problem <problem-name>"
    exit 1
fi

mkdir -p $1
echo "| [${1}](https://leetcode.com/problems/${1}) | null | null | null | null |" >> README.md
