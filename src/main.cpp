//Rfid 0.91
#define PIN_SPK 15 //pin спикера
#define SS_PIN 2  //pin ss rfid
#define RST_PIN 0 //pin rst rfid
#define NUM_LEDS 8  //кол-во светодиодов
#define PIN_LEDS 16 //pin 1-го светодиода

#include <Arduino.h>
#include <Ticker.h>     //для создания периодических вызовов функций (таймеры)
#include <SPI.h>        //для работы с интерфейсом SPI
#include <MFRC522.h>    //для работы с RFID-модулем RC522
#include "FastLED.h"    //для управления адресуемыми светодиодными лентами и матрицами.
#include <ESP8266WiFi.h>//для работы с Wi-Fi на ESP8266
#include <ESP8266Ping.h>//для выполнения операций Ping на ESP8266
#include <PubSubClient.h>//для работы с MQTT-протоколом на ESP8266

void rcread();//предназначена для чтения данных с RFID-модуля
void color_rainboow();
void color_rfid();
void color_blue();
void color_red();
void color_yellow();
void senddata();//для отправки данных через протокол MQTT

Ticker reboottimer; //для управления перезагрузкой
MFRC522 mfrc522(SS_PIN, RST_PIN); //для работы с RFID-модулем
CRGB leds[NUM_LEDS]; //последовательность RGB
WiFiClient espClient;//для работы с Wi-Fi на ESP8266
PubSubClient client(espClient);//для работы с MQTT-протоколом

int out = 0;
int stread = 0;
int streads = 0;
int blocktime2;
float counter;
float counters;
int rbsr;
String rcuid = "";
String rcuids = "";

int setbrg = 250;        //яркость радуги
int setbrg1 = 250 ;        //яркость сплошных цветов цвет
int rbn_time1 = 850 ;     //задержка цвет
int rbn_time2 = 250 ;      //задержка черный
int rbnshag = 2 ;        //шаг радуги
int rbnspeed = 80 ;      //скорость радуги
int blocktime = 12;      //блокировка время повторного считывания
int spkMHz = 1300;         //частота спикера
int spk_beeptime = 250;  //время спикера
int typycode = 0;         //тип кода 522 0-hex_lite  1-DEC 2-HEX
float rebootesp = 86400.0; //время reboot, sec

const char* ssid = "Sovetskaya 49-77"; //wifi SSID
const char* password = "233200101070001"; //wifi Password
const char* mqttServer = "192.168.3.21";
const int mqttPort = 20204;
const char* mqttUser = "userGOKB";
const char* mqttPassword = "@pdL!12sP";
const char* msgTopic = "info/uid";    //Топик в который шлем сообщения
const char* msgconect = "Устройство добавления чипов";  //Сообщение при старте
const IPAddress hostName(192,168,50,111); //ip mqtt для пинга
int pingResult = 1;
IPAddress ipadress(192,168,100,39);
IPAddress gatewayadress(192,168,100,1);
IPAddress subnetadress(255,255,255,0);
void restart(){
ESP.restart();
}

void setup() { //инициализируются и настраиваются различные компоненты и библиотеки(выполняется 1 раз при запуске микроконтроллера)
  //Serial.begin(115200);
  SPI.begin();
  mfrc522.PCD_Init();
  FastLED.addLeds<WS2811, PIN_LEDS, GRB>(leds, NUM_LEDS).setCorrection( TypicalLEDStrip );//настройка адресуемых светодиодов
  WiFi.config(ipadress, gatewayadress, subnetadress);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
     delay(500);
     color_blue();
  }
   client.setServer(mqttServer, mqttPort);//настройка сервера MQTT
     while (!client.connected()) {
      color_yellow(); //Connecting to MQTT...
  if (client.connect("espClient", mqttUser, mqttPassword )) {
       color_rfid();  //connected
     } else {
      color_red();  //failed with state
      delay(2000);
    }
  }
  client.publish("info", msgconect); //Restart info
  reboottimer.attach(rebootesp, restart);
  }

void loop() {
color_rainboow(); //функция для изменения цвета адресуемых светодиодов в радужных цветах
senddata();       //функция для отправки данных
rcread();         //функция для чтения RFID
if (WiFi.status() != WL_CONNECTED)
    {
      color_blue();
      ESP.restart();
    }
// pingResult =  Ping.ping(hostName);
// if (pingResult == 0) {
// ESP.restart();
// }
}

void senddata(){ //для отправки данных через протокол MQTT
if (rcuid != rcuids){
  rcuids = rcuid;
  char msgOut [25];
  rcuid.toCharArray(msgOut,25); //Создается массив символов и копируется значение rcuid
  client.connect("espClient", mqttUser, mqttPassword );//Устанавливается соединение с MQTT сервером
  client.publish(msgTopic,msgOut);//Отправляется сообщение msgOut на топик
  client.subscribe(msgTopic);
  color_rfid();//Светодиоды меняют цвет на зеленый
  }
else if ( streads == 1){
  char msgOut [25];
  rcuid.toCharArray(msgOut,25);
  client.connect("espClient", mqttUser, mqttPassword );
  client.publish(msgTopic, msgOut);
  color_rfid();//Светодиоды меняют цвет на зеленый
  stread = 1;
  streads = 0;
  }
}

