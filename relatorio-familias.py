## Código para criar um relatório de acompanhamento da família enlutada ##


class FamiliaEnlutada:
    def __init__(self, nome, data_falecimento, contato, apoio_recebido, observacoes):
        self.nome = nome
        self.data_falecimento = data_falecimento
        self.contato = contato
        self.apoio_recebido = apoio_recebido
        self.observacoes = observacoes
        self.apoio_encerrado = False  ## Indica se o apoio foi encerrado ##
        self.feedback = None  ## Inicialmente, não há feedback ##

    def encerrar_apoio(self):
        """Marca o apoio como encerrado."""
        self.apoio_encerrado = True

    def registrar_feedback(self, feedback):
        """Registra o feedback da família sobre o apoio recebido."""
        self.feedback = feedback

def gerar_relatorio(familias):
    """Gera um relatório de acompanhamento das famílias enlutadas."""
    with open("relatorio_familias_enlutadas.txt", "w") as arquivo:
        arquivo.write("Relatório de Acompanhamento - Famílias Enlutadas\n")
        arquivo.write("="*50 + "\n\n")
        
        for familia in familias:
            arquivo.write(f"Nome: {familia.nome}\n")
            arquivo.write(f"Data do Falecimento: {familia.data_falecimento}\n")
            arquivo.write(f"Contato: {familia.contato}\n")
            arquivo.write(f"Apoio Recebido: {familia.apoio_recebido}\n")
            arquivo.write(f"Observações: {familia.observacoes}\n")
            ## Verifica se o apoio foi encerrado ##
            if familia.apoio_encerrado:
                arquivo.write("Status: Apoio encerrado por solicitação da família\n")
            else:
                arquivo.write("Status: Apoio ativo\n")
            
            ## Verifica se há feedback ##
            if familia.feedback:
                arquivo.write(f"Feedback: {familia.feedback}\n")
            else:
                arquivo.write("Feedback: Nenhum feedback fornecido\n")
            
            arquivo.write("-"*50 + "\n")

def main():
    ## Lista de famílias enlutadas ##
    familias_enlutadas = [
        FamiliaEnlutada("Maria Pereira", "12-07-2019", "1234-5678", "Apoio psicológico", "Acompanhamento semanal"),
        FamiliaEnlutada("José Souza da Silva", "08-05-2023", "1011-1213", "Grupo de apoio", "Necessita de mais suporte emocional"),
    ]

    ## Encerrar o apoio da família "José Souza da Silva" ##
    familias_enlutadas[1].encerrar_apoio()

    ## Registrar feedback da família "Maria Pereira" ##
    familias_enlutadas[0].registrar_feedback("O apoio foi muito útil e reconfortante.")

    ## Gerar o relatório das famílias ##
    gerar_relatorio(familias_enlutadas)
    print("Relatório gerado com sucesso!")

main()
