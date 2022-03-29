from circular import NoC

class ListaDSEC:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    
    
    def trocar(self, posicao, novovalor):
        aux = self.prim = self.ult
        if self.quant == 1: #caso exista apenass 1 elemento na lista
            self.prim = self.ult = NoC(novovalor, None)
            self.prim.prox = self.prim
        
        else:
            while self.ult.prox != posicao: # Percorre até chegar na posição anterior a desejada
                aux.next 
                
    
    
    def consultarAnterior(self, valor): 
        while self.ult.prox != self.prim:
            if self.info == valor:
                return self.ult
        return valor #caso self.ult.prox == self.prim, quer dizer que a lista é unitária, seu anterior, no caso de ListaDSEC, é ele mesmo
    
    def contarPares(self):
        par = 0;
        aux = self.ult
        while self.ult.prox != self.prim:
            aux.next     #falta implementar a atualiza;áo dos ponteiros
            if self.info % 2 == 0:
                par += 1;
        return ('Os pares aparecem {} na lista'.format(par));