#!/bin/bash
history_file=~/.bash_history
top_commands=$(cat "$history_file" | awk '{print $1}' | sort | uniq -c | sort -nr | head -n 5)
echo "最常使用的5个命令："
echo "$top_commands"
