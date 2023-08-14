ls  /ts/pod/px/px*/config/p*fng.conf | while read -r f; do grep -l "BOND" "$f"; done

du -a | cut -f2 | grep ".conf" | while read -r f; do grep -l "NA_INST_BBG" "$f";done


while sleep 1; do echo "Hi"; done

From <https://unix.stackexchange.com/questions/10646/repeat-a-unix-command-every-x-seconds-forever> 



grep "Error Out of Memory" /ts/log/tscmf/* | cut -d" " -f 10 | while read f; do grep "UPDATED.*pricingNumber.*$f.*errorCode" /ts/log/tscmf/bciwfprx.log.20190909_114624; done | cut -d" " -f12 | sort | uniq 


p293:op1> grep  "Error Out of Memory" /ts/log/tscmf/*  | cut -d" " -f 10  | while read f; do grep "UPDATED.*pricingNumber.*$f.*errorCode" /ts/log/tscmf/*; done | sed -n 's/^.*pricingNumber \[\([0-9]*\).*/Px: \1/p' | sort | uniq
Px: 1824
Px: 2054
Px: 3633
Px: 3813
Px: 4495
Px: 961

Search for all the BCHQUOT sessions

 ls  /ts/pod/px/px*/config/p*fng.conf | while read -r f; do grep "BCHQ" "$f" && echo $f ; done | sed 'N;s/\n/ /' | sed -n 's/^.*TargetCompId=\([(A-Z)(0-9)]*[^\s]\).*px\([0-9]*[^\/]\).*/Session: \1 Pricing number: \2/p

CIS ticket information
n253:op1> grep 571=270062 /sg1/data//.475.*7|tr -s '\001' '\n'|egrep "^+(571|60|48|22|55|64|31|32|423)="


PIMCO burst of messages

less /ts/data/tsfeed/tsfeed_request_events.log | grep "prcNum \[996\]" | cut -b1-15 | sort | uniq -c | less 
