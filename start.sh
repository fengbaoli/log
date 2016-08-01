#!/bin/bash
while((1<2))
do
status=`ps -ef|grep python|grep client.py|grep -v grep|wc -l`
if [ $status -eq 0 ];then
python client.py  &>/dev/null
fi
sleep 10
done
