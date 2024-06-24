class HashTableSeparateChaining:
    def __init__(self, size=100, hashMethod = 'multiplication'):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.hashMethod = hashMethod

    def hashFunction(self, key, size): 
        if(self.hashMethod == 'division'):
            return self.hashDivision(key)
        elif(self.hashMethod == 'folding'):
            return self.hashFolding(key, size)
        elif(self.hashMethod == 'multiplication'):
            return self.hashMultiplication(key,size)           

    def hashFolding(key, size):
        key_str = str(key)
        sum_parts = 0

        # Split the key into parts of length 2
        for i in range(0, len(key_str), 2):
            part = key_str[i:i+2]
            sum_parts += int(part)

        return sum_parts % size

    def hashDivision(self, key):
        return hash(key) % self.size

    def hashMultiplication(key, size):
        constant = 0.61803398875  
        key = int(key)
        
        # Multiplica a chave pela constante A
        product = key * constant
        
        # Transforma o resultado em binário de 10 bits
        product_bin = bin(int(product * (2 ** 10)))[2:].zfill(10)
        
        # Remove as extremidades para obter 5 bits centrais
        if len(product_bin) > 10:
            product_bin = product_bin[-10:]  # Certifica que não exceda 10 bits
        middle_bits = product_bin[2:7]
        
        # Retorna o decimal desses 5 bits
        return int(middle_bits, 2) % size


    def insert(self, key):
        index = self.hashFunction(key, self.size)
        print(index)
        if key not in self.table[index]:
            self.table[index].append(key)
            print(f'{key} inserted at position {index}')
        else:
            print(f'{key} already exists in the hash table')

    def search(self, key):
        index = self.hashFunction(key, self.size)
        if key in self.table[index]:
            print(f'{key} found at position {index}')
            return True
        else:
            print(f'{key} not found in the hash table')
            return False

    def remove(self, key):
        index = self.hashFunction(key, self.size)
        if key in self.table[index]:
            self.table[index].remove(key)
            print(f'{key} removed from position {index}')
        else:
            print(f'{key} not found in the hash table')

    def display_table(self):
        for index, keys in enumerate(self.table):
            if keys:
                print(f'Position {index}: {keys}')

