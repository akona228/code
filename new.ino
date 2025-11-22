#include <Key.h>

int r = 11;
int g = 9;
int b = 10;


void setup()
{
    pinMode(r, OUTPUT);
    pinMode(g, OUTPUT);
    pinMode(b, OUTPUT);
}

void loop ()
{
    //(sosa) - соничка
    analogWrite(r, 247);
    analogWrite(g, 228);
    analogWrite(b, 84);

    delay(500);
    //(принцесса) - влад
    analogWrite(r, 133);
    analogWrite(g, 173);
    analogWrite(b, 127);
    
    delay(500);
    //мой
    analogWrite(r, 120);
    analogWrite(g, 151);
    analogWrite(b, 158);

    delay(500);

}