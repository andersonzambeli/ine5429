
import time

def check_at_least_1_odd(l :list): # função que checa se o vetor dado tem pelo menos um valor ímpar
    check = False
    for i in range(0,len(l)): # se acha um valor ímpar termina 
        if (l[i] % 2 == 1):
            check = True
            break
    
    if (check == False): # se não acha um valor ímpar, faz o primeiro elemento se tornar ímpar
        if(l[0] != 0):
            l[0] = l[i] - 1
        else:
            l[0] = l[0] + 1


def get_nums_fromTime(l: list): # função que pega os ultimos dígitos do tempo entre a epoca de inicio e o tempo atual e coloca em uma lista
        
    time_ = int(time.time_ns())
    #print(time_)
        
    for i in range(0,10):
        t = time_ % 10
        l.append(t)
#         if(i==0):
#             l.append(1)
#         else:
#             l.append(0)
        time_ = time_//10
    
    print(l)
    check_at_least_1_odd(l) # checa se há pelo menos um numero impar
    print(l)

class Lagged_fib_generator: # classe que implemnta o LFG
    
    
    
    
    def __init__(self, max_): # max_ é o valor maximo de numero gerado, j e k são parametros da sequencia
        self.max = max_
        self.k = 10
        self.j = 7
        self.time = int(time.time())
        self.list_nums = []
        #self.get_nums_fromTime()
        self.counter = 0
    
    def get_nums_fromTime(self): # função que pega os primeiros valores para a sequencia mas internamente na classe
       
        for i in range(0,10):
           
            t = self.time % 10
            
            self.list_nums.append(t)
            self.time = self.time//10;
        print(self.list_nums)
        self.check_at_least_1_odd()
        print(self.list_nums)

    def check_at_least_1_odd(self): # funcçao que checa se há um numero ímpar, mas internamente na classe
        check = False
        for i in range(0,len(self.list_nums)):
            if (self.list_nums[i] % 2 == 1):
                check = True
                break
        
        if (check == False):
            if(self.list_nums[0] != 0):
                self.list_nums[0] = self.list_nums[i] - 1
            else:
                self.list_nums[0] = self.list_nums[0] + 1
           
    
    def n_rand(self, n): # função que calcula um termo n da sequencia
        
        if (n < 10): # caso onde n é um dos k priemiros termos
            return self.list_nums[n]
        else:
            list_temp = self.list_nums.copy() # faz uma cópia da lista
            for i in range(self.k,n+1): # loop para calcular os novos termos a partir de k até n 
                s2 = (list_temp[self.k - self.j] + list_temp[self.k - self.k]) % self.max # formula de recorrencia do LFG
#                 print("    List_tem antes:    " + str(list_temp))
#                 print("    s2 = " + str(s2))
                list_temp.pop(0) # aqui atualizamos a lista para que ela tenha somente os ultimos k elementos da sequencia
                list_temp.append(s2)                   
#                 print("    List_tem depois:    " + str(list_temp))
#                 print("\n")   
                          
            return list_temp[9] # retorna o ultimo elemento

    def n_rand2(self, l: list): # função similar anterior, porém calcula a partir de uma lista de numeros iniciais qualquer
        list_temp = l.copy()
        s2 = (list_temp[self.k - self.j] + list_temp[self.k - self.k]) % self.max
        #print("    List_tem antes:    " + str(list_temp))
        #print("    s2 = " + str(s2))
        list_temp.pop(0)
        list_temp.append(s2)
        self.counter = self.counter + 1
        #print("    List_tem depois:    " + str(list_temp))
        #print("\n")   
                          
        return list_temp
        
                
                
def call_fib_gen(bits): # função que acha um numero com pelo menos o numero de bits passado 
    fib = Lagged_fib_generator(2**bits - 1) # cria o gerador com o valor máximo
    i = 0
    val = -1
    #print(val.bit_length())
    list_: list = []
    get_nums_fromTime(list_)
    #print(list_)
    
    while( val.bit_length() < bits): # gera o proximo termo da sequencia até achar o primeiro que tem o numero mínimo de bits
        list_ = fib.n_rand2(list_)
        #print (list_)
        val = list_[9]
        #print(val.bit_length())
    print(fib.counter)
    return val



#print(time.time())
start_time = time.perf_counter()
randomval = call_fib_gen(100)
print(randomval)
print(randomval.bit_length())
print("--- %s seconds ---" % (time.perf_counter() - start_time))


        
        
