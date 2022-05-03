import random

individuo1 = [1, 2, 3, 4, 5, 6, 8, 9]
individuo2 = random.sample(individuo1, len(individuo1))
indAnterior1 = individuo1
indAnterior2 = individuo2
print("Lista 2: ",individuo2)
print('\n')

c = [3,6]
c1 = min(c)
c2 = max(c)
lc = c2 - c1 + 1

porcion1 = individuo1[c1:c2+1]
porcion2 = individuo2[c1:c2+1]

individuo1[c1:c2+1] = porcion2
individuo2[c1:c2+1] = porcion1

l = len(individuo1)

print("Individuo 1: ",individuo1)
print("Individuo 2: ",individuo2)


relleno = []

if c2 != len(indAnterior1):
    k = c2 + 1
else:
    k = 0



    

while(1):
    it = 0

    


    # for h in range(c1, c2+1):       #if in porcion
    #     #print(k)
    #     if indAnterior1[k] == individuo1[h]:
    #         if k == (len(indAnterior1)-1):
    #             k = 0
    #         else: 
    #             k += 1
    #         break
    #     else: 
    #         it += 1
        
    # if it == lc:
    #     relleno.append(indAnterior1[k])
    #     if k == (len(indAnterior1)-1):
    #         k = 0
    #     else: 
    #         k += 1
    
    # if k == (c2 + 1):
    #     break

print("Relleno: ", relleno)