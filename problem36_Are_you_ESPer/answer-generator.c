#include <stdio.h>
#include <stdlib.h>
#include <time.h> 
#include <stdint.h>

/* 
nc ctfq.sweetduet.info 10777

to check remote server timestamp, ssh to server as follows and ran date command
'''
ssh -p 10022 q4@ctfq.sweetduet.info
Pass: q60SIMpLlej9eq49
'''
The above login info can be found at challenge "Villager A" (http://ksnctf.sweetduet.info/problem/4)

https://dixq.net/forum/viewtopic.php?t=16864 
https://stackoverflow.com/questions/3818755/imul-assembly-instruction-one-operand
https://stackoverflow.com/questions/38961903/get-high-32bit-of-32x32-multiply
http://www.koikikukan.com/archives/2017/10/31-000300.php
https://cboard.cprogramming.com/c-programming/104485-how-convert-uint32_t-string.html
https://stackoverflow.com/questions/11147633/send-and-receive-an-integer-value-over-tcp-in-c
https://ctftime.org/writeup/12780
https://github.com/VulnHub/ctf-writeups/blob/master/2016/tjctf/guess.md
https://ctftime.org/writeup/11396
*/

int main(int argc, char *argv[])
{
	//srand(time(NULL));
	srand(time(NULL) + atoi(argv[1])); //need to get exact current time
	//the system clock for ctfq.sweetduet.info was about 12061 seconds ahead at the time of solving
	int i;
	for (i = 0; i<20; i++) {
		//int eax = rand();
		uint32_t ecx = rand();
		uint32_t hardcoded_value = 1717986919; //0x66666667
		uint64_t edx = (uint64_t) ecx * hardcoded_value;
		uint32_t msb = (edx >> 32) & 0xffffffff;
		//printf("msb: %d\n", msb);
		uint32_t eax = ecx >> 31;
		uint32_t edi = msb;
		edi = edi >> 2;
		edi = edi - eax;
		edi = edi + edi * 4;
		edi = edi + edi;
		uint32_t randint = ecx - edi;
		//printf("randint: %d\n", randint);
		printf("%d\n", randint);
	}
	return 0;
}

/*
Level 1/20, Challenge 1/10
? Correct!

Level 2/20, Challenge 1/8
? Correct!

Level 3/20, Challenge 1/6
? Correct!

Level 4/20, Challenge 1/4
? Correct!

Level 5/20, Challenge 1/2
? Correct!

Level 6/20, Challenge 1/1
? Correct!

Level 7/20, Challenge 1/1
? Correct!

Level 8/20, Challenge 1/1
? Correct!

Level 9/20, Challenge 1/1
? Correct!

Level 10/20, Challenge 1/1
? Correct!

Level 11/20, Challenge 1/1
? Correct!

Level 12/20, Challenge 1/1
? Correct!

Level 13/20, Challenge 1/1
? Correct!

Level 14/20, Challenge 1/1
? Correct!

Level 15/20, Challenge 1/1
? Correct!

Level 16/20, Challenge 1/1
? Correct!

Level 17/20, Challenge 1/1
? Correct!

Level 18/20, Challenge 1/1
? Correct!

Level 19/20, Challenge 1/1
? Correct!

Level 20/20, Challenge 1/1
? Correct!

Congratulations!
FLAG_Xmh3xVEXQ7zwTwkT

*/