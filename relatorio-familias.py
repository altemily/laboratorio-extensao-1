## Código para criar um relatório de acompanhamento da família enlutada ##

class FamiliaEnlutada:
    def __init__(self, nome, data_falecimento, contato, apoio_recebido, observacoes):
        self.nome = nome
        self.data_falecimento = data_falecimento
        self.contato = contato
        self.apoio_recebido = apoio_recebido
        self.observacoes = observacoes
        self.apoio_encerrado = False  ## Novo atributo para indicar se o apoio foi encerrado ##

    def encerrar_apoio(self):
        """Marca o apoio como encerrado por solicitação da família."""
        self.apoio_encerrado = True

def gerar_relatorio(familias):
    with open("relatorio_familias_enlutadas.txt", "w") as arquivo:
        arquivo.write("Relatório de Acompanhamento - Famílias Enlutadas\n")
        arquivo.write("="*50 + "\n\n")
        
        for familia in familias:
            arquivo.write(f"Nome: {familia.nome}\n")
            arquivo.write(f"Data do Falecimento: {familia.data_falecimento}\n")
            arquivo.write(f"Contato: {familia.contato}\n")
            arquivo.write(f"Apoio Recebido: {familia.apoio_recebido}\n")
            arquivo.write(f"Observações: {familia.observacoes}\n")
            ## Verifica se o apoio foi encerrado e inclui no relatório ##
            if familia.apoio_encerrado:
                arquivo.write("Status: Apoio encerrado por solicitação da família\n")
            else:
                arquivo.write("Status: Apoio ativo\n")
            arquivo.write("-"*50 + "\n")


## Exemplo de uso ##

familias_enlutadas = [
    FamiliaEnlutada("Maria Pereira", "12-07-2019", "1234-5678", "Apoio psicológico", "Acompanhamento semanal"),
    FamiliaEnlutada("José Souza da Silva", "08-05-2023", "1011-1213", "Grupo de apoio", "Necessita de mais suporte emocional"),
]

## Encerrar o apoio da família "José Souza da Silva" ##

familias_enlutadas[1].encerrar_apoio()

## Gerar o relatório ##

gerar_relatorio(familias_enlutadas)
print("Relatório gerado com sucesso!")
