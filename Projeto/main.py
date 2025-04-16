from etl import ler_csv, filtrar_produtos_nao_entregues, somar_valor_produtos

path_arquivo = r'C:\Users\Uso Pessoal\desktop\estudos\jornada_dados\treinamento_funcao\Projeto\vendas.csv'

arquivo = ler_csv(path_arquivo)
filtro = filtrar_produtos_nao_entregues(arquivo)
valor = somar_valor_produtos(filtro)

print(valor)