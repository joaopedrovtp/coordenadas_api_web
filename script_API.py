'''
Script criado para busca de coordenadas geográficas utilizando a Geocoding API do Matchbox
Planilha excel utilizada como fonte de dados - verificar arquivo 'Layout - Pesquisa coordenadas.xlsx'

'''

import os  # lida com o sistema operacional da máquina
from openpyxl import load_workbook, workbook  # biblioteca que lida com o excel
from mapbox import Geocoder
from dynaconf import settings


def mapbox_API(file):
    # importando o arquivo excel a ser utilizado
    book = load_workbook(file)  # abre o arquivo excel que será utilizado para cadastro
    sheet = book["Coordenadas"]  # seleciona a sheet chamada "Coordenadas"
    i = 2  # aqui indica começará da segunda linha do excel, ou seja, pulará o cabeçalho
    for r in sheet.rows:

        endereco = sheet[i][1] # [linha][coluna]
        bairro = sheet[i][2]
        munic_UF = sheet[i][3]

        # Verifica se o campo 'Endereço' da primeira linha está preenchido 
        if str(type(endereco.value)) == "<class 'NoneType'>":
            break

        # Concatena endereço completo com ou sem bairro preenchido 
        if str(type(bairro.value)) == "<class 'NoneType'>":
            endereco_completo = endereco.value + " " + munic_UF.value
        else:
            endereco_completo = endereco.value + " " + bairro.value + " " + munic_UF.value

        # Iniciando Mapbox Geocoding API
        geocoder = Geocoder() 
        geocoder = Geocoder(access_token=settings.MAPBOX_TOKEN) # Token auth

        ## Buscando localização pela API pelo endereço completo
        # Busca pelo endereço completo no país Brasil
        response = geocoder.forward(endereco_completo, country=['br'], limit = 3)
        
        # Caso não localize o endereço, será informado na célula do excel
        if response.status_code == 401:
            sheet[i][6].value= "Nao foi possivel identificar"
            sheet[i][7].value= "NA"
            sheet[i][8].value= "NA"
            continue

        # Loop para coletar os 3 endereços/coordenadas   
        k = 6
        for j in range(3): 
            # Coletar o endereço completo
            address = response.geojson()['features'][j]['place_name']
            sheet[i][k].value = address

            # Coletar a latitude e logitude     
            latlong  = response.geojson()['features'][j]['center']
            latitude = latlong[1]
            longitude = latlong[0]

            # Preenchendo lat/long em cada célula 
            sheet[i][k+1].value = latitude
            sheet[i][k+2].value = longitude

            k += 3

        i += 1

    file = book

    return file



