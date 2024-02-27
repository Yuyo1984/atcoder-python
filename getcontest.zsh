#!/bin/zsh

echo 解きたいabcの番号の範囲をスペースで区切って指定してください:

read n1 n2

for i in $(seq -w $n1 $n2)
do
  acc new abc"$i"
done
