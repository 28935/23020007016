#!/bin/bash

read -p "请输入一个文件路径：" filename

if [ -e $filename ];then
        echo "OK"
else
        echo "No such file"
fi
