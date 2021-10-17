import requests
from datetime import datetime

def main(dict):
    if dict.get('type') == 'DIARIO':
        dia_semana = {
            0: 'Segunda',
            1: 'Terca',
            2: 'Quarta',
            3: 'Quinta',
            4: 'Sexta',
            5: 'Sabado',
            6: 'Domingo'
        }
        data = datetime.strptime(dict.get('data'),'%Y-%m-%d')
        if data > datetime.now():
            return { 'cotacao': 0, 'dia_semana': "Dia Invalido" }
        else:
            url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data.strftime('%m-%d-%Y')}'&$top=100&$format=json&$select=cotacaoCompra"
            response = requests.get(url)
            if response.ok:
                cotacao = response.json().get('value')
                if len(cotacao)>0:
                    cotacao = cotacao[0].get('cotacaoCompra')
                else:
                    cotacao = 0
            else:
                cotacao = 0
            return { 'cotacao': cotacao, 'dia_semana': dia_semana.get(data.weekday()) }
    elif dict.get('type') == 'PERIODO':
        response = ''
        data_1 = datetime.strptime(dict.get('data_1'),'%Y-%m-%d')
        data_2 = datetime.strptime(dict.get('data_2'),'%Y-%m-%d')
        if data_1< datetime(1994,7,1):
            data_1 = datetime(1994,7,1)
        url = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='{begin}'&@dataFinalCotacao='{end}'&$format=json&$select=cotacaoCompra,dataHoraCotacao"
        url = url.format(begin = data_1.strftime('%m-%d-%Y'),end = data_2.strftime('%m-%d-%Y'))
        data = requests.get(url).json().get('value')
        if len(data) == 0:
            response = "Datas Invalidas ou sem valor de Dólar no periodo"
        else:
            dolar_comeco = data[0]['cotacaoCompra']
            dolar_fim = data[-1]['cotacaoCompra']
            dolar_var = (dolar_fim/dolar_comeco)-1
            response = """Variação do Dólar = {:,.3f}%
    Começo ({data_1}) = R${dolar_1}
    Fim ({data_2}) = R${dolar_2}""".format(
                dolar_var*100,
                data_1 = data_1.strftime("%d/%m/%Y"),
                dolar_1 = dolar_comeco,
                data_2 = data_2.strftime("%d/%m/%Y"),
                dolar_2 = dolar_fim
                )
        return { 'resultado': response }
