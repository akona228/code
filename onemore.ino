void setup()
{ 
    for(int i = 0; i <= 13; i++){ 
        pinMode(i, OUTPUT);
}
}

void loop() {
for(int i = 0; i <= 13; i++){
digitalWrite(i, HIGH);
delay(300);

}

}

int led_start = 0;
int led_end = 13;

void setup()
{
  for(int i = led_start; i <= led_end; i++){
  pinMode(i, OUTPUT);
  }

}

void loop() {
  for(int i = led_end; i >= led_start; i -- ){
  digitalWrite(i, HIGH);
  delay(pause); 
  pause = pause + 100;
  }
}