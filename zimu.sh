#!/bin/bash
content="dwadscfbfgynhjythgfseaszxcfvbgnhjmkilolpoiujhytgrewasxdcfvghyujjklplmlpqeazxcvhjuytredfghjkljhbgvbhjhgfdsawqertyhgbnmbvcxzxdsxczsqwe"
sort=$(echo "$content" | grep -o . | grep -v '[. ]' | sort | uniq -c | sort -rn)
echo "按字母出现频率降序排序："
echo "$sort"
