#!/bin/bash

sum (){
        echo "第一个参数值为$1"
        echo "第二个参数值为$2"
        sum=$[$1+$2]
        echo $sum
}
