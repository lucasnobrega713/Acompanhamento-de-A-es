import streamlit as st
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import pandas as pd
import requests
import plotly.express as px


def pagina_inicio():
    st.title('Acompanhamento da Bolsa de Valores D-1')
    st.subheader('Informações Gerais')
    st.write('')
    st.write('')
    st.write('Olá, seja muito bem vindo(a) ao dash para acompanhamento da bolsa de valores.')
    st.write('Esse painel foi construido unicamente como forma de estudo, sem fins lucrativos. Espero que aqui consiga encontrar informações relevantes para você e qualquer dica que tenha, pode estar entrando em contato comigo utilizando as informações abaixo.')
    st.write('')
    st.write('')
    st.subheader('Projeto desenvolvido por Lucas de Sousa Nobrega')
    st.write('')
    st.write('')
    st.subheader("Informações de Contato")

    # Informações de contato em Markdown
    informacoes_contato = """
    **Endereço:** Rua Projetada 2, Número 57 - 
    **Cidade:** Massaranduba - 
    **CEP:** 58120-000

    **Telefone:** (83) 9 9365-2937
    **Email:** lucas.nobrega_sousa@outlook.com
    """

    # Exibir as informações de contato usando o widget Markdown
    st.markdown(informacoes_contato)
    
    st.title('')
    st.title('')
    st.subheader('Código da Página:')

    st.code('''def pagina_inicio():
    st.title('Acompanhamento da Bolsa de Valores D-1')
    st.subheader('Informações Gerais')
    st.write('')
    st.write('')
    st.write('Olá, seja muito bem vindo(a) ao dash para acompanhamento da bolsa de valores.')
    st.write('Esse painel foi construido unicamente como forma de estudo, sem fins lucrativos. Espero que aqui consiga encontrar informações relevantes para você e qualquer dica que tenha, pode estar entrando em contato comigo utilizando as informações abaixo.')
    st.write('')
    st.write('')
    st.subheader("Informações de Contato")

    # Informações de contato em Markdown
    informacoes_contato = """
    **Endereço:** Rua Projetada 2, Número 57 - 
    **Cidade:** Massaranduba - 
    **CEP:** 58120-000

    **Telefone:** (83) 9 9365-2937
    **Email:** lucas.nobrega_sousa@outlook.com
    """

    # Exibir as informações de contato usando o widget Markdown
    st.markdown(informacoes_contato)''')

    st.markdown('<hr style="margin-top: 50px;">', unsafe_allow_html=True)
    st.write("© 2023 Lucas de Sousa Nobrega.")

