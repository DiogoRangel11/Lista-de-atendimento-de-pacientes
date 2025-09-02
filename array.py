class Paciente:
    def __init__(self,nome, prio):
        self.nome = nome
        self.prioridade = prio

class Fila:
    def __init__(self):
        self.pacientes = [None]*100
        self.tamanho = 0 #Inicializa o tamanho do array como índice 0
        self.paciente_anterior = None
        self.count_prioridade = 0 #Contagem de pacientes com prioridades
        self.count_semprioridade = 0 #Contagem de pacientes sem prioridades

    def add(self,nome,prioridade):
        paciente = Paciente(nome, prioridade)
        if self.pacientes is None: #Se a fila estiver vazia, adiciona o paciente no início;
            self.pacientes[0] = paciente
            self.paciente_anterior = self.pacientes[0]
            if paciente.prioridade == True:
                self.count_prioridade += 1
            else:
                self.count_semprioridade += 1
            self.tamanho += 1

        sem_prioridade_consecutivos = 0
        i = self.tamanho - 1
        while i >= 0: #Verificação do array do final ao início para ver quantos pacientes sem prioridade consecutivos
            if self.pacientes[i].prioridade == False:
                sem_prioridade_consecutivos += 1
            else:
                break
            i -= 1

        if paciente.prioridade == True:
            if sem_prioridade_consecutivos >= 2:
                self.pacientes[self.tamanho] = paciente
                self.tamanho += 1
                self.count_prioridade += 1
                self.count_semprioridade = 0
            else:
                self.pacientes[self.tamanho] = paciente
                self.tamanho += 1
                self.count_prioridade += 1
                self.count_semprioridade = 0
        else: #Se o paciente não tiver prioridade
            self.pacientes[self.tamanho] = paciente
            self.tamanho += 1
            self.count_semprioridade += 1
            if self.count_semprioridade == 2:
                self.count_semprioridade = 0
                self.count_prioridade = 0

    def atender(self):
        if self.tamanho == 0:
            resp = "Não há pacientes na fila para serem atendidos!"
            return resp
        else:
            paciente_antendido = self.pacientes[0]
            if paciente_antendido.prioridade:
                self.count_prioridade -= 1
            else:
                self.count_semprioridade -= 1
            for valor in range(0,self.tamanho-1):
                self.pacientes[valor] = self.pacientes[valor+1]
            self.pacientes[self.tamanho-1] = None

            self.tamanho -= 1
            
    def listar(self):
        seqNomes = ""
        i = 0
        aux = self.pacientes[i]
        while aux != None:
            seqNomes += aux.nome + ": " + aux.prioridade + " - "
            i += 1
            aux = self.pacientes[i]
