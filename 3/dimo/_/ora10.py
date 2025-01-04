#!/usr/bin/env python
# coding: utf-8

# 1. Valósítsd meg a paritásbites kódolást páratlanra való kiegészítéssel!
# 
# 

# In[ ]:


class ParCheckCode:
    def encode(self, data):
        ones_count = data.count('1')
        if ones_count % 2 == 0:
            data += "1"
        else:
            data += "0"
        return data
        
    def decode(self, cdata): # hibás szó estén jelezzük
        ones_count = cdata.count('1')
        
        if ones_count % 2 == 0:
            raise ValueError("paritas nem paratlan")
        return cdata[:-1]

p = ParCheckCode()
print(p.encode("1010"))
print(p.decode(p.encode("1010")))


# 2. Valósítsd meg a kétdimenziós paritásbites kódolást!
# 
# 

# In[ ]:


class TwoDimParCheckCode:
    self.p = ParCheckCode()
    
    def encode(self, data): # a legkisebb valódi osztó alapján darabold fel
        lvo = None
        for i in range(2, len(data) + 1):
            if len(data) % i == 0:
                lvo = i
        if lvo is None:
            lvo = len(data)
        rows = lvo
        cols = len(data) // lvo
        
        matrix = [list(data[i * cols:(i + 1) * cols]) for i in range(rows)]
        for i in range(rows):
            parity_bit = str(matrix[i].count('1') % 2)
            matrix[i].append(parity_bit)
                    
        last_row = []
        for j in range(cols + 1):
            col_bits = [matrix[i][j] for i in range(rows)]
            parity_bit = str(col_bits.count('1') % 2)
            last_row.append(parity_bit)
        matrix.append(last_row)
        return matrix
        
        
    def decode(self, cdata): # corrects 1 error, notifies if there is 2
        rows = len(cdata) - 1
        cols = len(cdata[0]) - 1
        error_row = None
        error_col = None
                
        for i in range(rows):
            parity_bit = str(cdata[i][:cols].count('1') % 2)
            if parity_bit != cdata[i][cols]:
                error_row = i
                    
        for j in range(cols):
            col_bits = [cdata[i][j] for i in range(rows)]
            parity_bit = str(col_bits.count('1') % 2)
            if parity_bit != cdata[rows][j]:
                error_col = j
                    
        if error_row is not None and error_col is not None:
            cdata[error_row][error_col] = '1' if cdata[error_row][error_col] == '0' else '0'
        elif error_row is not None or error_col is not None:
            raise ValueError("több hiba")
                
        original_data = ''
        for i in range(rows):
            original_data += ''.join(cdata[i][:cols])
        return original_data
        
        
tp = TwoDimParCheckCode()
print(tp.encode("010101"))


# 3. Írj programot, amely egy standard alakú generátormátrixhoz elkészíti annak hibaellenőrző\-mátrix párját!  
# 
# 

# In[ ]:


def hibaellenorzo_matrix(G):
    k, n = G.nrows(), G.ncols()
    P = G[:, k:]     
    
    I_r = identity_matrix(n - k)
    H = block_matrix([[P.transpose()], [I_r]])
    
    return H


G = Matrix([[1, 0, 0, 1, 1],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1]])

H = hibaellenorzo_matrix(G)
print(G)
print(H)


# 4. Írj programot, amely egy standard alakú hibaellenőrző\-mátrixhoz elkészíti annak generátormátrix párját!  
# 
# 

# In[ ]:


def generator_matrix(H):
    n = H.ncols()
    k = n - H.nrows()  
    G = Matrix(GF(2), k, n)
    
    G[:, :k] = identity_matrix(GF(2), k)
    
    for i in range(k, n):
        G[:, i] = H.transpose().column(i - k)
    
    return G


# 5* Adj programot, amely egy generátormátrixhoz meghatározza a vele ekvivalens szisztematikus kód generátormátrixát! (opcionális, nem plusz pontra)
# 
# 

# In[ ]:





# In[ ]:




