import random
import time

def find_next_probable_prime(num, iters): # função que recebe um número e calcula o proximo primo a partir dele, ou o próprio numero caso ele seja primo
    
    if (num % 2 == 0): # se o numero for par, transforma em ímpar somando 1
        num = num + 1
    miller = Miller_rabin(iters) # cria o teste de Miller-Rabin
    res = False
    while(res == False): # enquanto o resultado do teste for falso, soma 2 ao numero e faz o teste de novo 
        res = miller.is_prime(num)
        if(res == True): # se o resultado for verdadeiro mostra o numero gerado e termina o teste
            print(num)
            print("Provavelmente primo")
            break
        else:
            num = num + 2
    


class Miller_rabin: # classe que implementa o teste de miller-rabin
    
    
    def __init__(self, k): # k é o numero de vezes que o teste rodara para um numero dado
        
        self.num = None
        self.k = k

    def is_prime(self, numero): # função que testa um numero
        
        self.num = numero
       
        
        if(self.num == 1 or self.num == 2 or self.num == 3 ): # casos bases
            #print("Primo")
            return True
       
        
        if(self.num % 2 == 0): # checa se numero é par e se for retorna falso para o numero passado
            #print("Composto")
            return False
    
        
        r = 0   
        d = self.num - 1
        while d % 2 == 0: # acha r e d tal que n-1 = (2 ^ r) * d
            d //= 2
            r += 1
        #print(d)
        #print(r)

        for i in range(0, self.k): # faz o test para k iterações passadas pelo usuário
            
            rnd = random.randint(2, self.num - 2) # escolhemos um número aleatório entre 2 e numero - 2
            
            x = pow(rnd, d, self.num) # achamos a valor de rnd elevado a D e tirmos o modulo com o numero 
            
            if x == 1 or x == self.num - 1: # se x for 1 ou numero - 1, o numero é um provavel primo 
                return True
            
            for j in range(0 , r - 1):
                x = pow(x, 2, self.num)  
                if x == self.num - 1:  
                    break
            else:
                #print("Composto")
                return False
        
        #print("Provavelmente primo")
        return True

start_time = time.perf_counter()   
mil = Miller_rabin(1)
# err = False
# while(err == False):
#     err = mil.is_prime(74665)
#     if(err == True):
#         print(err)
#         break
res = mil.is_prime(74665)


#find_next_probable_prime(554385705565953163597750325476111003302981660521164333133862474489159397873474187519460861938313861743513813194960931445654983723205275382995238132926443627342793003253567638421276850268682946303633926463092674593406811888271655782968152278864252164984954408955027875107415196085158388427962209424378329868119630256965540646158591419027747854675339833023790135189603117938471391568424071105674563398901567170287915177430510212191696149052212766743867318746972293164878038258339753794045670080385837709720928629816945711883957319355563109203666043944743108077841280562858291398584603690267918411763957173600050388353990896337097965403701719812801618091795594080584408042632821883033348959155419069842888069624002919756541799466060999268429479218028230592930619716844395126441710297352204693790282786249296046705741902614607809481439297871992205918745783224506122889720874045480562883978986403810786390327272938257420344292238663688215078451742601337467190786761162581890333335846706549234646351476575722725604362574122892624050241786470091801250150221133832222343043625020919525224822366333878762168691159855190140799773344839596209079377562744821382172329794379264198764, 1)

print("--- %s seconds ---" % (time.perf_counter() - start_time))
print(res)
