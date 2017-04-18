from socket import *
import sys
import array
from socket import gethostname, gethostbyname 
Hosti='127.0.0.1'
Porti=9000
import os
klientisocket=socket(AF_INET,SOCK_DGRAM)

#PASTRIMI KONSOLES---------------------------------------------#
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#--------------------------------------------------------------#

            
#definimi f-oneve--------------------------------------------->
  #Foni printo:
def Printo():
      try:
         EdhenaPrintim=input('Shtypni teksin tuaj ne formatin PRINTO emri qe deshironi ta ktheni mbrapsht\n')
         a,b=EdhenaPrintim.split(' ')
         if(a=='PRINTO'):
           klientisocket.sendto(EdhenaPrintim.encode('utf-8'),(Hosti,Porti))
           mesazhipranuar,serveradresa=klientisocket.recvfrom(1024)
           print('Pergjigja: '+mesazhipranuar.decode('utf-8'))
      except:
          print('Keni shkruar formatin gabbim ose kemi probleme me klientserverin')
          
  #Foni Zanore:
def Zanore():
      try:      
        EdhenaZanore=input('Shtypni nje tekst ne formatin ZANORE emri qe deshironi te numroni zanoret\n')
        zanore,emri=EdhenaZanore.split(' ')
        if(zanore=='ZANORE'):
           klientisocket.sendto(EdhenaZanore.encode('utf-8'),(Hosti,Porti))
           mesazhipranuar,serveradresa=klientisocket.recvfrom(1024)
           print(mesazhipranuar.decode('utf-8'))
      except:
           print('Keni shkruar formatin gabbim ose kemi probleme me klientserverin')
def IP():
      try:
           IP1='IP'+' '+gethostbyname(gethostname())
           klientisocket.sendto(IP1.encode('utf-8'),(Hosti,Porti))
           mesazhipranuar,serveradresa=klientisocket.recvfrom(1024)
           print('Ip e Klientit eshte:')
           print(mesazhipranuar.decode('utf-8'))
      except:
          print('Gabime me klientserverin, ju kerkojme ndjese')
        
   #Foni Faktoriel:
def Faktoriel():
      try:
            EdhenaFaktoriel=input('Shtypni nje tekst ne formatin FAKTORIEL numri qe deshironi te llogaritni\n')
            faktoriel,numri=EdhenaFaktoriel.split(' ')
            if(faktoriel=='FAKTORIEL'):
              klientisocket.sendto(EdhenaFaktoriel.encode('utf-8'),(Hosti,Porti))
              mesazhipranuar,serveradresa=klientisocket.recvfrom(1024)
              print('Kemi marrur me sukses pergjigjen nga serveri-Faktoriel per llogaritjen e faktorielit: Numri qe derguat eshte '+numri +' Faktoriel i tij eshte:')
              print(mesazhipranuar.decode('utf-8'))
      except:
            print('Keni shkruar formatin gabbim ose kemi probleme me klientserverin')
            
             
     #Foni Time:
def Time():
      try:
              klientisocket.sendto(message.encode('utf-8'),(Hosti,Porti))
              mesazhipranuar,serveradresa=klientisocket.recvfrom(1024)
              print('Kemi marrur me sukses pergjigjen nga serveri-Time per kthimin e kohes,Koha e sakte eshte: ')
              print(mesazhipranuar.decode('utf-8'))
      except:
               print('Kemi probleme me Klientserverin ,ju kerkojme ndjese!')
              
           
     #Foni Keno:
def Keno():
      try:
              klientisocket.sendto(message.encode('utf-8'),(Hosti,Porti))
              mesazhipranuar,serveradresa=klientisocket.recvfrom(1024)
              print('Kemi marrur me sukses pergjigjen nga serveri-Keno per kthimin e 20 numrave nga rangu [1,80],Keta numra jane: ')
              print(mesazhipranuar.decode('utf-8'))
      except:
         print('Gabime me klientiserverin ju kerkojme ndjese')
         
      #Foni Hosti:
