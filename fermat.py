import time
import random


def find_next_probable_prime(num, iters): # função que recebe um número e calcula o proximo primo a partir dele, ou o próprio numero caso ele seja primo
    
    if (num % 2 == 0): # se o numero for par, transforma em ímpar somando 1
        num = num + 1
    fer = Fermat(iters) # cria o teste de Fermat
    res = False
    while(res == False): # enquanto o resultado do teste for falso, soma 2 ao numero e faz o teste de novo
        res = fer.is_prime(num)
        if(res == True): # se o resultado for verdadeiro mostra o numero gerado e termina o teste
            print(num)
            print("Provavelmente primo")
            break
        else:
            num = num + 2

class Fermat(): # classe que implenta o teste de fermat
    
    def __init__ (self, k): # k é o numero de vezes que o teste rodara para um numero dado
        
        self.num = 0 
        self.k = k
    
    def is_prime(self, number): # checa se um numero é primo pelo teorema de fermat 
        
         
        self.num = number
        
        if(self.num == 1 or self.num == 2 or self.num == 3 ): # considera os casos bases
            #print("Primo")
            return True
        
        for i in range(0, self.k): # verifica a o teorema de fermat para um k numeros aleatorios entre 2 e numero - 2
            rnd = random.randint(2, self.num - 2)
            if (pow(rnd, self.num - 1 , self.num) != 1):
                return False
        return True

start_time = time.perf_counter()   
fer = Fermat(1)
res = fer.is_prime(74665)
#find_next_probable_prime(20, 10)
print("--- %s seconds ---" % (time.perf_counter() - start_time))
print(res)

            