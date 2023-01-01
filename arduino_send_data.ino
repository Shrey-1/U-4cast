
char buf[300];
#include <DHT.h>
#include <DHT_U.h>
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP280.h>

#define DHTPIN 2 
#define DHTTYPE    DHT11
#define BMP_SCK  (13)
#define BMP_MISO (12)
#define BMP_MOSI (11)
#define BMP_CS   (10)
Adafruit_BMP280 bmp; 

int Analog_PIN  =A0; 
int Min_Temperature = -25;
int Max_Temperature = 80;
int sensorValue;
int digitalValue;
const float CURRENT = 3.3; 
const float MAX_AD_VALUE = 1023.0; 
const float AD_VALUE_BY_VOLT = (MAX_AD_VALUE / 5.0) * CURRENT;
DHT_Unified dht(DHTPIN, DHTTYPE);
 


  void setup() {
   pinMode (Analog_PIN, INPUT);
    
    sensor_t sensor;
   
  pinMode(2, INPUT);
  dht.begin();
  bmp.begin();
  bmp.setSampling(Adafruit_BMP280::MODE_NORMAL,     /* Operating Mode. */
                  Adafruit_BMP280::SAMPLING_X2,     /* Temp. oversampling */
                  Adafruit_BMP280::SAMPLING_X16,    /* Pressure oversampling */
                  Adafruit_BMP280::FILTER_X16,      /* Filtering. */
                  Adafruit_BMP280::STANDBY_MS_500);
      Serial.begin(9600);

  }




  void loop() {
      delay(2000);
      float Analog;
  float Tf;
  float Tc;
 sensorValue = analogRead(0);
 String str=String(sensorValue, DEC);
  
  int Temp_Range = (abs(Min_Temperature) + abs(Max_Temperature));
  Analog = analogRead(2);   
  Tf = Analog * (Temp_Range / AD_VALUE_BY_VOLT); // 0 - 1023 is Default Arduino 10 bit resolution for A/D Converter, https://www.arduino.cc/en/Tutorial/AnalogInputPins
  Tc = (Tf - 32) * 5/9;

 sensors_event_t event;
    dht.temperature().getEvent(&event);
   str=str+" "+String(event.temperature);
   
   dht.humidity().getEvent(&event);
        str=str+" "+String(event.relative_humidity);

str=str+" "+String(bmp.readTemperature());
   
str=str+" "+String(bmp.readPressure());

str=str+" "+String(bmp.readAltitude(1105.05));
str=str+" "+String(Tf);
str=str+" "+String(Tc);
    str.toCharArray(buf,str.length());
    
    Serial.write(buf,50); //Write the serial data

    delay(1000);

  }
