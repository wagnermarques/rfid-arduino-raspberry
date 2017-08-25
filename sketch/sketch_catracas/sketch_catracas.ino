/**
   * Ref.: https://github.com/wagnermarques/rfid 
   * ----------------------------------------------------------------------------
   * This is a MFRC522 library example; see https://github.com/miguelbalboa/rfid
   * for further details and other examples.
   *
   * NOTE: The library file MFRC522.h has a lot of useful info. Please read it.
   *
   * Released into the public domain.
   * ----------------------------------------------------------------------------
   * This sample shows how to read and write data blocks on a MIFARE Classic PICC
   * (= card/tag).
   *
   * BEWARE: Data will be written to the PICC, in sector #1 (blocks #4 to #7).
   *
   *
   * Typical pin layout used:
   * -----------------------------------------------------------------------------------------
   *             MFRC522      Arduino       Arduino   Arduino    Arduino          Arduino
   *             Reader/PCD   Uno/101       Mega      Nano v3    Leonardo/Micro   Pro Micro
   * Signal      Pin          Pin           Pin       Pin        Pin              Pin
   * -----------------------------------------------------------------------------------------
   * RST/Reset   RST          9             5         D9         RESET/ICSP-5     RST
   * SPI SS      SDA(SS)      10            53        D10        10               10
   * SPI MOSI    MOSI         11 / ICSP-4   51        D11        ICSP-4           16
   * SPI MISO    MISO         12 / ICSP-1   50        D12        ICSP-1           14
   * SPI SCK     SCK          13 / ICSP-3   52        D13        ICSP-3           15
   *
   */
 
  #include "/usr/share/arduino/libraries/SPI/SPI.h"
  #include <MFRC522.h>
 
  #define RST_PIN         9         
  #define SS_PIN          10        
 
 
  MFRC522 mfrc522(SS_PIN, RST_PIN);   // Instancia do cartao MFRC522.

  //key.keyByte é um array de 6 posicoes cada uma com 0xFF que é a chave do padrao de fabrica
  MFRC522::MIFARE_Key key; 

  boolean verifica_se_o_cartao_e_compativel();
  String obtem_string_tipo_do_cartao();

  void setup() {
      //Serial.println("=== void setup() {...");
      Serial.begin(9600); // Inicializa comunicacao serial com o computador

      // Nao tendo porta serial aberto, nao faz nada. Importante para arduino baseados no ATMEGA32U
      while (!Serial);   
      SPI.begin();        // Inicializa barramento SPI
      mfrc522.PCD_Init(); // Inicializa cartao MFRC522
    
      //Setando o pino 13 como output porque vamos querer acende-lo quando um usuario logar
      //Esse pino sera utilizado tambem pra forcender os 5 volts pra significar que o usuario foi reconhecido 
      pinMode(LED_BUILTIN, OUTPUT);         
  }
 
 
  /**
   * Main loop.
   */ 
  void loop() { 

       // Loop para leitura de cartoes
      
      if ( ! mfrc522.PICC_IsNewCardPresent())
          return;
    
      //Seleciona tipos de cartoes
      if ( ! mfrc522.PICC_ReadCardSerial())
          return;
 
      if(!verifica_se_o_cartao_e_compativel()){
        Serial.println(F("msg | Cartao Imcompativel. Apenas Mifare Classic sao suportados."));
        return;         
      }
      
      //byte cardUidByte[10] = get_card_uidByte();
      //dump_byte_array(mfrc522.uid.uidByte, mfrc522.uid.size);
      for (byte i = 0; i < mfrc522.uid.size; i++) {
          Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
          Serial.print(mfrc522.uid.uidByte[i], HEX);
      }

  }
 
  boolean verifica_se_o_cartao_e_compativel(){
    //Serial.println("\n === boolean verifica_se_o_cartao_e_compativel(){... \n"); 
      MFRC522::PICC_Type piccType = mfrc522.PICC_GetType(mfrc522.uid.sak);   
      // Checa a compatibilidade
      if (    piccType != MFRC522::PICC_TYPE_MIFARE_MINI
          &&  piccType != MFRC522::PICC_TYPE_MIFARE_1K
          &&  piccType != MFRC522::PICC_TYPE_MIFARE_4K) {       
          return 0;
      }   
      return 1;
  }

  
 


