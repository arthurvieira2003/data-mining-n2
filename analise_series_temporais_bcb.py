import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from scipy.stats import linregress
import warnings
from io import StringIO
import re
from datetime import datetime, timedelta

warnings.filterwarnings('ignore')

# Configuração para os gráficos
plt.rcParams['font.size'] = 12
plt.rcParams['figure.figsize'] = (14, 8)
plt.style.use('default')

class AnalisadorSeriesTemporaisBCB:
    """Classe para análise de séries temporais do BCB"""
    
    def __init__(self):
        self.dados = {}
        self.resultados_analise = {}
    
    def baixar_dados_bcb(self, codigo_serie, nome_serie):
        """Baixa dados da API do BCB usando código da série"""
        try:
            print(f"\n📊 Baixando dados: {nome_serie} (Código: {codigo_serie})")
            
            # URL da API do BCB - usando formato JSON com filtro de data (últimos 10 anos)
            data_final = datetime.now().strftime('%d/%m/%Y')
            data_inicial = (datetime.now() - timedelta(days=3650)).strftime('%d/%m/%Y')  # 10 anos atrás
            
            url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados?formato=json&dataInicial={data_inicial}&dataFinal={data_final}"
            
            response = requests.get(url, timeout=60)  # Aumentei timeout para 60 segundos
            
            # Verifica se houve erro HTTP
            if response.status_code != 200:
                print(f"❌ Erro HTTP {response.status_code} para {nome_serie}")
                print(f"   URL: {url}")
                return None
            
            # Processa o JSON
            dados_json = response.json()
            
            # Verifica se o conteúdo não está vazio
            if not dados_json:
                print(f"❌ Resposta vazia para {nome_serie}")
                return None
            
            # Converte JSON para DataFrame
            df = pd.DataFrame(dados_json)
            
            # Verifica se as colunas estão corretas
            if 'data' in df.columns and 'valor' in df.columns:
                # Remove espaços em branco
                df['data'] = df['data'].astype(str).str.strip()
                df['valor'] = df['valor'].astype(str).str.strip()
                
                # Remove linhas vazias
                df = df[df['data'] != '']
                df = df[df['valor'] != '']
                
                # Converte data
                df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')
                
                # Converte valor (remove espaços e converte para float)
                df['valor'] = df['valor'].str.replace(' ', '').str.replace(',', '.')
                df['valor'] = pd.to_numeric(df['valor'], errors='coerce')
                
                # Remove valores nulos
                df = df.dropna()
                
                if len(df) == 0:
                    print(f"❌ Nenhum dado válido encontrado para {nome_serie}")
                    return None
                
                print(f"✅ Dados carregados: {len(df)} observações")
                print(f"📅 Período: {df['data'].min().strftime('%m/%Y')} a {df['data'].max().strftime('%m/%Y')}")
                
                self.dados[nome_serie] = df
                return df
            else:
                print(f"❌ Erro: Colunas esperadas não encontradas. Colunas disponíveis: {df.columns.tolist()}")
                return None
                
        except Exception as e:
            print(f"❌ Erro ao baixar dados de {nome_serie}: {e}")
            return None
    
    def analisar_tendencia(self, df, nome_serie):
        """Analisa tendência da série temporal"""
        
        try:
            # Ordena por data
            df = df.sort_values('data').copy()
            
            # Converte datas para números para regressão
            df['data_num'] = df['data'].map(pd.Timestamp.timestamp)
            
            # Remove valores nulos
            mask = ~(df['data_num'].isna() | df['valor'].isna())
            x = df.loc[mask, 'data_num'].values
            y = df.loc[mask, 'valor'].values
            
            # Regressão linear
            slope, intercept, r_value, p_value, std_err = linregress(x, y)
            
            # Determina tendência
            if p_value < 0.05:  # Significativo
                if slope > 0:
                    tendencia = "📈 CRESCENTE"
                    cor_tendencia = 'green'
                else:
                    tendencia = "📉 DECRESCENTE"
                    cor_tendencia = 'red'
            else:
                tendencia = "📊 ESTÁVEL"
                cor_tendencia = 'blue'
            
            resultado = {
                'nome_serie': nome_serie,
                'tendencia': tendencia,
                'cor_tendencia': cor_tendencia,
                'slope': slope,
                'intercept': intercept,
                'r_squared': r_value**2,
                'p_value': p_value,
                'dados': df,
                'periodo': f"{df['data'].min().strftime('%m/%Y')} a {df['data'].max().strftime('%m/%Y')}",
                'observacoes': len(df),
                'valor_min': df['valor'].min(),
                'valor_max': df['valor'].max(),
                'valor_medio': df['valor'].mean()
            }
            
            self.resultados_analise[nome_serie] = resultado
            return resultado
            
        except Exception as e:
            print(f"❌ Erro na análise de {nome_serie}: {e}")
            return None
    
    def plotar_serie_temporal(self, resultado):
        """Plota série temporal com linha de tendência"""
        
        if resultado is None:
            return
        
        try:
            df = resultado['dados']
            nome_serie = resultado['nome_serie']
            
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 10))
            
            # Gráfico da série temporal
            ax1.plot(df['data'], df['valor'], 'b-', linewidth=2, alpha=0.7, label='Dados Originais')
            
            # Linha de tendência
            x_num = df['data_num'].values
            y_trend = resultado['slope'] * x_num + resultado['intercept']
            ax1.plot(df['data'], y_trend, '--', color=resultado['cor_tendencia'], linewidth=3, 
                    label=f'Tendência: {resultado["tendencia"].split(" ")[1]}')
            
            ax1.set_title(f'Série Temporal: {nome_serie}', fontsize=16, fontweight='bold')
            ax1.set_xlabel('Data', fontsize=12)
            ax1.set_ylabel('Valor (%)', fontsize=12)
            ax1.grid(True, alpha=0.3)
            ax1.legend()
            ax1.tick_params(axis='x', rotation=45)
            
            # Painel de estatísticas
            ax2.axis('off')
            stats_text = f"""
📊 ANÁLISE ESTATÍSTICA - {nome_serie}

🎯 Tendência Identificada: {resultado['tendencia']}
📐 Coeficiente Angular: {resultado['slope']:.8f}
📈 R² (Coef. Determinação): {resultado['r_squared']:.4f}
🔍 P-valor: {resultado['p_value']:.2e}
✅ Significância Estatística: {'Sim' if resultado['p_value'] < 0.05 else 'Não'} (α = 0.05)
📅 Período Analisado: {resultado['periodo']}
📊 Número de Observações: {resultado['observacoes']}
📏 Valor Mínimo: {resultado['valor_min']:.2f}%
📏 Valor Máximo: {resultado['valor_max']:.2f}%
📊 Valor Médio: {resultado['valor_medio']:.2f}%
            """
            
            ax2.text(0.05, 0.95, stats_text, transform=ax2.transAxes, fontsize=11,
                    verticalalignment='top', fontfamily='monospace',
                    bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.8))
            
            plt.tight_layout()
            
            # Salva gráfico
            nome_arquivo = f'{nome_serie.replace(" ", "_").replace("/", "_").lower()}_analise.png'
            plt.savefig(nome_arquivo, dpi=300, bbox_inches='tight')
            print(f"💾 Gráfico salvo: {nome_arquivo}")
            
            plt.show()
            
        except Exception as e:
            print(f"❌ Erro ao plotar {nome_serie}: {e}")
    
    def gerar_relatorio(self):
        """Gera relatório consolidado das análises"""
        print("\n" + "="*80)
        print("📋 RELATÓRIO CONSOLIDADO - ANÁLISE DE SÉRIES TEMPORAIS BCB")
        print("="*80)
        
        if not self.resultados_analise:
            print("⚠️ Nenhuma análise foi realizada com sucesso.")
            return
        
        print("\n🎯 RESUMO EXECUTIVO:")
        print("-" * 40)
        
        for i, (nome, resultado) in enumerate(self.resultados_analise.items(), 1):
            print(f"\n{i}. {nome}")
            print(f"   📈 Tendência: {resultado['tendencia']}")
            print(f"   📊 R²: {resultado['r_squared']:.4f}")
            print(f"   📅 Período: {resultado['periodo']}")
            print(f"   📋 Observações: {resultado['observacoes']}")
            print(f"   📐 Coef. Angular: {resultado['slope']:.8f}")
        
        print("\n" + "="*80)
        print("📊 METODOLOGIA UTILIZADA:")
        print("-" * 40)
        print("• Regressão Linear para identificação de tendências")
        print("• Teste de significância estatística (α = 0.05)")
        print("• Análise do coeficiente de determinação (R²)")
        print("• Visualização com gráficos de linha e tendência")
        
        print("\n📚 FERRAMENTAS E FONTES:")
        print("-" * 40)
        print("• Ferramenta: Python 3.x")
        print("• Bibliotecas: Pandas, NumPy, Matplotlib, SciPy")
        print("• Fonte: API do Banco Central do Brasil")
        print("• URL: https://dadosabertos.bcb.gov.br/dataset/")

