from buscaInsercao import No;


class ListaDSE:
    def __init__(self):
        self.prim = None
        self.quant = 0
        
    #percorre a lista e retorna o índice do no     
    def _getNo(self, posicao): # '_' deixa a def escondida, não é necesário ficar visível para o usuário 
        aux = self.prim
        for i  in range(posicao):
            if aux:
                aux = aux.next
            else:
                raise IndexError("List index out of range")  
        return aux
    
    #representacao que sera usada para exibir os dados
    def __repr__(self) :
        r = ""
        aux = self.prim
        while (aux):
            r = r + str(aux.dado) + "->"
            aux = aux.next
        return r
    
    # métodos para poder representar em String no print
    def __str__(self):
        return self.__repr__()
       
    def inserirPosicao(self, posicao, dado):
        no = No(dado)
        #caso queira inserir no início do No
        if posicao == 0:
            no.next = self.prim
            self.prim = no
        else:
            #subtraímos 1 para chegar no elemento anterior que contém o endereço do prox que é oque queremos
            aux = self._getNo(posicao - 1)  #chamando a função que retorna o No procurado
            no.next = aux.next     #capturando endereço do restante da lista
            aux.next = no
        self.quant = self.quant + 1 #acrescentando 1 unidade no tamanho da lista
            
                
    def removePosicao(self, posicao):
        #caso a lista estiver vazia
        if self.prim == None:
            raise ValueError("{} is not in list".format(posicao))
        #caso queira remover o início
        elif self.prim.dado == posicao:
            self.prim = self.prim.next 
            self.quant = self.quant - 1 #Decrementando 1 unidade do tamanho da lista
            return True #feedback, operacao executada 
        else:  
            antAux= self.prim  
            aux = self.prim.next
            while(aux):
                if aux.dado == posicao:
                    antAux.next = aux.next # ligando o anterior doque vai ser removido ao seu posterior 
                    aux.next = None  #posicao retirada da lista 
                antAux = aux
                aux = aux.next   
                self.quant = self.quant - 1 #Decrementando 1 unidade do tamanho 
            return True #feedback, operacao executada 
        raise ValueError("{} is not in list".format(posicao))  
         
        ###FALTA IMPLEMENTAR
    def removerTodas(self, valor):
        #caso a lista estiver vazia
        if self.prim == None:
            raise ValueError("{} is not in list".format(valor))
        elif self.prim.dado == posicao:
            self.prim = self.prim.next 
            self.quant = self.quant - 1 #Decrementando 1 unidade do tamanho da lista
            return True #feedback, operacao executada  
        else:
            antAux= self.prim  
            aux = self.prim.next
        
    
    def inserirApos(self, valor1, valor2):
        no = No(valor1)
        #caso queira inserir no início do No
        if valor1 == 0:
            no.next = self.prim
            self.prim = valor2
        else:
            #retorna exatamente o no que apontara para o valor 2, já que será inserido após 
            aux = self._getNo(valor1)  #chamando a função que retorna o No procurado
            no.next = aux.next     #capturando endereço do restante da lista
            aux.next = valor2
        self.quant = self.quant + 1 #acrescentando 1 unidade no tamanho da lista
    
    
    def somarElementos(self):
        auxSoma = 0         #variável aux que guarda os valores dos nós
        aux = self.prim
        while aux and aux.dado != None: #percorre até que o ultimo nó aponte pra o vazio 
            aux = aux.prox
            auxSoma = auxSoma + aux.dado
        return auxSoma