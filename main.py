from HashTableCoalescedChaining import HashTableCoalescedChaining
from HashTableOpenAddressing import HashTableOpenAddressing
from HashTableSeparateChaining import HashTableSeparateChaining

print('Selecione a função hash:') 
print('(A) - Divisão') 
print('(B) - Dobra') 
print('(C) - Multiplicação') 
hashMethodInput = input()

hashMethod = 'division'
if(hashMethodInput == 'A'):
    hashMethod = 'division'
elif(hashMethodInput == 'B'):
    hashMethod = 'folding'
elif(hashMethodInput == 'C'):
    hashMethod = 'multiplication'
else:
    raise Exception("Input inválido")

print('Selecione o tratamento de colisão:') 
print('(A) - Encadeamento Exterior') 
print('(B) - Encadeamento Interior') 
print('(C) - Endereçamento Aberto') 
colisionMethodInput = input()

colisionMethod = 'open'
if(colisionMethodInput == 'A'):
    hashTable = HashTableSeparateChaining(size=10, hashMethod=hashMethod)
elif(colisionMethodInput == 'B'):
     hashTable = HashTableCoalescedChaining(size=10, hashMethod=hashMethod)
elif(colisionMethodInput == 'C'):
     hashTable = HashTableOpenAddressing(size=10, hashMethod=hashMethod)
else:
    raise Exception("Input inválido")


runUserCommandsLoop = True

while(runUserCommandsLoop):
    print('Selecione a ação:') 
    print('(A) - Inserir') 
    print('(B) - Buscar') 
    print('(C) - Remover')
    print('(D) - Mostrar') 
    print('(E) - Sair') 

    action = input()

    if(action == 'A'):
        print('Insira o valor para inserir:') 
        value = input()
        hashTable.insert(value)
    elif(action == 'B'):
        print('Insira o valor para buscar:') 
        value = input()
        hashTable.search(value)
    elif(action == 'C'):
        print('Insira o valor para buscar:') 
        value = input()
        hashTable.remove(value)
    elif(action == 'D'):
        hashTable.display_table(value)
    elif(action == 'E'):
        runUserCommandsLoop = False
    else:
        runUserCommandsLoop = False
        raise Exception("Input inválido")


