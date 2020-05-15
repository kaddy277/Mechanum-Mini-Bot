#include <dht.h>



#include<Wire.h>

#define motorLF1 10
#define motorLF2 5

#define motorRF1 12
#define motorRF2 4

#define motorLB1 8
#define motorLB2 7

#define motorRB1 13
#define motorRB2 2

#define e1 9
#define e2 6

#define e3 11
#define e4 3

int a[10];


void setup()
{
  Wire.begin(0x07);
  Serial.begin(9600);
  
  pinMode(motorLF1,OUTPUT);
  pinMode(motorLF2,OUTPUT);
  pinMode(motorRF1,OUTPUT);
  pinMode(motorRF2,OUTPUT);
  pinMode(motorLB1,OUTPUT);
  pinMode(motorLB2,OUTPUT);
  pinMode(motorRB1,OUTPUT);
  pinMode(motorRB2,OUTPUT);
  
  pinMode(e1,OUTPUT);
  pinMode(e2,OUTPUT);
  pinMode(e3,OUTPUT);
  pinMode(e4,OUTPUT);

  analogWrite(e1,0);
  analogWrite(e2,0);
  analogWrite(e3,0);
  analogWrite(e4,0);
  
  Wire.onReceive(rEVENT);
  
}

void rEVENT()
{
  int nb=Wire.available();
   for(int i=0;i<nb;i++)
   {
    a[i]=Wire.read();
  }
}

void loop()