def Host():
      try: 
              klientisocket.sendto(message.encode('utf-8'),(Hosti,Porti))
              mesazhipranuar,serveradresa=klientisocket.recvfrom(1024)
              print(mesazhipranuar.decode('utf-8'))
      except:
              print('Gabime me klientiserverin ju kerkojme ndjese')
       

    #fONI PER PORTIN:
def Port():
      try:
              pergjigja='PORTI'
              klientisocket.sendto(pergjigja.encode('utf-8'),(Hosti,Porti))
              mesazhipranuar,serveradresa=klientisocket.recvfrom(1024)
              print(mesazhipranuar.decode('utf-8'))   
      except:
              print('Gabime me klientserverin')
             
#Ketu fillojne f-onet e Rines:
def Rina():
      try:
              Edhena=input('Jeni ne pjesen e realizuar nga Rina ,dy metadota e saj jane:Siperfaqjaperimetri dhe domeni,\n shtyp 1 per metoden SiperfaqjaPerimetri\n Shtyp 2 per metoden domeniEmailit\n')
              if(Edhena=='1'):
                SiperfaqjaPerimetri()
              if(Edhena=='2'):
                  Emaili()
              else:
                  print('Nuk keni shtypur asnjeren nga parametrat 1 ose 2')
                  inputRina=input('shtypni P nese doni te vazhdoni tek metoda Rina , shtypni J nese doni tjera')
                  if(inputRina=='P'):
                    cls()
                    Rina()
                  else:
                    perfundo()
                 
      except:
          print('formati gabim ose klientiserveri nuk funksionon')

def Trekendeshi():
                      print('Shkruani parametrat ne formen psh:LARTESIA:4 BAZA:5 ku e dhena miret ne centimeter\n')
                      lartesia=input('LARTESIA:')
                      baza=input('BAZA:')
                      try:
                          lartesia1=float(lartesia)
                          baza1=float(baza) 
                          parametratDergim='TREKENDESHI'+' '+lartesia+' '+baza
                          klientisocket.sendto(parametratDergim.encode('utf-8'),(Hosti,Porti))
                          mesazhipranuar,serveradresa=klientisocket.recvfrom(1024)
                          print(mesazhipranuar.decode('utf-8'))
                          inputRina=input('shtypni P nese doni te vazhdoni tek metoda Rina , shtypni J nese doni tjera')
                          if(inputRina=='P'):
                              cls()
                              Rina()
                          else:
                              perfundo()
                      except ValueError:
                        print("KENI SHTYPUR TE DHENA INVALIDE OSE KEMI PROBLEME ME KLIENTSERVERIN")
                        inputRina=input('shtypni P nese doni te vazhdoni tek metoda Rina , shtypni J nese doni tjera')
                        if(inputRina=='P'):
                          cls()
                          Rina()
                        else:
                          perfundo()
def Katrori():
                      print('Shkruani brinjen e katrorit ne formen BRINJA:\n')
                      brinja=input('BRINJA:')
                      try:
                          brinja1=float(brinja)
                          parametratDergim='KATRORI'+' '+brinja
                          klientisocket.sendto(parametratDergim.encode('utf-8'),(Hosti,Porti))
                          mesazhipranuar,serveradresa=klientisocket.recvfrom(1024)
                          print(mesazhipranuar.decode('utf-8'))
                          inputRina=input('shtypni P nese doni te vazhdoni tek metoda Rina , shtypni J nese doni tjera')
                          if(inputRina=='P'):
                              cls()
                              Rina()
                          else:
                              perfundo()
                      except ValueError:
                        print("KENI SHTYPUR TE DHENA INVALIDE OSE KEMI PROBLEME ME KLIENTSERVERIN")
                        inputRina=input('shtypni P nese doni te vazhdoni tek metoda Rina , shtypni J nese doni tjera')
                        if(inputRina=='P'):
                          cls()
                          Rina()
                        else:
                          perfundo()