def pagina_intraday():
    #API Request

    ALPHA_VANTAGE_API_KEY = 'TCHQ4YXXQ2B07DR4'
    ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')

    #Ações
    simbolos = [
        'MSFT', 'AAPL', 'BA', 'GOOGL', 'AMZN', 'TSLA', 'NVDA', 'JPM', 'V', 'MA',
        'WMT', 'PG', 'UNH', 'HD', 'DIS', 'CRM', 'ADBE', 'VZ', 'KO', 'INTC',
        'NFLX', 'CMCSA', 'PFE', 'ABT', 'T', 'NKE', 'MRK', 'PEP', 'ABBV', 'CVX'
    ]


    #Sidebar
    st.sidebar.title('Filtros')
    qutd_info = st.sidebar.number_input('Nº de Informações na tabela:', min_value=1, max_value=50, value=10)
    symbol = st.sidebar.selectbox('Escolha o simbolo da ação:', simbolos)


    #Dashboard
    st.title('Intraday')
    st.write('Este painel apresenta dados Intraday da Bolsa de Valores usando a Alpha Vantage.')

    if symbol:
        interval = '15min'
        data, meta_data = ts.get_intraday(symbol=symbol, interval=interval, outputsize='full')
        data['Variacao'] = data['4. close'].diff()
        data['Variacao_Porcentagem'] = (data['Variacao'] / data['4. close'].shift(1)) * 100

        st.subheader('Dados de Preços de Fechamento')
        st.write(data.head(qutd_info))

        st.subheader('Gráfico de Preços de Fechamento')
        fig_preco = px.line(data, x=data.index, y='4. close', labels={'x': 'Data', 'y': 'Preço de Fechamento'})
        fig_preco.update_layout(title=f'Preços de Fechamento para {symbol}')

        st.plotly_chart(fig_preco)

        st.subheader('Variação de Preço em Porcentagem')
        fig_variacao = px.line(data, x=data.index, y='Variacao_Porcentagem', labels={'x': 'Data', 'y': 'Variação de Preço (%)'})
        fig_variacao.update_layout(title=f'Variação de Preço em Porcentagem para {symbol}')

        st.plotly_chart(fig_variacao)

        st.subheader('Volume de Negociações')
        fig_volume = px.bar(data, x=data.index, y='5. volume', labels={'x': 'Data', 'y': 'Volume de Negociações'})
        fig_volume.update_layout(title=f'Volume de Negociações para {symbol}')

        st.plotly_chart(fig_volume)

        #'''

        #Sidebar
        st.sidebar.subheader('Informações da Ação')
        st.sidebar.write(f"Nome da Empresa: {meta_data['2. Symbol']}")
        st.sidebar.write(f"Última Data Disponível: {meta_data['3. Last Refreshed']}")

        start_date = st.sidebar.date_input("Data de Início", data.index.min())
        end_date = st.sidebar.date_input("Data Final", data.index.max())

        filtered_data = data.loc[start_date:end_date]

        st.set_option('deprecation.showPyplotGlobalUse', False)  # Para suprimir um aviso de depreciação
        #'''

        st.title('')
        st.title('')
        st.subheader('Código da Página:')

        st.code('''def pagina_intraday():
                
    #API Request
    ALPHA_VANTAGE_API_KEY = 'TCHQ4YXXQ2B07DR4'
    ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')

    #Ações
    simbolos = [
        'MSFT', 'AAPL', 'BA', 'GOOGL', 'AMZN', 'TSLA', 'NVDA', 'JPM', 'V', 'MA',
        'WMT', 'PG', 'UNH', 'HD', 'DIS', 'CRM', 'ADBE', 'VZ', 'KO', 'INTC',
        'NFLX', 'CMCSA', 'PFE', 'ABT', 'T', 'NKE', 'MRK', 'PEP', 'ABBV', 'CVX'
    ]


    #Sidebar
    st.sidebar.title('Filtros')
    qutd_info = st.sidebar.number_input('Nº de Informações na tabela:', min_value=1, max_value=50, value=10)
    symbol = st.sidebar.selectbox('Escolha o simbolo da ação:', simbolos)


    #Dashboard
    st.title('Intraday')
    st.write('Este painel apresenta dados Intraday da Bolsa de Valores usando a Alpha Vantage.')

    if symbol:
        interval = '15min'
        data, meta_data = ts.get_intraday(symbol=symbol, interval=interval, outputsize='full')
        data['Variacao'] = data['4. close'].diff()
        data['Variacao_Porcentagem'] = (data['Variacao'] / data['4. close'].shift(1)) * 100

        st.subheader('Dados de Preços de Fechamento')
        st.write(data.head(qutd_info))

        st.subheader('Gráfico de Preços de Fechamento')
        fig_preco = px.line(data, x=data.index, y='4. close', labels={'x': 'Data', 'y': 'Preço de Fechamento'})
        fig_preco.update_layout(title=f'Preços de Fechamento para {symbol}')

        st.plotly_chart(fig_preco)

        st.subheader('Variação de Preço em Porcentagem')
        fig_variacao = px.line(data, x=data.index, y='Variacao_Porcentagem', labels={'x': 'Data', 'y': 'Variação de Preço (%)'})
        fig_variacao.update_layout(title=f'Variação de Preço em Porcentagem para {symbol}')

        st.plotly_chart(fig_variacao)

        st.subheader('Volume de Negociações')
        fig_volume = px.bar(data, x=data.index, y='5. volume', labels={'x': 'Data', 'y': 'Volume de Negociações'})
        fig_volume.update_layout(title=f'Volume de Negociações para {symbol}')

        st.plotly_chart(fig_volume)

        #Sidebar
        st.sidebar.subheader('Informações da Ação')
        st.sidebar.write(f"Nome da Empresa: {meta_data['2. Symbol']}")
        st.sidebar.write(f"Última Data Disponível: {meta_data['3. Last Refreshed']}")

        start_date = st.sidebar.date_input("Data de Início", data.index.min())
        end_date = st.sidebar.date_input("Data Final", data.index.max())

        filtered_data = data.loc[start_date:end_date]

        st.set_option('deprecation.showPyplotGlobalUse', False)
        ''')

    st.markdown('<hr style="margin-top: 50px;">', unsafe_allow_html=True)
    st.write("© 2023 Lucas de Sousa Nobrega.")
