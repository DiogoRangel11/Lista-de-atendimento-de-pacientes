from arrayED import Fila

if __name__ == "__main__":
    fila_pacientes = Fila()
    menu = "------ MENU PACIENTES -------\n1- Cadastrar Paciente\n2- Antender Paciente\n3- Listar Pacientes\n4- SAIR"
    while True:
        print(menu)
        try:
            n = int(input("Escolha uma opção acima: "))
        except ValueError:
            print("Digite apenas números inteiros!")
            continue
        #ESCOLHAS DO MENU:
        if n == 1:
            print("---- CADASTRO DO PACIENTE ----")
            nome = input("Infome o nome do paciente: ")
            p = int(input("O paciente é prioridade? [1 -Sim/ 2- Não] "))
            if p == 1:
                prioridade = True
            else:
                prioridade = False
            fila_pacientes.add(nome, prioridade)
            print("Paciente adicionado com sucesso!")
        elif n == 2:
            print("---- ATENDIMENTO AO PACIENTE ----")
            print(f"Paciente atendido: {fila_pacientes.atender()}") #Atende na ordem que foi adicionado com as regras estabelecidas
        elif n == 3:
            print("---- LISTA DE PACIENTES ----")
            print(fila_pacientes.listar())
        elif n == 4:
            if fila_pacientes.tam1 == 0 and fila_pacientes.tam2 == 0:
                break
            else:
                print("Existem pacientes para serem atendidos.")
        else:
            print("Opção inválida!")
    
    print(fila_pacientes.total())
