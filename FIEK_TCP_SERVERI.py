from socket  import *
from datetime import datetime
import random
import math
import sys
import os
PORTI=9000
ServeriHost='RRjeta'
ServeriSocket=socket(AF_INET,SOCK_STREAM)
ServeriSocket.bind(('',PORTI))
ServeriSocket.listen(5)
print('SOCKETI I KRUJUA ME SUKSES TANI MUND TE PRANOJ TE DHENA\n')
#--------------

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
#-------------
#DEFINIMI FUNSIONEVE------------------------------------------------------->
def Printo():     
              try:
                  print('Kemi marrur kerkesen nga klienti per ta derguar tekstin mbrapsht\n')
                  tekstiPrapa=b[::-1]#FUNSKIONI QE KTHEN TEKSTIN MBRAPSHT
                  Konektimi.send(tekstiPrapa.encode('utf-8'))
                  print('Pergjigja u dergua :) :)')
              except:
                     message='Foni Printo ka ndalur, provoni perseri!'
                     Konektimi.send(tekstiPrapa.encode('utf-8'))
def Zanore():
              try:
                  numro=0
                  
                 
                  print('Kemi marrur kerkesen nga klienti per te numruar zanoret\n')
                  for krk in b:
                      if(krk=='a' or krk=='A' or krk=='E' or krk=='e' or krk=='y' or krk=='Y' or krk=='i' or krk=='I'):
                        numro=numro+1
                      if(krk=='o' or krk=='O'):
                        numro=numro+1
                      if(krk=='u' or krk=='U'):
                        numro=numro+1
                  
                   
                  numro2=str(numro)
                  pergjigja=('Teksti derguar permban:'+numro2+'zanore')
                  Konektimi.send(pergjigja.encode('utf-8'))
                  print('Pergjigja u dergua :) :)')
              except:
                   print('Foni zanore ka ndalur, provoni perseri!')
def IP():       
              try:
                 print('Kemi marrur kerkesen nga klienti per ta derguar IP e tij\n')
                 Konektimi.send(b.encode('utf-8'))
                 print('Pergjigja u dergua :) :)')
              except:
                   print('Foni zanore ka ndalur, provoni perseri!')
def Emaili():   
              try:
                  print('Kemi marrur kerkesen nga klienti per te parcaktuar domenin e emailit '+b)
                  simboli='@'
                  simboli1='.'
                  domeni='Formati Gabim'
                  b1=str(b)
                  for i in b1:
                      if i in simboli:
                         r,g= b1.split('@')
                         for i in g:
                             if i in simboli1:
                                 r,t=g.split('.')
                                 domeni='Domeni i emailit tuaj '+b+' eshte  :'+str(r)
                  Konektimi.send(domeni.encode('utf-8'))
                  print('Pergjigja u dergua :) :)')
                                 
              except:
                  print('Gabime me metoden ose keni shkruar gabim formatin')
def Trekendeshi():
              try:
                  print('Kemi marrur kerkesen per llogaritjen e siperfaqes se trekendeshit')
                  B1=float(b)
                  C1=float(c)
                  Siperfaqja=str(B1*C1/2)
                  perimetri=str(3*C1)
                  pergjigja='Trekendeshi barabrinjes me brinje: '+c+' ka siperfaqe: '+Siperfaqja+'dhe perimeter: '+perimetri
                  Konektimi.send(pergjigja.encode('utf-8'))
                  print('Pergjigja u dergua :) :)')
              except:
                    print('Foni trekendeshi ka ndalur, provoni perseri!')
def Katrori():
              try:
                  print('Kemi marrur kerkesen per llogaritjen e siperfaqes se katrorit')
                  B1=float(b)
                  Siperfaqja=str(B1*B1)
                  Perimetri=str(4*B1)
                  pergjigja='Katrori me brinje: '+b+' ka siperfaqe: '+Siperfaqja+'dhe perimeter: '+Perimetri
                  Konektimi.send(pergjigja.encode('utf-8'))
                  print('Pergjigja u dergua :) :)')
              except:
                  print('Foni katrori ka ndalur, provoni perseri!')
