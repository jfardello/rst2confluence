#!/bin/sh
# Runs rst2confluence.py on all .rst files in test/ and compares them
# to the expected output (.exp)
if [ $# -eq 0 ]; then
    files=tests/rst/*.rst
else
    files="$*"
fi

mkdir -p tests/tmp

for i in $files; do
    echo -n Testing $i
    i=`basename $i`
    expFile="tests/exp/$i.exp"
    outFile="tests/tmp/$i.out"
    diffFile="tests/tmp/$i.diff"
    rst2confluence "tests/rst/$i"  "$outFile"
    if [ $? -ne 0 ]; then
        echo -e "\033[00;31merror running rst2confluence\033[00m"
        break;
    fi

    if [ ! -f "$expFile" ]; then
        expFile=/dev/null
    fi

    diff -u "$expFile" "$outFile" > "$diffFile"
    if [ "$?" -ne "0" ]; then
        echo -e " \033[00;31merror\033[00m"
        cat "$diffFile" | colordiff
        break;
    else
        #all fine
        echo -e " \033[00;32mok\033[00m"
        rm "$outFile"
        rm "$diffFile"
    fi
done