def Rrethi():
                      print('Shkruani rrezja e katrorit ne formen RREZJA:\n')
                      rrezja=input('RREZJA:')
                      try:
                          rrezja1=float(rrezja)
                          parametratDergim='RRETHI'+' '+rrezja
                          klientisocket.sendto(parametratDergim.encode('utf-8'),(Hosti,Porti))
                          mesazhipranuar,serveradresa=klientisocket.recvfrom(1024)
                          print(mesazhipranuar.decode('utf-8'))
                          inputRina=input('shtypni P nese doni te vazhdoni tek metoda Rina , shtypni J nese doni tjera')
                          if(inputRina=='P'):
                              cls()
                              Rina()
                          else:
                              perfundo()
                      except ValueError:
                        print("KENI SHTYPUR TE DHENA INVALIDE OSE KEMI PROBLEME ME KLIENTSERVERIN")
                        inputRina=input('shtypni P nese doni te vazhdoni tek metoda Rina , shtypni J nese doni tjera')
                        if(inputRina=='P'):
                          cls()
                          Rina()
                        else:
                          perfundo()
def SiperfaqjaPerimetri():
      print('Kjo metode ju mundeson te njehsoni siperfaqen dhe perimetrin e tre formave gjeometrike:\ntrekendeshit,rrethit dhe katorit\n Per te bere kete fillimisht zgjidhni formen gjeometrike duke shkruar mesazhin ne formatin psh :TREKENDESHI\n')
      forma=input('Forma: ')
      if(forma=='TREKENDESHI'):
           Trekendeshi()
      if(forma=='KATRORI'):
         Katrori()
      if(forma=='RRETHI'):
          Rrethi()
                        
def Emaili():
                      try:
                        print('Shkruni emailin dhe ne do te ju tregojme domenin tuaj')
                        emaili=input('Emaili: ')
                        EmailiDergim='Emaili'+' '+emaili
                        klientisocket.sendto(EmailiDergim.encode('utf-8'),(Hosti,Porti))
                        mesazhipranuar,serveradresa=klientisocket.recvfrom(1024)
                        print(mesazhipranuar.decode('utf-8'))
                        inputRina=input('shtypni P nese doni te vazhdoni tek metoda Rina , shtypni J nese doni tjera')
                        if(inputRina=='P'):
                           cls()
                           Rina()
                        else:
                         perfundo()
                      except:
                          print('GABIME ME KLIENTSERVERIN OSE FONIN\n')
                          perfundo()
#Metodat e ardianit
def Ardian():
    try:
         pergjigja=input("Zgjedh njerin nga Funksionet RANGU ose TEK\n")
         if(pergjigja == 'RANGU' ):
                 Rangu()
                
         if(pergjigja == 'TEK' ):
                TEK()
                
    except:
          print('Keni shtypur gabim formatin ose kemi probleme me klientserverin')
          perfundo()

def Rangu():
    try:
        num = input('Shtypni numrin i cili percakton se deri ne cilin rang numrohen numrat e thjeshte (shkruaje ne formatin RANGU numri ) \n')
        ranguu,numrii=num.split(' ')
        if(ranguu=='RANGU'):
            klientisocket.sendto(num.encode('utf-8'),(Hosti,Porti))
            mesazhipranuar,serveradresa=klientisocket.recvfrom(1024)
            print('Kemi marrur me sukses pergjigjen nga serveri-Rangu per numrimin e nr te thjeshte: Numri qe derguat eshte '+numrii +' dhe numri i kthyer nga serveri eshte:')
            print(mesazhipranuar.decode('utf-8'))
    except:
            print('Keni shkruar formatin gabim ose kemi probleme me klient-serverin')
            perfundo()
            

def TEK():
    try:
         numtek = input('Shtypni numrin i cili percakton se deri ne cilin rang numrohen numrat tek (shkruaje ne formatin TEK numri ) \n')
         tek,numriii=numtek.split(' ')
         if(tek=='TEK'):
            klientisocket.sendto(numtek.encode('utf-8'),(Hosti,Porti))
            mesazhipranuar,serveradresa=klientisocket.recvfrom(1024)
            print('Kemi marrur me sukses pergjigjen nga serveri-TEK per numrimin e nr tek: Numri qe derguat eshte '+numriii +' dhe numri i kthyer nga serveri eshte:')
            print(mesazhipranuar.decode('utf-8'))
    except:
            print('Keni shkruar formatin gabim ose kemi probleme me klient-serverin')



