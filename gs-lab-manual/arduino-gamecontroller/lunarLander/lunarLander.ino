#define UD A0
#define LR A1
int received;
char buffer[10];		  // input buffer
int N; // how many measurements to make but one measurement is always returned in this program
boolean done = false;
int LRvali; // initial LR value
int UDvali; // initial UD value
int LRval; //  LR value
int UDval; //  UD value



void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600);
  digitalWrite(13, LOW);   // turn the LED off
  delay(1000);
  LRvali = analogRead(LR);
  UDvali = analogRead(UD);
}

void loop() {
      received = 0;
    	buffer[received] = '\0';
    	done = false;
    
    	// Check input on serial line.
    	while (!done) {

        //get thruster values
        LRval = analogRead(LR);
        UDval = analogRead(UD);

        //turn on LED if thruster is firing
        if(abs(LRval-LRvali)>1 || abs(UDval-UDvali)>1) {
            digitalWrite(13, HIGH);   // turn the LED on
        }
        else {
            digitalWrite(13, LOW);   // turn the LED off        
        }

        //listen to Serial input
    		if (Serial.available()) {	// Something is in the buffer
    			N = Serial.read();	// so get the number byte
    			done = true;
    		}
    	}

      // get thruster values  
      LRval = analogRead(LR);
      UDval = analogRead(UD);

      // write thruster values
      Serial.print(LRval, DEC);
      Serial.print('\t');
      Serial.print(UDval, DEC);
      Serial.print('\n');
      delay(10);
}
