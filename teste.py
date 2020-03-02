import bowling_kata
nome=input("Digite o nome do jogador:")
while nome != 'sair':
    jogador1 = bowling_kata.CalculadoraPontuacaoBoliche(nome)
    jogador1.jogar(0)
    nome=input("Digite o nome do jogador ou sair para finalizar:")
