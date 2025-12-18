from datetime import datetime, timedelta

# Função para gerar o SQL insert para vários dias
def gerar_sql_torneios(inicio_id, inicio_numero_buraco, inicio_numero_tranca, data_inicial, ga_ids, dias):
    sql = f"-- Data inicial: {data_inicial}\n"  # Adiciona a data inicial como um comentário
    formatos_horarios = ["11:00:00", "13:00:00", "15:00:00", "17:00:00", "19:00:00", "21:00:00", "23:00:00"]
    data_inicial = datetime.strptime(data_inicial, '%Y-%m-%d')

    for dia in range(dias):  # Loop para cada dia
        data_torneio = data_inicial + timedelta(days=dia)
        data_torneio_str = data_torneio.strftime('%Y-%m-%d')

        for i, ga_id in enumerate(ga_ids):
            for j, horario in enumerate(formatos_horarios):
                to_id = inicio_id + dia * len(ga_ids) * len(formatos_horarios) + i * len(formatos_horarios) + j

                if ga_id == 200:  # Buraco
                    to_num = inicio_numero_buraco + dia * len(formatos_horarios) + j
                    to_name = f"LobbyTorneio-Buraco{to_num}"
                    to_appname = f"LobbyTorneio-Buraco{to_num}"
                    descricao = 'Torneio de Buraco Individual'
                    game_type = 'B'
                else:  # Tranca
                    to_num = inicio_numero_tranca + dia * len(formatos_horarios) + j
                    to_name = f"LobbyTorneio-Tranca{to_num}"
                    to_appname = f"LobbyTorneio-Tranca{to_num}"
                    descricao = 'Torneio de Tranca Individual'
                    game_type = 'T'

                sql += f"({to_id},{ga_id},'{to_name}','TO_NAME não pode conter hipen no nome como antigamente, consultar Luiz','active','','{game_type}',0,0,2,0,1,0,'{to_appname}',100,8,'Troféu Virtual','Inscrições Abertas','','{data_torneio_str} {horario}',0,0,'','{descricao}',0,0,0,1,1),\n"
    
    # Substituir a última vírgula por ponto e vírgula
    if sql.endswith(",\n"):
        sql = sql.rstrip(",\n") + ";\n"
    
    return sql

# Função para salvar o SQL em um arquivo
def salvar_sql_em_arquivo(sql, data_inicial, dias):
    nome_arquivo = f"torneios_{data_inicial}_dias_{dias}.sql"  # Nome do arquivo inclui a data e o número de dias
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(sql)

# Parâmetros iniciais
inicio_id = 60749
inicio_numero_buraco = 5833
inicio_numero_tranca = 5833
data_inicial = '2025-12-20'
ga_ids = [200, 201]  # Buraco (200), Tranca (201)
dias = 90  # Gerar torneios por 90 dias

# Gerar SQL
sql_gerado = gerar_sql_torneios(inicio_id, inicio_numero_buraco, inicio_numero_tranca, data_inicial, ga_ids, dias)

# Salvar o SQL gerado em um arquivo
salvar_sql_em_arquivo(sql_gerado, data_inicial, dias)
