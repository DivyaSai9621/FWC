#include <avr/io.h>
#include <util/delay.h>
#include<stdbool.h>
int main (void)
{
bool A,B,C,F;
DDRD=0b11100000;                                        
DDRB=0b00100000;
while(1)
{
A=(PIND & (1<<PIND2)) == (1<<PIND2);
B=(PIND & (1<<PIND3)) == (1<<PIND3);
C=(PIND & (1<<PIND4)) == (1<<PIND4);
F=(A&&!B&&!C)||(!A&&B&&!C)||(!A&&!B&&C)||(A&&B&&C);

PORTB = (F<<5);
}
return 0;

}
