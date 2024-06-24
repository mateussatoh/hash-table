class HashTableOpenAddressing:
    def __init__(self, size=100, hashMethod = 'multiplication'):
        self.size = size
        self.table = [None] * size
        self.hashMethod = hashMethod

    def hashFunction(self, key, size, attempt = 0): 
        if(self.hashMethod == 'division'):
            return self.hashDivision(key, attempt)
        elif(self.hashMethod == 'folding'):
            return self.hashFolding(key, size, attempt)
        elif(self.hashMethod == 'multiplication'):
            return self.hashMultiplication(key,size, attempt)           

    def hashFolding(key, size, attempt):
        key_str = str(key)
        sum_parts = 0

        # Split the key into parts of length 2
        for i in range(0, len(key_str), 2):
            part = key_str[i:i+2]
            sum_parts += int(part)

        return (sum_parts + attempt) % size

    def hashDivision(self, key, attempt):
        return (hash(key) + attempt) % self.size

    def hashMultiplication(key, size, attempt):
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
        return (int(middle_bits, 2) + attempt) % size


    def insert(self, key):
        for attempt in range(self.size):
            index = self.hashFunction(key, self.size ,attempt)
            if self.table[index] is None:
                self.table[index] = key
                print(f'{key} inserted at position {index}')
                return
        print(f'Hash table is full, cannot insert {key}')

    def search(self, key):
        for attempt in range(self.size):
            index = self.hashFunction(key, self.size, attempt)
            if self.table[index] == key:
                print(f'{key} found at position {index}')
                return True
            elif self.table[index] is None:
                break
        print(f'{key} not found in the hash table')
        return False

    def remove(self, key):
        for attempt in range(self.size):
            index = self.hashFunction(key, self.size, attempt)
            if self.table[index] == key:
                self.table[index] = None
                print(f'{key} removed from position {index}')
                return
            elif self.table[index] is None:
                break
        print(f'{key} not found in the hash table')

    def display_table(self):
        for index, key in enumerate(self.table):
            if key is not None:
                print(f'Position {index}: {key}')

