#!/bin/bash

for i in {12000..12100};
do
	./answer.out $i | nc ctfq.sweetduet.info 10777
	echo $i 
done