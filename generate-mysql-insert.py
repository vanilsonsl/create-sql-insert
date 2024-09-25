```python
from datetime import datetime, timedelta

# Função para gerar o SQL insert
def gerar_sql_torneios(inicio_id, inicio_numero_buraco, inicio_numero_tranca, data_inicial, ga_ids):
    sql = ""
    formatos_horarios = ["11:00:00", "13:00:00", "15:00:00", "17:00:00", "19:00:00", "21:00:00", "23:00:00"]
    data_inicial = datetime.strptime(data_inicial, '%Y-%m-%d')
    
    for i, ga_id in enumerate(ga_ids):
        for j, horario in enumerate(formatos_horarios):
            to_id = inicio_id + i * len(formatos_horarios) + j
            to_num_buraco = inicio_numero_buraco + i * len(formatos_horarios) + j
            to_num_tranca = inicio_numero_tranca + i * len(formatos_horarios) + j
            data_torneio = data_inicial + timedelta(days=i)
            data_torneio_str = data_torneio.strftime('%Y-%m-%d')

            if ga_id == 200:  # Buraco
                to_name = f"LobbyTorneio-Buraco{to_num_buraco}"
                to_appname = f"LobbyTorneio-Buraco{to_num_buraco}"
                descricao = 'Torneio de Buraco Individual'
            else:  # Tranca
                to_name = f"LobbyTorneio-Tranca{to_num_tranca}"
                to_appname = f"LobbyTorneio-Tranca{to_num_tranca}"
                descricao = 'Torneio de Tranca Individual'
            
            sql += f"({to_id},{ga_id},'{to_name}','TO_NAME não pode conter hipen no nome como antigamente, consultar Luiz','active','','B',0,0,2,0,1,0,'{to_appname}',100,8,'Troféu Virtual','Inscrições Abertas','','{data_torneio_str} {horario}',0,0,'','{descricao}',0,0,0,1,1),\n"

    return sql

# Parâmetros iniciais
inicio_id = 54435
inicio_numero_buraco = 2676
inicio_numero_tranca = 2676
data_inicial = '2024-09-27'
ga_ids = [200, 201]  # Buraco (200), Tranca (201)

# Gerar SQL
sql_gerado = gerar_sql_torneios(inicio_id, inicio_numero_buraco, inicio_numero_tranca, data_inicial, ga_ids)
print(sql_gerado)
```
