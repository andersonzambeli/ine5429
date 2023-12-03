from multiprocessing import Process, Pipe
import random
import time
from phe import paillier


def votante(conn_vc, conn_vr, num_voters):

    public_key: paillier.PaillierPublicKey = None
    key = conn_vr.recv()
    public_key = key
    print("Chave publica recebida pelos votantes:")
    print(public_key)


    config = 2

    conn_vc.send(public_key.encrypt(0))



    if (config == 1):

        for i in range(0,num_voters):

            num  = random.randint(1,2)
            if (num == 1):
                vote = "a"
            
            if (num == 2):
                vote = "b"

            if( vote == "a"):
                conn_vc.send(public_key.encrypt(1))

            if(vote == "b"):
                conn_vc.send(public_key.encrypt(1 << 8))


    if(config == 2):

        votes = ['a', 'a', 'a', 'a', 'b', 'a', 'a', 'a', 'a', 'b']
        for i in range(0,num_voters):

            vote = votes[i]
            

            if( vote == "a"):
                conn_vc.send(public_key.encrypt(1))
                
            if(vote == "b"):
                conn_vc.send(public_key.encrypt(1 << 8))
            
            print("Voto " + str(i) + " enviado.\n")
    
    
    conn_vr.close()
    conn_vc.close()


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

    start_time = time.perf_counter()

    num_voters = 10

    public_key, private_key = paillier.generate_paillier_keypair(None , 2048)
    print("Chave publica gerada:")
    print(public_key)
    conn_rv, conn_vr = Pipe()
    conn_vc, conn_cv = Pipe()
    conn_rc, conn_cr = Pipe()
    p = Process(target=votante, args=(conn_vc, conn_vr, num_voters))
    conn_rv.send(public_key)
    p.start()
    p = Process(target=contador, args=(conn_cv, conn_cr, num_voters))
    p.start()
    
    resultado = private_key.decrypt(conn_rc.recv())
    votos_b = resultado >> 8
    votos_a = resultado - (votos_b << 8)

    print("Votos para A:")
    print(votos_a)
    print("Votos para B:")
    print(votos_b)
    
    
    p.join()

    print("\n--- %s seconds ---" % (time.perf_counter() - start_time))