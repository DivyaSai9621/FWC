#include <Arduino.h>
int A,B,C,X;

void setup() 
{
    pinMode(5, OUTPUT);
    pinMode(2, INPUT);  
    pinMode(3, INPUT);
    pinMode(4, INPUT);
    
}

// the loop function runs over and over again forever
void loop() 
{
A = digitalRead(2); 
B = digitalRead(3); 
C = digitalRead(4); 
 
X=(!A&&!B&&C)||(!A&&B&&!C)||(A&&B&&C)||(A&&!B&&!C);

digitalWrite(5,X);
}
