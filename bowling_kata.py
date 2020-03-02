class CalculadoraPontuacaoBoliche():

    def __init__(self,nome):
        self.nome=nome
        self.pontuacao=list()

    def jogar(self,jogada):
        
        contRodada=1
        spareVerifica= False
        contaSpare=0
        bonus=0
        anterior=0
        for i in range(10):

            
            chances=2
            contChances=0
            somaJogada=0
            pinos=10
            
            while contChances < chances:
                
                jogada=int(input("Digite o numero de pinos derrubados:"))
                if spareVerifica == True:
                    bonus= bonus+jogada
                    print(bonus)
                    spareVerifica= False

                
                
                if jogada >=0 and jogada <=10:
                    
                    pinos= pinos - jogada
                    print('Restam:',pinos,'pinos')
                    if pinos < 0 or pinos > 10:
                        print("Excedeu a quantidade de pinos,tente novamente")
                        pinos= 10 - antValido
                    
                
                    else:
                        antValido=jogada
                        somaJogada= jogada + anterior
                        if somaJogada == 10 and jogada !=10 and contChances == 1:
                            print("Spare!!")
                            contaSpare+=1
                            spareVerifica= True  
                        
                        if jogada < 10:
                            contChances+=1
                            self.pontuacao.append(jogada)
                            anterior=jogada
                            
                        else:
                            if contRodada <= 9:
                                print('Strike!')
                                contChances=2
                                self.pontuacao.append(jogada)
                                
                            else:
                                print('Strike!')
                                contChances=2
                                self.pontuacao.append(jogada)
                                for i in range(2):
                                    bonusj= int(input("Jogada bonus!!! Digite o numero de pinos derrubados:"))
                                    jogada=bonusj
                                    self.pontuacao.append(jogada)
                else:
                    print("Jogada inválida! Tente novamente")

                

                
            contRodada+=1
            print('Spares:',contaSpare)
                    
            
        print('Bônus do Spare:',bonus)
        pontos=self.pontuacao
        print('Lista de pinos derrubados:',pontos)
        strikeBonus=0
        resultado=0
        for i in pontos:
            resultado= resultado+i

        for i in range(len(pontos)-2):
            if pontos[i] == 10:
                strikeBonus= strikeBonus + pontos[i+1]+pontos[i+2]
                
                
        print('Soma bônus do strike:',strikeBonus)
        
        
        #resultado=bonus+strikeBonus
        print(self.nome,'fez:',resultado+bonus+strikeBonus,' pontos')
        



        

                
