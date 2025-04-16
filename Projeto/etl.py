# Biblioteca
import csv


# Função para tratar arquivos
def ler_csv(nome_arquivo:str) -> list[dict]:
    """
    Função que le um arquivo csv e retorna uma lista de dicionarios
    """
    lista = []
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista


def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:
    """
    Função que filtra produtos onde entrega = False
    """
    produtos_filtrados = []
    for produto in lista:
        if produto.get('entregue') == "False":
            produtos_filtrados.append(produto)
    return produtos_filtrados


def somar_valor_produtos(lista_produtos : list[dict]) -> int:
    """
    Função que soma os valores dos produtos entregues
    """
    valor_total = 0
    for produto in lista_produtos:
        valor_total += int(produto.get('price'))
    return valor_total