def Rrethi():   
              try:
                 print('Kemi marrur kerkesen per llogaritjen e siperfaqes se rrethit')
                 R1=float(b)
                 Siperfaqja=str(3.14*R1*R1)
                 Perimetri=str(2*3.14*R1)
                 pergjigja='Rrethi me rreze '+b+' ka siperfaqen: '+Siperfaqja+'dhe perimeter: '+Perimetri
                 Konektimi.send(pergjigja.encode('utf-8'))
                 print('Pergjigja u dergua :) :)')
              except:
                   print('Foni rrethi ka ndalur, provoni perseri!')
def Faktoriel():
              try:
                 print('Kemi marrur kerkesen nga klienti per ta derguar faktorielin e numrit'+b)
                 b1=int(b)
                 print('\n')
                 i=1
                 faktorieli=1
                 while i<=b1:
                     faktorieli=faktorieli*i
                     i=i+1
                 faktorieliFund=str(faktorieli)
                 Konektimi.send(faktorieliFund.encode('utf-8'))
                 print('Pergjigja u dergua :) :)')
              except:
                   print('Foni faktoriel ka ndalur, provoni perseri!')
def Time():
              try:            
                  print('Kemi marrur kerkesen per te kthyer kohen nag serveri\n')
                  koha= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                  Konektimi.send(koha.encode('utf-8'))
                  print('Pergjigja u dergua :) :)')
              except:
                  print('Foni Time ka ndaluar')
def Hosti():
              try:
                print('Kemi marrur kerkesen nga klienti per te kthyer Hostin\n')
                Pergjigja='Hosti i kientit eshte:'+ServeriHost
                Konektimi.send(Pergjigja.encode('utf-8'))
                print('Pergjigja u dergua :) :)')
              except:
                 print('Foni ka ndaluar\n')
                 Pergjigja='Hosti Klientit nuk eshte gjetur!!!'
                 Konektimi.send(Pergjigja.encode('utf-8'))
def Port():
             try:
                print('Kemi marrur kerkesen per te kthyer Portin nga serveri\n')
                Pergjigja='Porti i komunikimit eshte: '+str(PORTI)
                Konektimi.send(Pergjigja.encode('utf-8'))
                print('Pergjigja u dergua :) :)')
             except:
                print('Foni ka ndaluar')
def Konverto1():
              try:
                 print('Kemi marrur kerkesen nga klienti per ta shnderruar CelciusToFarenhajt temperature:')
                 a1=int(b)
                 farenhajt=(1.8 * a1)+32
                 Dergesa='Temperatura e konvertuar nga '+b+' Celcius eshte '+str(farenhajt)+' Farenhajt'
                 Konektimi.send(Dergesa.encode('utf-8'))
                 print('Pergjigja u dergua :) :)')
              except:
                   print('Foni per te konvertuar temperaturen  ka ndalur, provoni perseri!')
def Konverto2():
              try:
                 print('Kemi marrur kerkesen nga klienti per ta shnderruar FarenhajToCelcius temperature:')
                 a1=int(b)
                 celcius=(a1-32)*1.8
                 Dergesa='Temperatura e konvertuar nga '+b+' Farenhajt eshte '+str(celcius)+' Celcius'
                 Konektimi.send(Dergesa.encode('utf-8'))
                 print('Pergjigja u dergua :) :)')
              except:
                   print('Foni per te konvertuar temperaturen  ka ndalur, provoni perseri!')
                   
def Konverto3():
              try:
                 print('Kemi marrur kerkesen nga klienti per ta shnderruar CelciusToKelvin temperature:')
                 a1=float(b)
                 kelvin=a1+273.15
                 Dergesa='Temperatura e konvertuar nga '+b+' Celcius eshte '+str(kelvin)+' Kelvin'
                 Konektimi.send(Dergesa.encode('utf-8'))
                 print('Pergjigja u dergua :) :)')
              except:
                   print('Foni per te konvertuar temperaturen  ka ndalur, provoni perseri!')
                   
def Konverto4():
              try:
                 print('Kemi marrur kerkesen nga klienti per ta shnderruar KelvinToCelcius temperature:')
                 a1=int(b)
                 celcius=a1-273.15
                 Dergesa='Temperatura e konvertuar nga '+b+' Kelvin eshte '+str(celcius)+' Celcius'
                 Konektimi.send(Dergesa.encode('utf-8'))
                 print('Pergjigja u dergua :) :)')
                 
              except:
                   print('Foni per te konvertuar temperaturen  ka ndalur, provoni perseri!')
                   
