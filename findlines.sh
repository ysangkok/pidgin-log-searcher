#!/usr/bin/env zsh
#echo 1-1-1.1.html:2:hello
#exit

export LANG=da_DK.UTF-8
unicodeblock=$(A=880; while (( A++ < 1023 )) { C=$(printf %04x $A); echo -n \\u$C; })
A="$(echo -n $unicodeblock | sed -re 's/(.)/\1|/g' )" # make regex
B="$(echo -n $A | head -c $(expr $(echo -e $A | wc -c) - 2))" # strip last |
cd ~/.purple/logs/jabber/ysangkok@gmail.com/vogelnatalia970@gmail.com/
for i in *; do
	grep -inH --color=never -E $B $i #| sed -e 's#<[^>]*>##g'
done
