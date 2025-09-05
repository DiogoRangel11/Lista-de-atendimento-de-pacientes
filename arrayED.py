class Paciente:
    def __init__(self,nome, prio):
        self.nome = nome
        self.prioridade = prio

class Fila:
    def __init__(self):
        self.pacientes_prioritarios = [None]*1000
        self.pacientes_naoprioritarios = [None]*1000
        self.tam1 = 0 #Inicializa o tamanho do array como índice 0
        self.tam2 = 0
        self.count_prioridade = 0 #Contagem de pacientes com prioridades
        self.count_semprioridade = 0 #Contagem de pacientes sem prioridades
        self.atendimentos_prioridade = 0
        self.atendimentos_semprioridade = 0

    def add(self,nome,prioridade):
        paciente = Paciente(nome, prioridade)
        if self.tam1 == 0 or self.tam2 == 0: #Se a fila estiver vazia, adiciona o paciente no início;
            if paciente.prioridade:
                self.pacientes_prioritarios[0] = paciente.nome
            else:
                self.pacientes_naoprioritarios[0] = paciente.nome
            self.tam1 += 1
            self.tam2 += 1
        else:
            if self.tam1 > 0 or self.tam2 > 0:
                if paciente.prioridade:
                    self.pacientes_prioritarios[self.tam1] = paciente.nome
                    self.tam1 +=1
                else:
                    self.pacientes_naoprioritarios[self.tam2] = paciente.nome
                    self.tam2 +=1

    def atender(self):
        if self.tam1 == 0 and self.tam2 == 0:
            resp = "Não há pacientes na fila para serem atendidos!"
            return resp

        if self.tam1 > 0 and self.tam2 > 0:
          if self.count_prioridade == 0:
              paciente_antendido = self.pacientes_prioritarios[0]
              for i in range(self.tam1):
                self.pacientes_prioritarios[i] = self.pacientes_prioritarios[i+1]
              self.pacientes_prioritarios[self.tam1-1] = None
              self.atendimentos_prioridade += 1
              self.count_prioridade += 1
              self.count_semprioridade = 0
              self.tam1 -= 1
              return paciente_antendido
          else:
            if self.count_prioridade == 1 and self.count_semprioridade < 2:
              paciente_antendido = self.pacientes_naoprioritarios[0]
              for i in range(self.tam2):
                self.pacientes_naoprioritarios[i] = self.pacientes_naoprioritarios[i+1]
              self.pacientes_naoprioritarios[self.tam2-1] = None
              self.atendimentos_semprioridade += 1
              self.count_semprioridade += 1
              if self.count_semprioridade >= 2:
                  self.count_prioridade = 0
              self.tam2 -= 1
              return paciente_antendido

        if self.tam1 > 0:
            paciente_antendido = self.pacientes_prioritarios[0]
            for i in range(self.tam1):
                self.pacientes_prioritarios[i] = self.pacientes_prioritarios[i+1]
            self.pacientes_prioritarios[self.tam1-1] = None
            self.atendimentos_prioridade += 1
            self.count_prioridade = 1
            self.count_semprioridade = 0
            self.tam1 -= 1
            return paciente_antendido
        
        paciente_antendido = self.pacientes_naoprioritarios[0]
        for i in range(self.tam2):
            self.pacientes_naoprioritarios[i] = self.pacientes_naoprioritarios[i+1]
        self.pacientes_naoprioritarios[self.tam2-1] = None
        self.atendimentos_semprioridade += 1
        self.count_semprioridade += 1
        self.tam2 -= 1
        return paciente_antendido

    def listar(self):
        seqNomes_prioridade = "" 
        seqNomes_semprioridade = "" 
        i = 0 
        aux = self.pacientes_prioritarios[i] 
        while i < self.tam1: 
            seqNomes_prioridade += f"{i + 1}- Nome: {aux};\n" 
            i += 1 
            aux = self.pacientes_prioritarios[i] 
        i = 0
        aux = self.pacientes_naoprioritarios[i] 
        while i < self.tam2: 
            seqNomes_semprioridade += f"{i + 1}- Nome: {aux};\n" 
            i += 1 
            aux = self.pacientes_naoprioritarios[i] 
        return f"Lista de pacientes prioritários:\n{seqNomes_prioridade}\nLista de pacientes sem prioridade:\n{seqNomes_semprioridade}"
    
    def total(self):
        total = self.atendimentos_prioridade + self.atendimentos_semprioridade
        if total == 0:
            return "Não foi realizado nenhum atendimento"
        else:
            por_prioridade = (100 * self.atendimentos_prioridade) / total
            por_semprioridade = (100 * self.atendimentos_semprioridade) / total
            return f"Total de atendimento: {total}\nPercentuais de atendimento:\nPacientes com prioridade: {por_prioridade:.1f}%\nPacientes sem prioridade: {por_semprioridade:.1f}%"