def Konverto5():
              try:
                 print('Kemi marrur kerkesen nga klienti per ta shnderruar KelvinToFarenhajt temperature:')
                 a1=int(b)
                 farenhajt=1.8*(a1-273.15)+32
                 Dergesa='Temperatura e konvertuar nga '+b+' Kelvin eshte '+str(farenhajt)+' farenhajt'
                 Konektimi.send(Dergesa.encode('utf-8'))
                 print('Pergjigja u dergua :) :)')
               
              except:
                   print('Foni per te konvertuar temperaturen  ka ndalur, provoni perseri!')
                   
def Konverto6():
              try:
                 print('Kemi marrur kerkesen nga klienti per ta shnderruar FarenhajtToKelvin temperature:'+a)
                 a1=int(b)
                 Kelvin=((a1-32) * 1.8)+273.15
                 Dergesa='Temperatura e konvertuar nga '+b+' Farenhajt eshte '+str(Kelvin)+' Kelvin'
                 Konektimi.send(Dergesa.encode('utf-8'))
                 print('Pergjigja u dergua :) :)')
              except:
                   print('Foni per te konvertuar temperaturen  ka ndalur, provoni perseri!')
                   
def Konverto7():
              try:
                 print('Kemi marrur kerkesen nga klienti per ta shnderruar KilogramToPound peshe:'+a)
                 a1=int(b)
                 pound=2.2046 * a1
                 Dergesa='Pesha e konvertuar nga '+b+' Kilogram eshte '+str(pound)+' Pound'
                 Konektimi.send(Dergesa.encode('utf-8'))
                 print('Pergjigja u dergua :) :)')
              except:
                   print('Foni per te konvertuar temperaturen  ka ndalur, provoni perseri!')
                   
def Konverto8():
              try:
                 print('Kemi marrur kerkesen nga klienti per ta shnderruar PoundToKilogram :'+a)
                 a1=int(b)
                 kilogram=a1/2.2046
                 Dergesa='Pesha e konvertuar nga '+b+' pound eshte '+str(kilogram)+' Kilogram'
                 Konektimi.send(Dergesa.encode('utf-8'))
                 print('Pergjigja u dergua :) :)')
              except:
                   print('Foni per te konvertuar temperaturen  ka ndalur, provoni perseri!')
def Keno():  
              try:  
                print('Kemi marrur kerkesen per te derguar 20 numra nga rangu [1-80]\n')
                keno=''
                for i in range(20):
                    p=random.randint(1,80)
                    if(str(i)=='0'):
                      keno=str(p)
                    else:
                      keno=str(p)+','+keno
                Konektimi.send(keno.encode('utf-8'))
                print('Pergjigja u dergua :) :)')
              except:
                  print('Foni keno ka ndaluar')

def ditelindja():
               dita=0
               try:
                if(a == 'PO'):
                           dita=dita+1
                if(b == 'PO'):
                           dita=dita+2
                if(c == 'PO'):
                           dita=dita+4
                if(d == 'PO'):
                           dita=dita+8
                if(e == 'PO'):
                          dita=dita+16 
                shfaq='Ditelindja juaj eshte me daten: '+str(dita)
                Konektimi.send(shfaq.encode('utf-8'))
                print('Pergjigja u dergua :) :)') 
                                     
               except:
                          print('Foni per Ditelindje ka ndalur, provoni perseri!')
def Lotaria():
               try:
                 i=random.randint(1,100)
                 bprova=int(b)
                 b1=bprova/10
                 b2=bprova%10
                 i1=i/10
                 i2=i%10
                 if(bprova==i):
                        s='Numrat u perputhen :ju fituat $100.000' 
                 if(b1==i1 and b2==i2):
                        s='Te gjith numrta u perputhen :ju fituar $50.000 dollar'
                 if(b1==i1 or b1==i2 or  b2==i2  or b2==i1):
                        s='Vetem nje numer eshte perputhur keni fituar $2500'
                 else:
                        s='Na vjen keq,asnje numer nuk eshte perputhur.PROVOJENI PRAP'
            
                 Konektimi.send(s.encode('utf-8'))
                 print('Pergjigja u dergua :) :)') 
                 
                           
               except:
                   print('Foni per Lotari ka ndalur, provoni perseri!')
