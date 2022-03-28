class No:
    def __init__(self, anterior, info, prox):
        self.prox = prox
        self.anterior = anterior
        self.info = info 
        
    class LDSE:
        def __init__(self):
            self.prim= self.ult= None
            self.quant = 0
            
        def inserirPosicao(self, valor, posicao):
            if self.quant == 0:
                self.prim = self.ult = No(valor, None)
            else: 
                aux = ant = self.prim
                while aux.prox != None and aux.info != posicao:
                    ant = aux
                    aux = aux.prox
                if aux.info == posicao:
                    ant.prox = posicao
                    if aux == self.prim:
                        self.prim = posicao
                    if aux == self.ult:
                        self.ult = aux.prox
                    self.quant += 1
         
            
        def somarElementos(self):
            somados = 0
            if self.quant == 0:
                somados;
            pass
            
             
        #def removePosicao(self, posicao):
            
            
        #def removerTodas(self, valor):
            
        
        #def inserirApos(self, valor1, valor2):
            
    
        
                
            
        