#ketu fillojne f-onet e Rrezartes

#----------------------------->
#Ketu fillojne fonet e Valmires
def Valmira():
      try:
         pergjigja=input("Zgjedh njerin nga Funksionet DITELINDJA ose LOTARIA\n")
         if(pergjigja == 'DITELINDJA' ):
                ditelindja()
                
         if(pergjigja == 'LOTARIA' ):
                lotaria()
                
      except:
          print('Keni shtypur gabim formatin ose kemi probleme me klientserverin')
          perfundo()
def ditelindja():
        print('A gjendet dita juaj e lindjes ne kete bllok: \n'
                      '1    3    5    7\n'
                      '9   11   13    15\n'                      
                      '17  19   21    23\n'
                      '25  27   29    31\n')
        pergjigja1=input('Pergjigju me PO ose JO\n')

        print('A gjendet dita juaj e lindjes ne kete bllok: \n'
                      '2    3    6    7\n'
                      '10  11   14    15\n'                      
                      '18  19   22    23\n'
                      '26  27   30    31\n')
        pergjigja2=input('Pergjigju me PO ose JO\n')
  
        print('A gjendet dita juaj e lindjes ne kete bllok: \n'
                      '4    5    6    7\n'
                      '12   13   14    15\n'                      
                      '20  21   23    23\n'
                      '28  29   30    31\n')
        pergjigja3=input('Pergjigju me PO ose JO\n')

        print('A gjendet dita juaj e lindjes ne kete bllok: \n'
                      '8    9   10    11\n'
                      '12  13   14    15\n'                      
                      '24  25   26    27\n'
                      '28  29   30    31\n')
        pergjigja4=input('Pergjigju me PO ose JO\n')

        print('A gjendet dita juaj e lindjes ne kete bllok: \n'
                      '16  17   18    19\n'
                      '10  21   22    23\n'                      
                      '24  25   26    27\n'
                      '28  29   30    31\n')
        pergjigja5=input('Pergjigju me PO ose JO\n')

        mesazhi = pergjigja1 + ' ' + pergjigja2 + ' ' +  pergjigja3 + ' ' +   pergjigja4 + ' ' +  pergjigja5
        klientisocket.sendto(mesazhi.encode('utf-8'),(Hosti,Porti))
        mesazhipranuar,serveradresa=klientisocket.recvfrom(1024)
        print('Kemi marrur me sukses pergjigjen nga serveri-Ditelindja ')
        print(mesazhipranuar.decode('utf-8'))
        inputRina=input('shtypni P nese doni te vazhdoni tek metodat e Valmires , shtypni J nese doni tjera')
        if(inputRina=='P'):
           cls()
           Valmira()
        else:
           perfundo()
        klientisocket.close()
def lotaria():
      try:
           edhenaMarrur1=input('Shtypni nje numer nga 1 deri 100 ne formatin: LOTARIA numri\n')
           funksioni1,numri=edhenaMarrur1.split(' ')
           if(funksioni1=='LOTARIA'):
               numri1=int(numri)
               if(numri1>0 & numri1<101):
                klientisocket.sendto(edhenaMarrur1.encode('utf-8'),(Hosti,Porti))
                mesazhipranuar,serveradresa=klientisocket.recvfrom(1024)
                print(mesazhipranuar.decode('utf-8'))
                inputRina=input('shtypni P nese doni te vazhdoni tek metodat e Rrezartes , shtypni J nese doni tjera')
                if(inputRina=='P'):
                   cls()
                   Valmira()
                else:
                  perfundo()
           else:
                   print('Numri i dhene nuk eshte ne kete interval[1-100]')
      except:
          print('gabim  formati ose fonet ka ndaluar ose klientserveri ka ndaluar!!')
          perfundo()