void rcread() {//предназначена для чтения данных с RFID-модуля
   if ( ! mfrc522.PICC_IsNewCardPresent())   {
    return;// Если новая карта не обнаружена, выходим из функции
  }
  if ( ! mfrc522.PICC_ReadCardSerial())   {
    return;// Если не удалось считать серийный номер карты, выходим из функции
  }
  String uid522DEC = ""; // Переменная для хранения UID в десятичном формате
  String uid522HEX = ""; // Переменная для хранения UID в шестнадцатеричном формате
  String uid522HEXs = ""; // Переменная для хранения UID в шестнадцатеричном формате (в верхнем регистре)

  //byte letter;
  blocktime2 = blocktime + 1;
  // Цикл для конкатенации байтов UID в строки uid522DEC, uid522HEX и uid522HEXs
  for (byte i = 0; i < mfrc522.uid.size; i++)
  {
     uid522DEC.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? "0" : ""));
     uid522DEC.concat(String(mfrc522.uid.uidByte[i], DEC));
     uid522HEX.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? "0" : ""));
     uid522HEX.concat(String(mfrc522.uid.uidByte[i], HEX));
     uid522HEXs.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? "0" : ""));
     uid522HEXs.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
     uid522HEXs.toUpperCase(); // Преобразование uid522HEXs в верхний регистр

// Проверка условий и обработка UID в формате HEX
  if (uid522HEX != rcuid && typycode == 0){
    rcuid = uid522HEX;
    stread = 1;
    tone(PIN_SPK, spkMHz, spk_beeptime);
    Serial.print(" UID tag HEX mqtt :");
    Serial.println(rcuid);
    }
    else if (uid522HEX == rcuid && typycode == 0 && stread <= blocktime){
    stread++;
    }
    else if (uid522HEX == rcuid && typycode == 0 && stread == blocktime2){
    stread = 0;
    streads = 1;
    tone(PIN_SPK, spkMHz, spk_beeptime);
    }
  // Проверка условий и обработка UID в формате DEC
    if (uid522DEC != rcuid && typycode == 1 ){
    rcuid = uid522DEC;
    tone(PIN_SPK, spkMHz, spk_beeptime);
    Serial.print(" UID tag DEC mqtt :");
    Serial.println(rcuid);
    }
  // Проверка условий и обработка UID в формате HEXs
    if (uid522HEXs != rcuid &&  typycode == 2){
    rcuid = uid522HEXs;
    tone(PIN_SPK, spkMHz, spk_beeptime);
    Serial.print(" UID tag HEXs mqtt :");
    Serial.println(rcuid);
    }
    }

void color_rainboow() {
  FastLED.setBrightness(setbrg);// Установка яркости светодиодной ленты
  for (int i = 0; i < NUM_LEDS; i++ ) {
    // Установка цвета светодиодов в радужных оттенках
    leds[i] = CHSV(counter + i * rbnshag, 255, 255);  // умножение i уменьшает шаг радуги
    // Параметры CHSV: (hue, saturation, value)
    // hue - определяет цвет (0-255), counter + i * rbnshag обеспечивает плавное изменение цвета
    // saturation - насыщенность цвета (0-255), здесь установлена на максимальное значение
    // value - яркость цвета (0-255), здесь установлена на максимальное значение
  }
    counters = rbnspeed * 0.01;// Изменение счетчика радуги на основе заданной скорости
    counter = counter + counters;// Изменение счетчика для плавного перехода цветов(counter меняется от 0 до 255 (тип данных byte)
  FastLED.show();
}

void color_rfid() {
  FastLED.setBrightness(setbrg1);
  for (int i = 0; i < NUM_LEDS; i++ ) {
    leds[i] = CRGB::Green;;
  }
  FastLED.show();
  FastLED.delay(rbn_time1); // Задержка в миллисекундах
  for (int i = 0; i < NUM_LEDS; i++ ) {
    leds[i] = CRGB::Black;;
  }
  FastLED.show();
}

void color_red() {
  FastLED.setBrightness(setbrg1);
  for (int i = 0; i < NUM_LEDS; i++ ) {
    leds[i] = CRGB::Red;;
  }
  FastLED.show();

}

void color_blue() {
  FastLED.setBrightness(setbrg1);
  for (int i = 0; i < NUM_LEDS; i++ ) {
    leds[i] = CRGB::Blue;;
  }
  FastLED.show();
  FastLED.delay(250);
  for (int i = 0; i < NUM_LEDS; i++ ) {
    leds[i] = CRGB::Black;;
  }
  FastLED.show();
}

void color_yellow() {
  FastLED.setBrightness(setbrg1);
  for (int i = 0; i < NUM_LEDS; i++ ) {
    leds[i] = CRGB::Yellow;;
  }
  FastLED.show();
}