def pagina_daily():
    st.title('Daily')
    st.write('Esta página apresenta dados Daily detalhados da Bolsa de Valores.')

    #API Request
    ALPHA_VANTAGE_API_KEY = 'TCHQ4YXXQ2B07DR4'
    ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')

    #Ações
    simbolos = [
        'MSFT', 'AAPL', 'BA', 'GOOGL', 'AMZN', 'TSLA', 'NVDA', 'JPM', 'V', 'MA',
        'WMT', 'PG', 'UNH', 'HD', 'DIS', 'CRM', 'ADBE', 'VZ', 'KO', 'INTC',
        'NFLX', 'CMCSA', 'PFE', 'ABT', 'T', 'NKE', 'MRK', 'PEP', 'ABBV', 'CVX'
    ]

    #Sidebar
    st.sidebar.title('Filtros')
    qutd_info = st.sidebar.number_input('Nº de Informações na tabela:', min_value=1, max_value=50, value=10)
    symbol = st.sidebar.selectbox('Escolha o simbolo da ação:', simbolos)

    if symbol:
        data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')
        data['Variacao'] = data['4. close'].diff()
        data['Variacao_Porcentagem'] = (data['Variacao'] / data['4. close'].shift(1)) * 100

        st.subheader('Dados de Preços de Fechamento')
        st.write(data.head(qutd_info))

        # Gráfico de Preços de Fechamento
        st.subheader('Gráfico de Preços de Fechamento')
        fig_preco = px.line(data, x=data.index, y='4. close', labels={'x': 'Data', 'y': 'Preço de Fechamento'}, title=f'Preços de Fechamento para {symbol}')
        fig_preco.update_traces(hovertemplate='Data: %{x}<br>Preço de Fechamento: %{y}')
        st.plotly_chart(fig_preco)

        # Gráfico de Variação de Preço em Porcentagem
        st.subheader('Variação de Preço em Porcentagem')
        fig_variacao = px.line(data, x=data.index, y='Variacao_Porcentagem', labels={'x': 'Data', 'y': 'Variação de Preço (%)'}, title=f'Variação de Preço em Porcentagem para {symbol}')
        fig_variacao.update_traces(hovertemplate='Data: %{x}<br>Variação de Preço: %{y:.2f}%')
        st.plotly_chart(fig_variacao)

        st.subheader('Volume de Negociações')
        fig_volume = px.bar(data, x=data.index, y='5. volume', labels={'x': 'Data', 'y': 'Volume de Negociações'}, title=f'Volume de Negociações para {symbol}')
        fig_volume.update_traces(hovertemplate='Data: %{x}<br>Volume: %{y}')
        st.plotly_chart(fig_volume)

        #Sidebar
        st.sidebar.subheader('Informações da Ação')
        st.sidebar.write(f"Nome da Empresa: {meta_data['2. Symbol']}")
        st.sidebar.write(f"Última Data Disponível: {meta_data['3. Last Refreshed']}")

        start_date = st.sidebar.date_input("Data de Início", data.index.min())
        end_date = st.sidebar.date_input("Data Final", data.index.max())

        filtered_data = data.loc[start_date:end_date]

        st.set_option('deprecation.showPyplotGlobalUse', False)  # Para suprimir um aviso de depreciação
        #'''

        st.title('')
        st.title('')
        st.subheader('Código da Página:')

        code = st.code('''def pagina_daily():
    st.title('Daily')
    st.write('Esta página apresenta dados Daily detalhados da Bolsa de Valores.')

    #API Request
    ALPHA_VANTAGE_API_KEY = 'TCHQ4YXXQ2B07DR4'
    ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')

    #Ações
    simbolos = [
        'MSFT', 'AAPL', 'BA', 'GOOGL', 'AMZN', 'TSLA', 'NVDA', 'JPM', 'V', 'MA',
        'WMT', 'PG', 'UNH', 'HD', 'DIS', 'CRM', 'ADBE', 'VZ', 'KO', 'INTC',
        'NFLX', 'CMCSA', 'PFE', 'ABT', 'T', 'NKE', 'MRK', 'PEP', 'ABBV', 'CVX'
    ]

    #Sidebar
    st.sidebar.title('Filtros')
    qutd_info = st.sidebar.number_input('Nº de Informações na tabela:', min_value=1, max_value=50, value=10)
    symbol = st.sidebar.selectbox('Escolha o simbolo da ação:', simbolos)

    if symbol:
        data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')
        data['Variacao'] = data['4. close'].diff()
        data['Variacao_Porcentagem'] = (data['Variacao'] / data['4. close'].shift(1)) * 100

        st.subheader('Dados de Preços de Fechamento')
        st.write(data.head(qutd_info))

        # Gráfico de Preços de Fechamento
        st.subheader('Gráfico de Preços de Fechamento')
        fig_preco = px.line(data, x=data.index, y='4. close', labels={'x': 'Data', 'y': 'Preço de Fechamento'}, title=f'Preços de Fechamento para {symbol}')
        fig_preco.update_traces(hovertemplate='Data: %{x}<br>Preço de Fechamento: %{y}')
        st.plotly_chart(fig_preco)

        # Gráfico de Variação de Preço em Porcentagem
        st.subheader('Variação de Preço em Porcentagem')
        fig_variacao = px.line(data, x=data.index, y='Variacao_Porcentagem', labels={'x': 'Data', 'y': 'Variação de Preço (%)'}, title=f'Variação de Preço em Porcentagem para {symbol}')
        fig_variacao.update_traces(hovertemplate='Data: %{x}<br>Variação de Preço: %{y:.2f}%')
        st.plotly_chart(fig_variacao)

        st.subheader('Volume de Negociações')
        fig_volume = px.bar(data, x=data.index, y='5. volume', labels={'x': 'Data', 'y': 'Volume de Negociações'}, title=f'Volume de Negociações para {symbol}')
        fig_volume.update_traces(hovertemplate='Data: %{x}<br>Volume: %{y}')
        st.plotly_chart(fig_volume)

        #Sidebar
        st.sidebar.subheader('Informações da Ação')
        st.sidebar.write(f"Nome da Empresa: {meta_data['2. Symbol']}")
        st.sidebar.write(f"Última Data Disponível: {meta_data['3. Last Refreshed']}")

        start_date = st.sidebar.date_input("Data de Início", data.index.min())
        end_date = st.sidebar.date_input("Data Final", data.index.max())

        filtered_data = data.loc[start_date:end_date]

        st.set_option('deprecation.showPyplotGlobalUse', False)''')
    st.markdown('<hr style="margin-top: 50px;">', unsafe_allow_html=True)
    st.write("© 2023 Lucas de Sousa Nobrega.")

