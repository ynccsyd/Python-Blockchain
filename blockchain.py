# İstenen sayıda blok oluşturabilen PYTHON kodu
#timestamp zaman damgasını ve
# hash algorimaları oluştur
import datetime   
import hashlib

#blokta yer alacak verileri tanımla

class Block:
   
    block_No = 0  # blok sayısı
    data = None  # blokta saklanan veri
    next = None
    nonce = 0
    hash = None
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    
    def __init__(self, data):
        self.data = data
# proof of work için SHA256 kullanıldı
# bu protokol sayısal imza standardında kullanılmak üzere 
# tasarlanmış bir şifreleme algoritmasıdır. 
#Algoritmaların hızlı çalışması için verinin kendisi değil özeti imzalanır.
    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.block_No).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.nonce).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') 
        )
        # hexademical'a dönüştür
        return h.hexdigest()
      
    def __str__(self):
        #blok değerlerini yaz
        return  "index: " + str(self.block_No) +  "\nTimestamp: " + str(self.timestamp) + "\nData: " + str(self.data) +"\nPrevious Hash: " + str(self.previous_hash) + "\nBlock Hash: " + str(self.hash())  + "\nHashes: "  + str(self.nonce) + "\n--------------"
  
# zincir yapısını oluştur
class Blockchain:
    
    diff = 20                   # madencilikteki zorluk
    maxNonce = 2**32
    target = 2 ** (256-diff)
    block = Block("Genesis")     # İlk bloğu oluştur
    head = block
    
    def add(self, block):
        
        # Bİr önceki blokğun hash i ile yeni hash oluştur
        block.previous_hash = self.block.hash()
        block.block_No = self.block.block_No + 1  #zincire ekleyerek devam et
        self.block.next = block
        self.block = self.block.next

    # bloğun zincire eklenip eklenmeyeceğinin kararını oluştur
    def mine(self, block):
        for n in range(self.maxNonce):
    #verilen bloğun hash değeri hedef değerimizden az mı?
    #öyle ise bloğu ekle
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1
  
blockchain = Blockchain()

#istenilen sayıda madencilik yapar şimdi 7 blok için
for n in range(7):
    blockchain.mine(Block("Block " + str(n+1)))
    
#her bloğu zincirde yaz
while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next
    