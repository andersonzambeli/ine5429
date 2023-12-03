from multiprocessing import Process, Pipe
import random
import time
from phe import paillier

# Processo do votante
def votante(conn_vc, conn_vr, num_voters):

    # Votante espera receber do responsável a chave pública
    public_key: paillier.PaillierPublicKey = None
    key = conn_vr.recv()
    public_key = key
    #print("Chave publica recebida pelos votantes:")
    #print(public_key)

    # Configuração dos votos, 1 é geração aleatória e 2 é os votos colocados no em um vetor de votos
    config = 2

    # Votante manda primeiro o valor de votos igual a zero para o contador
    conn_vc.send(public_key.encrypt(0))


    # Configuração 1
    if (config == 1):

        for i in range(0,num_voters):
            # Numero aleatorio entre 1 e 2 para saber se voto vai ser em A, caso o numero seja 1 ou B se for 2
            num  = random.randint(1,2)
            if (num == 1):
                vote = "a"
            
            if (num == 2):
                vote = "b"

            # Se o voto for em A envia 1 para o contador
            if( vote == "a"):
                conn_vc.send(public_key.encrypt(1))

            # Se o voto for B envia 1 shiftado para a esquerda por 8 ao contador
            if(vote == "b"):
                conn_vc.send(public_key.encrypt(1 << 8))

    # Configuração 2 onde o vetor votes guarda os votos, assim podemos ver o votos e mudar para ver o resultado final
    if(config == 2):
        
        print("\n Vetor de votos:")
        votes = ['a', 'a', 'a', 'a', 'b', 'a', 'a', 'a', 'a', 'b']
        print(votes)
        print('')
        for i in range(0,num_voters):

            vote = votes[i]
            

            if( vote == "a"):
                conn_vc.send(public_key.encrypt(1))
                
            if(vote == "b"):
                conn_vc.send(public_key.encrypt(1 << 8))
            
            print("Voto " + str(i) + " enviado.\n")
    
    
    conn_vr.close()
    conn_vc.close()

# Processo do Contador
def contador(conn_cv, conn_cr, num_voters):

    resultado_crypt = conn_cv.recv()
    

    for i in range(0, num_voters):
        temp = conn_cv.recv()
        
        resultado_crypt = resultado_crypt + temp
        print("Voto " + str(i) + " recebido. O texto do voto: " + str(temp.ciphertext()))
        print('')
        pass
    conn_cr.send(resultado_crypt)
    conn_cr.close()
    conn_cv.close()

if __name__ == '__main__':

    start_time = time.perf_counter() # variavel que seta quando começou o programa

    num_voters = 10 # numeros de votantes

    # Aqui geramos as duas chaves da criptografia, a publica e a privada. Podemos escolher o tamanho das chaves mudando o segundo argumento
    # da função generate_paillier_keypair
    public_key, private_key = paillier.generate_paillier_keypair(None , 128)
    print("Chave publica gerada:")
    print(public_key)

    # Aqui estamos criando pipes para fazer a comunicação entre os processos onde a primeira letra apos o conn diz de qual processo sai a mensagem e a segunda
    # o processo destino. Por exemplo conn_rv comunicação com mensagem saindo do responsável (r) e indo para votante(v)
    conn_rv, conn_vr = Pipe()
    conn_vc, conn_cv = Pipe()
    conn_rc, conn_cr = Pipe()

    # Criação do processo dos votantes e já enviando a chave publica para ele
    p = Process(target=votante, args=(conn_vc, conn_vr, num_voters))
    conn_rv.send(public_key)
    p.start()

    # Criação do processo do contador
    p = Process(target=contador, args=(conn_cv, conn_cr, num_voters))
    p.start()
    
    # Responsável espera resultado da contagem chegar pelo pipe
    resultado = private_key.decrypt(conn_rc.recv())
    
    # responsável separa o valor dos votos de A e B no inteiro recebido
    votos_b = resultado >> 8
    votos_a = resultado - (votos_b << 8)

    # Mostra o valores de votos
    print("Votos para A:")
    print(votos_a)
    print("Votos para B:")
    print(votos_b)
    
    
    p.join()

    # Mostra o tempo que levou a execução do programa
    print("\n--- %s seconds ---" % (time.perf_counter() - start_time))