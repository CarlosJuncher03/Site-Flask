from conex_sql_sever import consulta_sqlserver

def quant_ticket_abertos(codigocliente):
    # Executar a consulta SQL para obter a quantidade de tickets abertos
    resultado = consulta_sqlserver(f"SELECT COUNT(*) FROM FP_Atendimento INNER JOIN Cliente ON Cliente.CodCliente = FP_Atendimento.CodCliente WHERE FP_Atendimento.Status != 'Concluido' AND FP_Atendimento.CodCliente = {codigocliente}")
    # Retornar o resultado da consulta
    return resultado[0][0] if resultado else 0


def quant_total(codigocliente):
    resultado = consulta_sqlserver(f"SELECT COUNT(*) FROM FP_Atendimento INNER JOIN Cliente ON Cliente.CodCliente = FP_Atendimento.CodCliente WHERE FP_Atendimento.CodCliente = {codigocliente}")
    # Retornar o resultado da consulta
    return resultado[0][0] if resultado else 0


def lista_atendimentos_cliente(codigocliente):
    consulta = f"SELECT FP_Atendimento.CodAtendimento,FP_Atendimento.Data, Vendedor.Nome, FP_Atendimento.NomeSolicitante, FP_Atendimento.Status,  FP_solicitacao.descricao, FP_Atendimento.Prioridade, FP_Atendimento.DataConclusao FROM FP_Atendimento INNER JOIN Vendedor ON FP_Atendimento.CodRespAt = Vendedor.CodVendedor LEFT JOIN FP_solicitacao ON FP_solicitacao.codigo = FP_Atendimento.FP_solicitacao WHERE FP_Atendimento.CodCliente = {codigocliente} order by FP_Atendimento.CodAtendimento desc"
    return consulta_sqlserver(consulta)
    

def nome_cliente(codigo_cliente):
    resultado = consulta_sqlserver(f"SELECT Cliente.nome FROM Cliente WHERE Cliente.CodCliente = {codigo_cliente}")
    return resultado[0][0] if resultado else None

def endereco_cliente(codigo_cliente):
    resultado = consulta_sqlserver(f"SELECT Cliente.Endereco FROM Cliente WHERE Cliente.CodCliente = {codigo_cliente}")
    return resultado[0][0] if resultado else None

def bairro_cliente(codigo_cliente):
    resultado = consulta_sqlserver(f"SELECT Cliente.Bairro FROM Cliente WHERE Cliente.CodCliente = {codigo_cliente}")
    return resultado[0][0] if resultado else None

def numero_cliente(codigo_cliente):
    resultado = consulta_sqlserver(f"SELECT Cliente.Numero FROM Cliente WHERE Cliente.CodCliente = {codigo_cliente}")
    return resultado[0][0] if resultado else None

def email_cliente(codigo_cliente):
    resultado = consulta_sqlserver(f"SELECT Cliente.EMail FROM Cliente WHERE Cliente.CodCliente = {codigo_cliente}")
    return resultado[0][0] if resultado else None