def pagina_status():
    st.title('Status das Bolsas')
    st.write('Está página apresenta as informações das bolsas de valores como: Está aberto ou fechado e horário de funcionamento')

    url = 'https://www.alphavantage.co/query?function=MARKET_STATUS&apikey={ALPHA_VANTAGE_API_KEY}'
    r = requests.get(url)
    data = r.json()
    df = pd.DataFrame(data)
    df

    st.markdown('<hr style="margin-top: 50px;">', unsafe_allow_html=True)
    st.write("© 2023 Lucas de Sousa Nobrega.")

def codigo_completo():
    st.code('''
    #Página Inicial
                    
    def pagina_inicio():
    st.title('Acompanhamento da Bolsa de Valores D-1')
    st.subheader('Informações Gerais')
    st.write('')
    st.write('')
    st.write('Olá, seja muito bem vindo(a) ao dash para acompanhamento da bolsa de valores.')
    st.write('Esse painel foi construido unicamente como forma de estudo, sem fins lucrativos. Espero que aqui consiga encontrar informações relevantes para você e qualquer dica que tenha, pode estar entrando em contato comigo utilizando as informações abaixo.')
    st.write('')
    st.write('')
    st.subheader("Informações de Contato")

    # Informações de contato em Markdown
    informacoes_contato = """
    **Endereço:** Rua Projetada 2, Número 57 - 
    **Cidade:** Massaranduba - 
    **CEP:** 58120-000

    **Telefone:** (83) 9 9365-2937
    **Email:** lucas.nobrega_sousa@outlook.com
    """

    # Exibir as informações de contato usando o widget Markdown
    st.markdown(informacoes_contato)
            
            
    #Página Intraday

    def pagina_intraday():
    #API Request

    ALPHA_VANTAGE_API_KEY = 'TCHQ4YXXQ2B07DR4'
    ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')

    #Ações
    simbolos = [
        'MSFT', 'AAPL', 'BA', 'GOOGL', 'AMZN', 'TSLA', 'NVDA', 'JPM', 'V', 'MA',
        'WMT', 'PG', 'UNH', 'HD', 'DIS', 'CRM', 'ADBE', 'VZ', 'KO', 'INTC',
        'NFLX', 'CMCSA', 'PFE', 'ABT', 'T', 'NKE', 'MRK', 'PEP', 'ABBV', 'CVX'
    ]


    #Sidebar
    st.sidebar.title('Filtros')
    qutd_info = st.sidebar.number_input('Nº de Informações na tabela:', min_value=1, max_value=50, value=10)
    symbol = st.sidebar.selectbox('Escolha o simbolo da ação:', simbolos)


    #Dashboard
    st.title('Intraday')
    st.write('Este painel apresenta dados Intraday da Bolsa de Valores usando a Alpha Vantage.')

    if symbol:
        interval = '15min'
        data, meta_data = ts.get_intraday(symbol=symbol, interval=interval, outputsize='full')
        data['Variacao'] = data['4. close'].diff()
        data['Variacao_Porcentagem'] = (data['Variacao'] / data['4. close'].shift(1)) * 100

        st.subheader('Dados de Preços de Fechamento')
        st.write(data.head(qutd_info))

        st.subheader('Gráfico de Preços de Fechamento')
        fig_preco = px.line(data, x=data.index, y='4. close', labels={'x': 'Data', 'y': 'Preço de Fechamento'})
        fig_preco.update_layout(title=f'Preços de Fechamento para {symbol}')

        st.plotly_chart(fig_preco)

        st.subheader('Variação de Preço em Porcentagem')
        fig_variacao = px.line(data, x=data.index, y='Variacao_Porcentagem', labels={'x': 'Data', 'y': 'Variação de Preço (%)'})
        fig_variacao.update_layout(title=f'Variação de Preço em Porcentagem para {symbol}')

        st.plotly_chart(fig_variacao)

        st.subheader('Volume de Negociações')
        fig_volume = px.bar(data, x=data.index, y='5. volume', labels={'x': 'Data', 'y': 'Volume de Negociações'})
        fig_volume.update_layout(title=f'Volume de Negociações para {symbol}')

        st.plotly_chart(fig_volume)

        #Sidebar
        st.sidebar.subheader('Informações da Ação')
        st.sidebar.write(f"Nome da Empresa: {meta_data['2. Symbol']}")
        st.sidebar.write(f"Última Data Disponível: {meta_data['3. Last Refreshed']}")

        start_date = st.sidebar.date_input("Data de Início", data.index.min())
        end_date = st.sidebar.date_input("Data Final", data.index.max())

        filtered_data = data.loc[start_date:end_date]

        st.set_option('deprecation.showPyplotGlobalUse', False)
            

    #Página Daily
                       
    def pagina_daily():
    st.title('Daily')
    st.write('Esta página apresenta dados Daily detalhados da Bolsa de Valores.')

    #API Request
    ALPHA_VANTAGE_API_KEY = 'TCHQ4YXXQ2B07DR4'
    ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')

    #Ações
    simbolos = [
        'MSFT', 'AAPL', 'BA', 'GOOGL', 'AMZN', 'TSLA', 'NVDA', 'JPM', 'V', 'MA',
        'WMT', 'PG', 'UNH', 'HD', 'DIS', 'CRM', 'ADBE', 'VZ', 'KO', 'INTC',
        'NFLX', 'CMCSA', 'PFE', 'ABT', 'T', 'NKE', 'MRK', 'PEP', 'ABBV', 'CVX'
    ]

    #Sidebar
    st.sidebar.title('Filtros')
    qutd_info = st.sidebar.number_input('Nº de Informações na tabela:', min_value=1, max_value=50, value=10)
    symbol = st.sidebar.selectbox('Escolha o simbolo da ação:', simbolos)

    if symbol:
        data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')
        data['Variacao'] = data['4. close'].diff()
        data['Variacao_Porcentagem'] = (data['Variacao'] / data['4. close'].shift(1)) * 100

        st.subheader('Dados de Preços de Fechamento')
        st.write(data.head(qutd_info))

        # Gráfico de Preços de Fechamento
        st.subheader('Gráfico de Preços de Fechamento')
        fig_preco = px.line(data, x=data.index, y='4. close', labels={'x': 'Data', 'y': 'Preço de Fechamento'}, title=f'Preços de Fechamento para {symbol}')
        fig_preco.update_traces(hovertemplate='Data: %{x}<br>Preço de Fechamento: %{y}')
        st.plotly_chart(fig_preco)

        # Gráfico de Variação de Preço em Porcentagem
        st.subheader('Variação de Preço em Porcentagem')
        fig_variacao = px.line(data, x=data.index, y='Variacao_Porcentagem', labels={'x': 'Data', 'y': 'Variação de Preço (%)'}, title=f'Variação de Preço em Porcentagem para {symbol}')
        fig_variacao.update_traces(hovertemplate='Data: %{x}<br>Variação de Preço: %{y:.2f}%')
        st.plotly_chart(fig_variacao)

        st.subheader('Volume de Negociações')
        fig_volume = px.bar(data, x=data.index, y='5. volume', labels={'x': 'Data', 'y': 'Volume de Negociações'}, title=f'Volume de Negociações para {symbol}')
        fig_volume.update_traces(hovertemplate='Data: %{x}<br>Volume: %{y}')
        st.plotly_chart(fig_volume)

        #Sidebar
        st.sidebar.subheader('Informações da Ação')
        st.sidebar.write(f"Nome da Empresa: {meta_data['2. Symbol']}")
        st.sidebar.write(f"Última Data Disponível: {meta_data['3. Last Refreshed']}")

        start_date = st.sidebar.date_input("Data de Início", data.index.min())
        end_date = st.sidebar.date_input("Data Final", data.index.max())

        filtered_data = data.loc[start_date:end_date]

        st.set_option('deprecation.showPyplotGlobalUse', False)''')

    st.markdown('<hr style="margin-top: 50px;">', unsafe_allow_html=True)
    st.write("© 2023 Lucas de Sousa Nobrega.")

#Seletor de Página
pagina_selecionada = st.sidebar.selectbox('Escolha uma página:', ('Página Inicial','Página Intraday', 'Página Daily','Código Completo'))

if pagina_selecionada == 'Página Inicial':
    pagina_inicio()
if pagina_selecionada == 'Página Intraday':
    pagina_intraday()
if pagina_selecionada == 'Página Daily':
    pagina_daily()
if pagina_selecionada == 'Status da Bolsa':
    pagina_status()
if (pagina_selecionada == 'Código Completo'):
    codigo_completo()