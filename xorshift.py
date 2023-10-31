
import time

def truncate_num_bits(num, bits): # funçaõ que pega os primeiros bits pedidos de um numero num
    
    num_bin = bin(num)
    # print(num_bin)
    num_bin = num_bin[2:]
    # print(num_bin)    
    num_bin = num_bin[0:bits]
    # print(num_bin)
    num_bin = int(num_bin, 2)
    # print(num_bin)
    return num_bin
    


class Xorshift32_generator: # classe qye implementa o xorshift 32
    
    def __init__(self, seed, bits): 
        self.seed = seed
        self.bits = bits
        self.counter = 0
        
    
    def rand_xor(self, val): #rodada de uma iteração de xor shift
        num = val ^ (val << 17)
        num ^= num >> 7
        num ^= num << 5
        num = num % ((2**32) - 1)
        self.counter =  self.counter + 1
        #print("Valor num % : " + str(num))
        #print(num.bit_length())
        
        return num 
    
    def rand_xor_(self): # função que gera um número de self.bits de tamanho
        bit_val = -1 # numero de bits do numero
        val = 0
        res = ''
        while(bit_val < self.bits):  # enquato o valor de bits for menor que o dado pelo usuario, são criados numeros de até 32 bits
                                     # e eles são concatenados até passar o numero de bits pedido
            
            if (bit_val == -1):  # se bit_val é -1, vamos gerar o primeiro numero
                val = self.rand_xor(self.seed)
                #print("Valor : " + str(val))
            else:
                val = self.rand_xor(val)
                #print("Valor : " + str(val))
            
            res = res + str(val) # resulado da ooperação pega o valor gerado e concatena com o que tinha antes
            
            
            bit_val = int(res).bit_length() # atualiza o valor de bits
            
        res = truncate_num_bits(int(res), self.bits) # trunca para gera um valor com o número exato de bits
        #print(self.counter)
        
            
        return res
    
   
start_time = time.perf_counter()   
xor = Xorshift32_generator(int(time.time_ns()) , 40) # valor inicial dado pelo tempo entre a epoca de inicio e o tempo atual em nanosegundos e o numero de bits que o numero gerado precisa ter
#xor = Xorshift32_generator(2 , 32)
a = xor.rand_xor_()
a = int(a)
print(a)
print(a.bit_length())
print("--- %s seconds ---" % (time.perf_counter() - start_time))