{ Serial.print("["); 
  for(int i=0;i<10;i++)
{
  Serial.print(a[i]);
  Serial.print(" ");
}
Serial.print("]");
    if(a[1]==0 and a[2]==0 and a[3]==0 and a[4]==0)                     //Wheels don't move
  { Serial.println(" BOT not moving");
    analogWrite(e1,a[5]);
    analogWrite(e2,a[6]);
    analogWrite(e3,a[7]);
    analogWrite(e4,a[8]);
  }
  else if(a[1]==2 and a[2]==2 and a[3]==2 and a[4]==2)                           //BOT moves front
  { analogWrite(e1,a[5]);
    analogWrite(e2,a[6]); 
    analogWrite(e3,a[7]);
    analogWrite(e4,a[8]);
    Serial.println(" BOT moving front");
    digitalWrite(motorLF1,HIGH);
    digitalWrite(motorLF2,LOW);
    digitalWrite(motorRF1,HIGH);
    digitalWrite(motorRF2,LOW);
    digitalWrite(motorLB1,HIGH);
    digitalWrite(motorLB2,LOW);
    digitalWrite(motorRB1,HIGH);
    digitalWrite(motorRB2,LOW);
  }
  else if(a[1]==1 and a[2]==1 and a[3]==1 and a[4]==1)                            //BOT moves back
  { analogWrite(e1,a[5]);
    analogWrite(e2,a[6]);
    analogWrite(e3,a[7]);
    analogWrite(e4,a[8]);
    Serial.println(" BOT moving back");
    digitalWrite(motorLF1,LOW);
    digitalWrite(motorLF2,HIGH);
    digitalWrite(motorRF1,LOW);
    digitalWrite(motorRF2,HIGH);
    digitalWrite(motorLB1,LOW);
    digitalWrite(motorLB2,HIGH);
    digitalWrite(motorRB1,LOW);
    digitalWrite(motorRB2,HIGH);
  }
  else if(a[1]==1 and a[2]==2 and a[3]==1 and a[4]==2)                             //BOT turns towards right
  { analogWrite(e1,a[5]);
    analogWrite(e2,a[6]);
    analogWrite(e3,a[7]);
    analogWrite(e4,a[8]);
    Serial.println(" BOT turning right");
    digitalWrite(motorLF1,HIGH);
    digitalWrite(motorLF2,LOW);
    digitalWrite(motorRF1,LOW);
    digitalWrite(motorRF2,HIGH);
    digitalWrite(motorLB1,HIGH);
    digitalWrite(motorLB2,LOW);
    digitalWrite(motorRB1,LOW);
    digitalWrite(motorRB2,HIGH);
  }
  else if(a[1]==2 and a[2]==1 and a[3]==2 and a[4]==1)                               //BOT turns towards left
  { analogWrite(e1,a[5]);
    analogWrite(e2,a[6]);
    analogWrite(e3,a[7]);
    analogWrite(e4,a[8]);
    Serial.println(" BOT turning left");
    digitalWrite(motorLF1,LOW);
    digitalWrite(motorLF2,HIGH);
    digitalWrite(motorRF1,HIGH);
    digitalWrite(motorRF2,LOW);
    digitalWrite(motorLB1,LOW);
    digitalWrite(motorLB2,HIGH);
    digitalWrite(motorRB1,HIGH);
    digitalWrite(motorRB2,LOW);
  }
  else if(a[1]==2 and a[2]==0 and a[3]==0 and a[4]==2)                              //BOT moves diagonally right forward
  { analogWrite(e1,a[5]);
    analogWrite(e2,a[6]);
    analogWrite(e3,a[7]);
    analogWrite(e4,a[8]);
    Serial.println(" BOT moving diagonally right front");
    digitalWrite(motorLF1,HIGH);
    digitalWrite(motorLF2,LOW);
    digitalWrite(motorRF1,LOW);
    digitalWrite(motorRF2,LOW);
    digitalWrite(motorLB1,LOW);
    digitalWrite(motorLB2,LOW);
    digitalWrite(motorRB1,HIGH);
    digitalWrite(motorRB2,LOW);
  }
  else if(a[1]==1 and a[2]==0 and a[3]==0 and a[4]==1)                              //BOT moves diagonally left downwards
  { analogWrite(e1,a[5]);
    analogWrite(e2,a[6]);
   analogWrite(e3,a[7]);
    analogWrite(e4,a[8]);
    Serial.println(" BOT moving diagonally left downwards");
    digitalWrite(motorLF1,LOW);
    digitalWrite(motorLF2,HIGH);
    digitalWrite(motorRF1,LOW);
    digitalWrite(motorRF2,LOW);
    digitalWrite(motorLB1,LOW);
    digitalWrite(motorLB2,LOW);
    digitalWrite(motorRB1,LOW);
    digitalWrite(motorRB2,HIGH);
  }
  else if(a[1]==0 and a[2]==2 and a[3]==2 and a[4]==0)                              //BOT moves diagonally left forward
  { analogWrite(e1,a[5]);
    analogWrite(e2,a[6]);
    analogWrite(e3,a[7]);
    analogWrite(e4,a[8]);
    Serial.println(" BOT moving diagonally left forward");
    digitalWrite(motorLF1,LOW);
    digitalWrite(motorLF2,LOW);
    digitalWrite(motorRF1,HIGH);
    digitalWrite(motorRF2,LOW);
    digitalWrite(motorLB1,HIGH);
    digitalWrite(motorLB2,LOW);
    digitalWrite(motorRB1,LOW);
    digitalWrite(motorRB2,LOW);
  }
  else if(a[1]==0 and a[2]==1 and a[3]==1 and a[4]==0)                              //BOT moves diagonally right downwards
  { analogWrite(e1,a[5]);
    analogWrite(e2,a[6]);
    analogWrite(e3,a[7]);
    analogWrite(e4,a[8]);
    Serial.println(" BOT moving diagonally right downwards");
    digitalWrite(motorLF1,LOW);
    digitalWrite(motorLF2,LOW);
    digitalWrite(motorRF1,LOW);
    digitalWrite(motorRF2,HIGH);
    digitalWrite(motorLB1,LOW);
    digitalWrite(motorLB2,HIGH);
    digitalWrite(motorRB1,LOW);
    digitalWrite(motorRB2,LOW);
  }

  else if(a[1]==2 and a[2]==1 and a[3]==1 and a[4]==2)                              //BOT moves right w/o turning
  { analogWrite(e1,a[5]);
    analogWrite(e2,a[6]);
    analogWrite(e3,a[7]);
    analogWrite(e4,a[8]);
    Serial.println(" BOT moving right");
    digitalWrite(motorLF1,HIGH);
    digitalWrite(motorLF2,LOW);
    digitalWrite(motorRF1,LOW);
    digitalWrite(motorRF2,HIGH);
    digitalWrite(motorLB1,LOW);
    digitalWrite(motorLB2,HIGH);
    digitalWrite(motorRB1,HIGH);
    digitalWrite(motorRB2,LOW);
  }
  else if(a[1]==1 and a[2]==2 and a[3]==2 and a[4]==1)                              //BOT moves left w/o turning
  { analogWrite(e1,a[5]);
    analogWrite(e2,a[6]);
   analogWrite(e3,a[7]);
    analogWrite(e4,a[8]);
    Serial.println(" BOT moving left");
    digitalWrite(motorLF1,LOW);
    digitalWrite(motorLF2,HIGH);
    digitalWrite(motorRF1,HIGH);
    digitalWrite(motorRF2,LOW);
    digitalWrite(motorLB1,HIGH);
    digitalWrite(motorLB2,LOW);
    digitalWrite(motorRB1,LOW);
    digitalWrite(motorRB2,HIGH);
  }
}
