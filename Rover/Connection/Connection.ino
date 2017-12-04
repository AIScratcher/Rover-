
#define input 11
#define output 12
#define delay_ms 10

void read_num() {
  int num[32];
  for(int i = 0; i < 32;++i) {
    num[i] = digitalWrite(input);
    delay(delay_ms);
  }
  char numc[33] = {'B',(char) num , '\0'};
  
}

void loop() {
  
}

