class Paciente:
    def __init__(self,nome, prio):
        self.nome = nome
        self.prioridade = prio

class Fila:
    def __init__(self):
        self.pacientes_prioritarios = [None]*1000
        self.pacientes_naoprioritarios = [None]*1000
        self.tam1 = 0 #Inicializa o tamanho do array como índice 0 (Prioridade)
        self.tam2 = 0 #Inicializa o tamanho do array como índice 0 (Sem Prioridade)
        self.count_prioridade = 0 #Contagem de pacientes com prioridades
        self.count_semprioridade = 0 #Contagem de pacientes sem prioridades
        self.atendimentos_prioridade = 0 #Contagem de pacientes com prioridades atendidos
        self.atendimentos_semprioridade = 0 #Contagem de pacientes sem prioridade atendidos

    def add(self,nome,prioridade):
        paciente = Paciente(nome, prioridade)
        if prioridade: # Se tem prioridade, adiciona no array de pacientes prioritários
            self.pacientes_prioritarios[self.tam1] = paciente.nome
            self.tam1 += 1
        else: # Se não tem prioridade, adiciona no array de pacientes sem prioridades
            self.pacientes_naoprioritarios[self.tam2] = paciente.nome
            self.tam2 += 1

    def atender(self):
        if self.tam1 == 0 and self.tam2 == 0: #Se não tiver nenhum paciente
            resp = "Não há pacientes na fila para serem atendidos!"
            return resp

        if self.tam1 > 0 and self.tam2 > 0: #Se houver pacientes com prioridade e sem prioridade
          if self.count_prioridade == 0:
              paciente_antendido = self.pacientes_prioritarios[0]
              for i in range(self.tam1-1): #Muda a posição dos pacientes
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
              for i in range(self.tam2-1): #Muda a posição dos pacientes
                self.pacientes_naoprioritarios[i] = self.pacientes_naoprioritarios[i+1]
              self.pacientes_naoprioritarios[self.tam2-1] = None
              self.atendimentos_semprioridade += 1
              self.count_semprioridade += 1
              if self.count_semprioridade >= 2:
                  self.count_prioridade = 0
              self.tam2 -= 1
              return paciente_antendido

        if self.tam1 > 0: #Se houver somente pacientes com prioridade
            paciente_antendido = self.pacientes_prioritarios[0]
            for i in range(self.tam1-1): #Muda a posição dos pacientes
                self.pacientes_prioritarios[i] = self.pacientes_prioritarios[i+1]
            self.pacientes_prioritarios[self.tam1-1] = None
            self.atendimentos_prioridade += 1
            self.count_prioridade = 1
            self.count_semprioridade = 0
            self.tam1 -= 1
            return paciente_antendido
        #Se houver somente pacientes sem prioridade        
        paciente_antendido = self.pacientes_naoprioritarios[0]
        for i in range(self.tam2-1): #Muda a posição dos pacientes
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
        while i < self.tam1 and self.tam1 != 0: 
            aux = self.pacientes_prioritarios[i] 
            seqNomes_prioridade += f"{i + 1}- Nome: {aux};\n" 
            i += 1 
            aux = self.pacientes_prioritarios[i] 
        i = 0
        while i < self.tam2: 
            aux = self.pacientes_naoprioritarios[i] 
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