def Konverto():
      try:
              messageKonverto=input('Shkruani konertimet qe deshironi te beni:\n'
                             'CelciusToFarenhajt\n'
                             'FarenhajToCelcius\n'
                             'CelciusToKelvin\n'
                             'KelvinToCelcius\n'
                             'KelvinToFarenhajt\n'
                             'FarenhajtToKelvin\n'
                             'KilogramToPound\n'
                             'PoundToKilogram ' + 'dhe numri qe deshironi te konvertoni  p.sh KONVERTO CelciusToFarenhajt 5\n')
                  
              simboli=' '
              count=0
              for i in messageKonverto:
                     if i in simboli:
                         count=count+1
              
              if(count==2):
                       a,b,c=messageKonverto.split(' ')
                       if(a=='KONVERTO'):
                           dergimi=b+' '+c
                           klientisocket.sendto(dergimi.encode('utf-8'),(Hosti,Porti))
                           mesazhipranuar,serveradresa=klientisocket.recvfrom(1024)
                           print(mesazhipranuar.decode('utf-8'))
                       
              else:
                  print('Nuk keni shkruar formatin e duhur!!!')
              inputi1=input('shtypni K nese deshironi te vazhdoni me konvertime, Shtypni J per tjera')
              if(inputi1=='K'):
                      cls()
                      Konverto()
              if(inputi1=='J'):
                  perfundo()
      except:
          print('Gabime ne format ose klientserveri ka ndaluar')
                       
#Foni Perfundo:
def perfundo():
    Pergjigja=input('Nese deshironi ta perfundoni shtypni PO ,nese deshironi te vazhdoni shtypni JO\n')
    if(Pergjigja=='PO'):
        exit()
    if(Pergjigja=='JO'):
        cls()
    else:
        perfundo()
#--------------------------------------------------------------------#
while 1:    
    print('=================================================================\nMirsevini\n===============================================================\n')
    message=input('Per IP shtypni IP \n'
              'Nese deshironi te shkruani nje emer dhe te ktheni mbrapsht shtypni PRINTO:   \n'
              'Nese deshironi te dini sa zanore ka nje emer  shtypni ZANORE \n'
              'Nese deshironi te gjeni faktorielin e nje numri shtypni FAKTORIEL\n'
              'Nese deshironi te gjeni 20 numra nga rangu [1-80]\n shtypni KENO\n'
              'Nese deshironi te konvertoni shenoni KONVERTO\n'
              'Nese deshironi te gjeni kohen shtypni TIME\n'
              'Nese deshironi te gjeni HOSTIN shtypni HOSTI\n'
              'Nese deshironi te gjeni IP e klientit shtypni IP\n'
              'Nese deshironi te gjnei Portin ekomunikimit shtypni PORTI\n'
              'Nese deshironi te paraqiten funsionet e bera nga Rina Selmani shtypni RINA\n'
              'Nese deshironi te parqiten fonet e bera nga Rrezarta Mustafa shtypni RREZARTA\n'
              'Nese deshironi te parqiten fonet e bera nga Valmira Gllareva shtypni VALMIRA\n'
              'Nese deshironi te parqiten fonet e bera nga Ardian Qubreli shtypni ARDIAN\n'
              'Nese deshironi te perfundoni shtypni PERFUNDOJE\n')
   

#definimi f-oneve---------------->
 #PRANIMI DHE EKZEKUTIMI KODIT
    if(message=='PRINTO'):
       Printo()
       perfundo()
    if(message=='ZANORE'):
       Zanore()
       perfundo()
    if(message=='IP'):
       IP()
       perfundo()
    if(message=='FAKTORIEL'):
       Faktoriel()
       perfundo()
    if(message=='TIME'):
       Time()
       perfundo()
    if(message=='KENO'):
       Keno()
       perfundo()
    if(message=='KONVERTO'):
       Konverto()
       perfundo()
    if(message=='HOSTI'):
       Host()
       perfundo()
    if(message=='PORTI'):
       Port()
       perfundo()
    if(message=='RINA'):
       Rina()
    if(message=='RREZARTA'):
       Rrezja()
    if(message=='VALMIRA'):
       Valmira()
    if(message=='ARDIAN'):
       Ardian()
       perfundo()
    if(message=='PERFUNDOJE'):
        exit()
       
      
    else:
        cls()
    
    

          
          
        