def main():
    """Função principal"""
    print("🏦 ANÁLISE DE SÉRIES TEMPORAIS - BANCO CENTRAL DO BRASIL")
    print("="*60)
    
    analisador = AnalisadorSeriesTemporaisBCB()
    
    # QUESTÃO 1: Endividamento das famílias brasileiras
    print("\n📈 QUESTÃO 1: Análise do Endividamento das Famílias Brasileiras")
    print("-" * 60)
    
    # Série escolhida: Endividamento das famílias com o sistema financeiro nacional
    df_endividamento = analisador.baixar_dados_bcb(29037, "Endividamento das Famílias com SFN")
    
    if df_endividamento is not None:
        resultado = analisador.analisar_tendencia(df_endividamento, "Endividamento das Famílias com SFN")
        if resultado:
            analisador.plotar_serie_temporal(resultado)
    
    # QUESTÃO 2: Análise de outros conjuntos de dados do BCB
    print("\n📊 QUESTÃO 2: Análise de Outros Conjuntos de Dados do BCB")
    print("-" * 60)
    
    # Datasets selecionados
    datasets_q2 = [
        # Taxa SELIC
        {
            'codigo': 1178,
            'nome': 'Taxa SELIC Acumulada'
        },
        # IPCA
        {
            'codigo': 433,
            'nome': 'IPCA - Variação Mensal'
        },
        # PIB
        {
            'codigo': 4380,
            'nome': 'PIB Mensal'
        },
        # Taxa de Câmbio
        {
            'codigo': 3698,
            'nome': 'Taxa de Câmbio R$/US$ - Média'
        }
    ]
    
    for dataset in datasets_q2:
        codigo = dataset['codigo']
        nome = dataset['nome']
        
        df = analisador.baixar_dados_bcb(codigo, nome)
        
        if df is not None:
            resultado = analisador.analisar_tendencia(df, nome)
            if resultado:
                analisador.plotar_serie_temporal(resultado)
    
    # Gera relatório final
    analisador.gerar_relatorio()
    
    print("\n✅ ANÁLISE CONCLUÍDA!")
    print("📁 Gráficos salvos como arquivos PNG no diretório atual.")
    
    # Resumo de sucessos e falhas
    total_tentativas = len(datasets_q2) + 1  # +1 para endividamento
    sucessos = len(analisador.resultados_analise)
    falhas = total_tentativas - sucessos
    
    print(f"\n📊 RESUMO DA EXECUÇÃO:")
    print(f"   ✅ Análises bem-sucedidas: {sucessos}")
    print(f"   ❌ Falhas: {falhas}")
    print(f"   📈 Taxa de sucesso: {(sucessos/total_tentativas)*100:.1f}%")

if __name__ == "__main__":
    main() 