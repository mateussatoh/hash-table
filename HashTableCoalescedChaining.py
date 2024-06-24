class HashTableCoalescedChaining:
    def __init__(self, size=100, hashMethod = 'multiplication'):
        self.size = size
        self.hashMethod = hashMethod
        self.table = [None] * size
        self.next = [-1] * size

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
        if self.table[index] is None:
            self.table[index] = key
            self.next[index] = -1
            print(f'{key} inserted at position {index}')
        else:
            print(f'Collision occurred at position {index}, resolving...')
            current = index
            while self.next[current] != -1:
                current = self.next[current]
            for i in range(self.size):
                if self.table[i] is None:
                    self.table[i] = key
                    self.next[current] = i
                    self.next[i] = -1
                    print(f'{key} inserted at position {i}')
                    return
            print(f'Hash table is full, cannot insert {key}')

    def search(self, key):
        index = self.hashFunction(key, self.size)
        current = index
        while current != -1 and self.table[current] != key:
            current = self.next[current]
        if current == -1:
            print(f'{key} not found in the hash table')
            return False
        else:
            print(f'{key} found at position {current}')
            return True

    def remove(self, key):
        index = self.hashFunction(key, self.size)
        current = index
        prev = -1
        while current != -1 and self.table[current] != key:
            prev = current
            current = self.next[current]
        if current == -1:
            print(f'{key} not found in the hash table')
        else:
            if prev == -1:
                self.table[current] = None
                self.next[current] = -1
            else:
                self.next[prev] = self.next[current]
                self.table[current] = None
                self.next[current] = -1
            print(f'{key} removed from position {current}')

    def display_table(self):
        for index, key in enumerate(self.table):
            if key is not None:
                print(f'Position {index}: {key} -> Next: {self.next[index]}')

