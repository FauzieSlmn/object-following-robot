char serialRead;
int speed = 150;
void setup() {
 Serial.begin(115200);
 
 pinMode(2, OUTPUT); //enB
 pinMode(3, OUTPUT); // motor A keadaan forward Motor kanan 
 pinMode(4, OUTPUT); // motor A keadaan backward
 pinMode(5, OUTPUT); // motor B keadaan forward Motor Kiri
 pinMode(6, OUTPUT); // motor B keadaan backward
 pinMode(7, OUTPUT); //enA
}

void loop() {
 if (Serial.available() > 0) {
    serialRead = Serial.read();

    switch (serialRead) {
      case 'A':
        forwardMotorA();
        stopMotorB();
        break;
      case 'B':
        forwardMotorA();
        forwardMotorB();
        break;
      case 'C': 
        forwardMotorB();
        stopMotorA();
        break;
      case 'D':
        forwardMotorA();
        stopMotorB();
        break;
      case 'E':
        stopMotorA();
        stopMotorB();
        break;
      case 'F':
        forwardMotorB();
        stopMotorA();
        break;
      case 'G':
        backwardMotorB();
        forwardMotorA();
        break;
      case 'H': 
        backwardMotorB();
        backwardMotorA();
        break;
      case 'J':
        backwardMotorA();
        forwardMotorB();
        break;
    }
 }
}

void forwardMotorA() {
  analogWrite(7, speed);
  digitalWrite(3, HIGH);
  digitalWrite(4, LOW);
}

void backwardMotorA() {
  analogWrite(7, speed);
  digitalWrite(3, LOW);
  digitalWrite(4, HIGH);
}

void stopMotorA() {
 digitalWrite(3, LOW);
 digitalWrite(4, LOW);
}

void forwardMotorB() {
  analogWrite(2, speed);
 digitalWrite(5, HIGH);
 digitalWrite(6, LOW);
}

void backwardMotorB() {
  analogWrite(2, speed);
 digitalWrite(5, LOW);
 digitalWrite(6, HIGH);
}

void stopMotorB() {
 digitalWrite(5, LOW);
 digitalWrite(6, LOW);
}
