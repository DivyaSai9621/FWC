


.include "/home/divya/assembly/m328Pdef.inc"

ldi r16,0b00100000  ;2 pin as output
out DDRB,r16



ldi r17, 0b11111000 ; identifying input pins 8,9,10
	out DDRB,r17		; declaring pins as input
ldi r17, 0b11111000;
	out PORTB,r17		; activating internal pullup for pins 8,9,10



ldi r18,0b00000001 ; value
ldi r19,0b00000001 ; value
ldi r20,0b00000001 ; value



and r18,r17 ; r18=C
lsr r17
and r19,r17; r19=B
lsr r17
and r20,r17; r20=A
lsr r17


ldi r22,0b00000001;
eor r22,r18;  r22=C'
ldi r23,0b00000001;
eor r23,r19; r23=B'
ldi r24,0b00000001;
eor r24,r20; r24=A'


mov r0,r24   ;for A'
and r0,r23   ; for A'B'
and r0,r18   ;for A'B'C=r0

mov r1,r24   ; for A'     
and r1,r19   ;for  A'B
and r1,r22   ;for A'BC'=r26

or  r0,r1   ;for A'B'C+A'BC'=r0

mov r2,r20   ;for A
and r2,r19  ;for  AB
and r2,r18   ;for ABC=r2

or r0,r2   ;for A'B'C+A'BC'+ABC=r0
mov r3,r20   ;for A
and r3,r23   ;for AB'
and r3,r22   ;forAB'C'=r3

or  r0,r3  ;for A'B'C+A' B C'+A B C+A B'C'=r16
mov r16,r0
lsl r16
lsl r16
lsl r16
lsl r16
lsl r16

out PORTD,r16             ;F output

start:
rjmp start
