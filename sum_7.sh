#!/bin/bash
sum=0
for ((num=1; num<=300; num++))
do
    if [ $((num % 7)) -eq 0 ]; then
        sum=$((sum + num))
    fi
done
echo "和为：$sum"
