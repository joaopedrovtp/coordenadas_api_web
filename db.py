import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from dynaconf import settings
import os


def save_to_db():
    
    # Cria um dataframe com a tabela final
    consultas = pd.read_excel(os.path.join(settings.UPLOAD_FOLDER, "Resultado_final.xlsx"),
        sheet_name="Coordenadas",
        header=0,
        index_col=False,
        keep_default_na=True
    )

    # Cria conexão com o banco de dados
    engine = create_engine(settings.DATABASE_URL, echo=True)

    # Sobe a tabela de resultado no db 
    consultas.to_sql('consultas', con = engine, if_exists = 'append', chunksize = 1000, index = False, index_label = 'ID')

    return print("Dados armazenados com sucesso")