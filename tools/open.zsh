#!/bin/zsh

echo -n A問題のurlを開きたいabcの番号の範囲を半角スペースで区切って指定してください:

read n1 n2

for i in {$n1..$n2};
do
  open `acc url abc"$i" abc"$i"_a`
done
