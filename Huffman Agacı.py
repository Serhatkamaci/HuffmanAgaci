
import time

def basla():
    
    def binarytoDecimal(sayi):

        toplam=0
        boyut=len(sayi)-1
        
        for i in sayi:

            carp=2**boyut
            toplam=toplam+(carp*int(i))
            boyut-=1

        return toplam


    deger=input("Bir sayi dizisi giriniz: ")

    bas=0
    son=8

    sayac=0
    degerListesi=[]

    while(sayac<(len(deger)/8)):

        degerListesi.append(deger[bas:son])
        bas+=8
        son+=8
        sayac+=1
    #print("Deger Listesi --> ",degerListesi)
    ascııDizisi=[]

    for i in degerListesi:

        sonuc=binarytoDecimal(i)
        #print(sonuc)
        ascııDizisi.append(chr(sonuc)) # Ascıı degere donusturmek icin kullandim.


    frekanslar={}


    for i in range(len(ascııDizisi)):

        if ascııDizisi[i] not in frekanslar:

            frekanslar[ascııDizisi[i]]=1

        else:

            frekanslar[ascııDizisi[i]]+=1

    frekanslar2=frekanslar.copy()
    frekanslar4=frekanslar.copy()

    print("Frekans dizisi --> ",frekanslar)        

    gercekDegerimiz=""

    for i in ascııDizisi:

        gercekDegerimiz+=i

    print("Bitler ile gercekte yazdigim deger --> ",gercekDegerimiz)
    print("\n\n")



    frekansDizisi=[]

    for i in frekanslar:

        frekansDizisi.append(frekanslar[i])

    # Frekanslarin kucukten buyuge dogru sıralanması.

    for i in range(len(frekansDizisi)):

        for j in range(len(frekansDizisi)):

            if frekansDizisi[i]<frekansDizisi[j]:

                tut=frekansDizisi[i]
                frekansDizisi[i]=frekansDizisi[j]
                frekansDizisi[j]=tut

    geciciFrekansDizisi=[]

    for i in frekanslar.keys():

        geciciFrekansDizisi.append(i)

    kontrol=0

    karakterSiralanmisHalleri=[]

    for i in frekansDizisi:

        for j in frekanslar:

            if i==frekanslar[j]:

                karakterSiralanmisHalleri.append(j)
                frekanslar[j]=-1 #Aynı frekans degerlerine sahip olan key degerleri olabilir.


    print("Frekans dizisinin siralanmis hali --> ",frekansDizisi)
    print("Karakter dizisinin siralanmis hali --> ",karakterSiralanmisHalleri)


    # Bundan sonraki adimlar icin frekanslar2 dizisine bakacagim.

    print(frekanslar2)

    karakterSiralanmisHalleri2=karakterSiralanmisHalleri.copy()
    karakterSayisi=len(frekanslar2) # Frekanslarina ayrilan karakterlerin toplam sayisi.
    print("Toplam karakter sayisi --> ",karakterSayisi)


    huffmanListesi=[]
    sayac=0
    print("\n\n")
    toplam=0
    liste=[]
    # Karakter listesinin tek elemanli olma durumunu kontrol et.


    def geleniSirala(liste):

        # Bu listenin icinde hem karakter hem de sayi var.

        frekanslar3=frekanslar2.copy()


        geciciListe=[]

        for i in karakterSiralanmisHalleri:

            if type(i)==str:

                geciciListe.append(frekanslar2[i])

            else:

                geciciListe.append(i) 

        for i in geciciListe:

            for j in geciciListe:

                if i<j:

                    tut=i
                    i=j
                    j=tut
        #print("Gecici Liste --> ",geciciListe)

        yeniListe=[]

        geciciListe2=geciciListe.copy()

        for i in geciciListe:

            for j in frekanslar3:

                if i==frekanslar3[j]:

                    yeniListe.append(j)
                    geciciListe2.remove(i)
                    frekanslar3[j]=-1
                    break

        #print("Gecici Liste ikinci gosterim --> ",geciciListe2)

        # Hala gecici listede eleman olabilir.

        if(len(geciciListe2)>0):

            for i in geciciListe2:

                yeniListe.append(i)

        #print("Yeni Liste --> ",yeniListe)
        return yeniListe


    while True:



        if(len(karakterSiralanmisHalleri))==0:
            break

        if type(karakterSiralanmisHalleri[0])==str:

            ilkEleman=karakterSiralanmisHalleri[0]
            liste.append(ilkEleman)
            toplam=toplam+frekanslar4[ilkEleman]
            #print("İlk eleman --> ",ilkEleman)
            karakterSiralanmisHalleri.pop(0)
            sayac+=1
            frekanslar2[ilkEleman]=-1
        else:
            ikinciEleman=karakterSiralanmisHalleri[0]
            liste.append(ikinciEleman)
            toplam+=ikinciEleman
            #print("İkinci eleman --> ",ikinciEleman)
            karakterSiralanmisHalleri.pop(0)
            sayac+=1

        if sayac==2:
            #print("Liste --> ",liste)
            huffmanListesi.append(liste)
            #print("Karakter dizisinin siralanmis hali --> ",karakterSiralanmisHalleri)    

            #print("Dizi ---> ",karakterSiralanmisHalleri)
            karakterSiralanmisHalleri=geleniSirala(karakterSiralanmisHalleri)


            karakterSiralanmisHalleri.insert(1,toplam)
            #print("Fonksiyona giden Karakter dizisinin siralanmis hali --> ",karakterSiralanmisHalleri)
            toplam=0
            liste=[]




            if len(karakterSiralanmisHalleri)==1:
                huffmanListesi.append([karakterSiralanmisHalleri[0]])
            sayac=0
    print("Huffman listesi --> ",huffmanListesi) # Bu listede en tepedekinin solunda kalan kısımlar hep 0 sagında kalanlar ise 1 olarak gidecek.
    # Agaci 2'li 2'li ciktim. Her seferinde toplam sonucunu ortaya alarak en kucuk sayi ile toplayip ilerledim.



    sonHaller={}
    huffmanUzunlugu=len(huffmanListesi)-1
    tepedekiEleman=huffmanListesi[huffmanUzunlugu][0] # Tepedeki elemanimizdir.
    print("Tepedeki Eleman --> ",tepedekiEleman)
    # Yukarıda tanımlamıs oldugum huffman listesinde en sonda yer alan eleman agacin tepesindeki elemandir.
    # Ondan once gelen listelerde yer alan sayilar(karakter olmayanlar) hep sag olarak karakterler ise sol olarak gelerek agacin yapraklarini olusturuyor.

    # Huffman listesinin her zaman saginda yer alan degerler onceki iki elmanin toplami ile elde edilen degerdir.

    # OLusturmus oldugum huffman agacimda her  zaman en asagida iki eleman digerlerinde ise 1 eleman olacak sekilde ilerliyor.

    # İlk olarak en asagida yer alan 2 karakterin yeni bit sayisini bulalim.

    # Simdi tepede yer alan sayiyi bulana kadar bit olarak toplama islemi gerceklestirecegim.

    toplam=""
    toplam2=""      
    birinciKarakter=huffmanListesi[0][0]
    ikinciKarakter=huffmanListesi[0][1]

    # En alt sol eleman icin.
    toplam+="0"

    # En alt sag eleman icin.
    toplam2+="1"    

    for i in range(1,len(huffmanListesi)):

        if huffmanListesi[i][0]==tepedekiEleman:
            break

        else:
            toplam+="1"
            toplam2+="1"

    sonHaller[birinciKarakter]=toplam[::-1]
    sonHaller[ikinciKarakter]=toplam2[::-1]
    karakterSayisi-=2
    sayac=1
    sayac2=2

    while(karakterSayisi>0):

        toplam=""

        toplam+="0"
        karakter=huffmanListesi[sayac][0]
        #print("Karakter --> ",karakter)

        for i in range(sayac2,len(huffmanListesi)):

            if huffmanListesi[i][0]==tepedekiEleman:
                break
            else:
                toplam+="1"

        sonHaller[karakter]=toplam[::-1]
        sayac+=1
        karakterSayisi-=1
        sayac2+=1
    print("\n\nKarakterlerin sıkıştırılmış halleri --> ",sonHaller)


    # Her zaman 0. ve sonuncu indeks dısındaki indekslerde "null" degeri verdim cunku bunlarin cocuklari yok.

    agacListesi='['
    agacListesi+=str(tepedekiEleman) # Kok degerini ekledim.
    huffmanListesi.pop()

    huffmanListesi=huffmanListesi[::-1]
    print("Hufmann Listesi --> ",huffmanListesi)


    for i in huffmanListesi:

        for j in i :

            k=","
            k+=str(j)
            agacListesi+=k

        agacListesi+=',null'
        agacListesi+=',null'

    agacListesi+="]"
    print("Agac Listesi --> ",agacListesi)
    
    
    print("\n----------------------------------------\n")
    
    print("Gercekteki bit sayısı --> ",len(deger))
    sonuc=0
    
    for i in gercekDegerimiz:
        
        decimal=binarytoDecimal(sonHaller[i])
        #print("binarytoDecimal(sonHaller[i])'nin decimal degeri --> ",decimal)
        sonuc+=decimal
        
    print("Sıkıştırma sonucunda elde etttiğimiz bit sayısı --> ",sonuc)
       
    print("\n----------------------------------------\n")
    
    
    class TreeNode:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
        def __repr__(self):
            return 'TreeNode({})'.format(self.val)

    def deserialize(string):
        if string == '{}':
            return None
        nodes = [None if val == 'null' else TreeNode(val)
                 for val in string.strip('[]{}').split(',')]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left  = kids.pop()
                if kids: node.right = kids.pop()
        return root

    def drawtree(root):
        def height(root):
            return 1 + max(height(root.left), height(root.right)) if root else -1
        def jumpto(x, y):
            t.penup()
            t.goto(x, y)
            t.pendown()
        def draw(node, x, y, dx):
            if node:
                t.goto(x, y)
                jumpto(x, y-20)
                t.write(node.val, align='center', font=('Arial', 12, 'normal'))
                draw(node.left, x-dx, y-60, dx/2)
                jumpto(x, y-20)
                draw(node.right, x+dx, y-60, dx/2)
        import turtle
        t = turtle.Turtle()
        t.speed(0); turtle.delay(0)
        h = height(root)
        jumpto(0, 30*h)
        draw(root, 0, 30*h, 40*h)
        t.hideturtle()
        turtle.mainloop()

    if __name__ == '__main__':
        drawtree(deserialize(agacListesi))
        
        
while True:
        
    print("\n\n1-)Huffman Algirtması ve Gorsellestirilmesi\n2-)Çıkış\n\n")
    
    durum=int(input("Yukarıda belirtilen durumlardan herhangi birini giriniz --> "))
     
    if durum==1:
        basla()
        
    elif durum==2:
        print("\n\nUygulamadan çıkış yapılıyor...")
        time.sleep(2)
        print("Uygulamayı kullandığınız için teşekkürler (:")
    
    elif durum>2:
        print("Yanlış seçim yaptınız.Lütfen yukarıda belirtilen seçimlerden herhangi birini giriniz (:\n")
        break