#fonet e ardianit
def Rangu():
                try:
                   print('Kemi marrur kerkesen nga klienti per te llogaritur numrin e numrave te thjeshte mes rangut te caktuar')
                   p = 2
                   j = 0
                   x=int(b)
                   while p <= x:
                     for i in range(2, p):
                        if p%i == 0:
                                p=p+1 
                                p=p+1
                                j=j+1
                   numriTotal=str(j)
                   Konektimi.send(numriTotal.encode('utf-8'))
                   print('Pergjigja u dergua :) :)')
                except:
                   vendi='gabim'
                   print('Foni Rangu ka ndalur, provoni perseri!')
                   Konektimi.send(vendi.encode('utf-8'))

       
def TEK():
                 try:
                  print('Kemi marrur kerkesen nga klienti per te llogaritur numrin e numrave tek mes rangut te caktuar')
                  y=int(b)
                  numratTek = 0  
                  for x in range(1,y):
                   if not x % 2:  
                     numratTek+=1  
                  numTek=str(numratTek)
                  Konektimi.send(numTek.encode('utf-8'))
                  print('Pergjigja u dergua :) :)')
                 except:
                  print('Foni TEK ka ndalur, provoni perseri!')
                   

while 1:
       Konektimi,adresa=ServeriSocket.accept()
       Edhena=Konektimi.recv(1024)
       EdhenaMarrur=str(Edhena.decode('utf-8'))
      
        
        #Fillimi kodit ku behet ndarja e te dhenes qe eshte derguar me qellim qe te dihet cfare opeeracioni do behet me te!!!
       simboli=' '
       numro=0
       try:
           for i in EdhenaMarrur:
              if i in simboli:
                numro=numro+1
           if(numro==0):
              #Fillimi kodit per te kthyer Time
              if(EdhenaMarrur=='TIME'):
                 Time()
              if(EdhenaMarrur=='KENO'):
                 Keno()
              if(EdhenaMarrur=='HOSTI'):
                 Hosti()
              if(EdhenaMarrur=='PORTI'):
                 Port()
           if(numro==1):
              a,b=EdhenaMarrur.split(' ')
        #Fillimi kodit per kthimin  e inputit mbrapsht
              if(a=='PRINTO' or a=='printo'):
                 Printo()
        #Fillimi kodit per te kthyer IPadresen
              if(a=='IP' or a=='ip'):
                 IP()
        #Fillimi kodit per te numruar sa zanore ka nje fjale
              if(a=='ZANORE'or a=='zanore'):
                  Zanore()
                  #Fillimi kodit per te kthyer Faktorielin
              if(a=='FAKTORIEL' or a=='faktoriel'):
                 Faktoriel()
               
              if(a=='KATRORI'):
                  print('hyri')
                  Katrori()
              if(a=='RRETHI'):
                 Rrethi()
              if(a=='Emaili'):
                 Emaili()
                 #fonet konverto
              if(a=='CelciusToFarenhajt'):
                 Konverto1()
                 
              if(a=='FarenhajtToCelcius'):
                 Konverto2()
              
              if(a=='CelciusToKelvin'):
                 Konverto3()
              if(a=='KelvinToCelcius'):
                 Konverto4()
              if(a=='KelvinToFarenhajt'):
                 Konverto5()
              if(a=='FarenhajtToKelvin'):
                 Konverto6()
              if(a=='KilogramToPound'):
                 Konverto7()
              if(a=='PoundToKilogram'):
                 Konverto8()
              if(a=='PERFECTNUMBER'):
                 Perfectnumber()
              if(a=='QYTETI'):
                 Qyteti()
              if(a=='LOTARIA'):
                 Lotaria()
              if(a=='TEK'):
                 TEK()
              if(a=='RANGU'):
                 Rangu()
                 #---------------------
           if(numro==2):
             a,b,c=EdhenaMarrur.split(' ')
             if(a=='TREKENDESHI'):
               Trekendeshi()
           if(numro==4):
               a,b,c,d,e=EdhenaMarrur.split(' ')
               ditelindja()
            
       except ValueError:
            print('Kemi probleme me Serverin, ju lutem provoni perseri!!')
              
         #-------------------------------------------------------------------------------------------------------PERFUNDIMTARE----------->

Konektimi.close()
               
