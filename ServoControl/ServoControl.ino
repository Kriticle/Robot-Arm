#include<Servo.h>
#include<stdio.h>
int myArray[5];
int val[5];
byte* ddata = reinterpret_cast<byte*>(&myArray); // pointer for transferData()
int pcDataLen = sizeof(myArray);
Servo myservoi;
Servo myservom;
Servo myservor;
Servo myservop;
Servo myservot;
Servo myservo[5] = {myservot,myservoi,myservom,myservor,myservop};
bool newData = false;
void setup() {
    Serial.begin(115200);
    myservo[0].attach(7);
    myservo[1].attach(8);
    myservo[2].attach(9);
    myservo[3].attach(10);
    myservo[4].attach(11);
    for (int k=0;k<5;k++){
      myservo[k].write(0);
    }
    // usual stuff
}

void loop() {
    checkForNewData();
    if (newData == true) {
      for (int i=0;i<5;i++){
        val[i] = map (myArray[i],0,320,0,180);
        printf("%d",myArray[i]);
      }
      printf("\n");
      for (int j=0;j<5;j++){
        myservo[j].write(val[j]);
      }
        newData = false;
    }
    for (int k=0;k<5;k++){
      myservo[k].write(0);
    }
}
void checkForNewData () {
    if (Serial.available() >= pcDataLen and newData == false) {
        byte inByte;
        for (byte n = 0; n < pcDataLen; n++) {
            inByte = Serial.read();
            ddata[n] = inByte;
        }
        newData = true;
    }
}