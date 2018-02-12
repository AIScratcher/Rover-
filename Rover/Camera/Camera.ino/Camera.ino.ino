#include "SoftwareSerial.h"
#include <VC0706_UART.h>
#include <SPI.h>
#define SS_SD  10
bool canSnap = false;
//use software serial
SoftwareSerial cameraconnection(2,3);//Rx, Tx
VC0706 cam = VC0706(&cameraconnection);


typedef unsigned int  uint;

void setup() 
{
    Serial.begin(9600);


    if(true == cameraInit()){
        canSnap = true;
        snapShot();
    }else{
      return;
    }
}

void loop() 
{
   
}

bool cameraInit()
{
    cam.begin(BaudRate_19200);
    char *reply = cam.getVersion();
    if (reply == 0) {
        Serial.println("Failed to get version");
        return false;
    } else {
        Serial.println(reply);
        return true;
    }
}

void snapShot()
{
    
    delay(3000);
    if (! cam.takePicture()){ 
         Serial.println("ERROR 0x1");
    }
    
    
    uint16_t jpglen = cam.getFrameLength();

    int32_t time = millis();
    cam.getPicture(jpglen);
    uint8_t picture[jpglen];
    uint8_t *buffer = cam.readPicture(jpglen);
    for(int i = 0;i < jpglen;i++) {
     picture[i] = buffer[i];
    }
    for(int i = 0;i < jpglen;i++) {
      Serial.print(picture[i],DEC);
    }
    cam.resumeVideo();    
}



