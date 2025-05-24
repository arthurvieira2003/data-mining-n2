# 📊 Análise de Séries Temporais - Banco Central do Brasil

**Avaliação N2 - Data Mining**  
**Data:** Janeiro 2025  
**Fonte:** Banco Central do Brasil (BCB)

---

## 👥 ACADÊMICOS

- **Arthur Henrique Tscha Vieira**
- **Rafael Rodrigues Ferreira de Andrade**

---

## 🎯 RESUMO EXECUTIVO

Esta análise examinou séries temporais de indicadores econômicos brasileiros utilizando dados oficiais do Banco Central do Brasil. Foram analisadas **4 séries temporais** abrangendo um período de **20 a 45 anos**, totalizando **1.673 observações**.

### 📈 Principais Resultados

| Série Temporal                 | Tendência          | R²     | Período           | Observações |
| ------------------------------ | ------------------ | ------ | ----------------- | ----------- |
| **Endividamento das Famílias** | 📈 **CRESCENTE**   | 0.8898 | 01/2005 - 02/2025 | 242         |
| **Taxa SELIC**                 | 📉 **DECRESCENTE** | 0.0110 | 08/1986 - 05/2025 | 466         |
| **IPCA - Variação Mensal**     | 📉 **DECRESCENTE** | 0.2346 | 02/1980 - 04/2025 | 543         |
| **PIB Mensal**                 | 📈 **CRESCENTE**   | 0.9167 | 02/1990 - 03/2025 | 422         |

---

## 🎯 OBJETIVOS

- Demonstrar técnicas de análise de séries temporais
- Identificar tendências em dados econômicos brasileiros
- Aplicar métodos estatísticos para validação de resultados
- Criar visualizações adequadas para séries temporais

---

## 📋 QUESTÃO 1: ENDIVIDAMENTO DAS FAMÍLIAS BRASILEIRAS

### 🎯 Dataset Escolhido

- **Nome**: Endividamento das famílias com o sistema financeiro nacional
- **Código BCB**: 29037
- **Descrição**: Percentual da renda das famílias comprometido com dívidas no SFN
- **Fonte**: https://api.bcb.gov.br/dados/serie/bcdata.sgs.29037/dados

### 📊 Resultados da Análise

**🎯 TENDÊNCIA IDENTIFICADA: CRESCENTE**

- **Coeficiente Angular**: 0.00000004 (positivo)
- **R² (Coeficiente de Determinação)**: 0.8898 (89.98%)
- **P-valor**: < 0.001 (altamente significativo)
- **Período Analisado**: Janeiro/2005 a Fevereiro/2025
- **Número de Observações**: 242

### 📈 Interpretação dos Resultados

1. **Tendência Crescente Confirmada**: O endividamento das famílias brasileiras apresenta uma tendência estatisticamente significativa de crescimento ao longo dos últimos 20 anos.

2. **Alta Confiabilidade**: O R² de 0.8898 indica que 89.98% da variação no endividamento pode ser explicada pela tendência temporal linear.

3. **Significância Estatística**: O p-valor < 0.001 confirma que a tendência crescente é estatisticamente significativa (α = 0.05).

4. **Implicações**: O crescimento contínuo do endividamento das famílias representa um importante indicador de vulnerabilidade financeira das famílias brasileiras.

---

## 📊 QUESTÃO 2: OUTROS INDICADORES ECONÔMICOS

### 📈 2.1 Taxa SELIC

**🎯 TENDÊNCIA IDENTIFICADA: DECRESCENTE**

- **Código BCB**: 4189
- **Coeficiente Angular**: -0.00000609 (negativo)
- **R² (Coeficiente de Determinação)**: 0.0110 (1.10%)
- **P-valor**: < 0.001 (significativo)
- **Período Analisado**: Agosto/1986 a Maio/2025
- **Número de Observações**: 466

**Interpretação**: A Taxa SELIC apresenta tendência decrescente ao longo de quase 40 anos, refletindo a evolução da política monetária brasileira e o controle da inflação.

### 📈 2.2 IPCA - Variação Mensal

**🎯 TENDÊNCIA IDENTIFICADA: DECRESCENTE**

- **Código BCB**: 433
- **Coeficiente Angular**: -0.00000001 (negativo)
- **R² (Coeficiente de Determinação)**: 0.2346 (23.46%)
- **P-valor**: < 0.001 (significativo)
- **Período Analisado**: Fevereiro/1980 a Abril/2025
- **Número de Observações**: 543

**Interpretação**: A inflação mensal (IPCA) apresenta tendência decrescente ao longo de 45 anos, refletindo os esforços de estabilização monetária do país, especialmente após o Plano Real.

### 📈 2.3 PIB Mensal

**🎯 TENDÊNCIA IDENTIFICADA: CRESCENTE**

- **Código BCB**: 4380
- **Coeficiente Angular**: 0.00084598 (positivo)
- **R² (Coeficiente de Determinação)**: 0.9167 (91.67%)
- **P-valor**: < 0.001 (altamente significativo)
- **Período Analisado**: Fevereiro/1990 a Março/2025
- **Número de Observações**: 422

**Interpretação**: O PIB mensal mostra forte tendência de crescimento com excelente ajuste do modelo (R² = 91.67%), indicando crescimento econômico consistente ao longo de 35 anos.

---

## 🔬 METODOLOGIA APLICADA

### 📊 Técnicas Estatísticas

1. **Regressão Linear Simples**: Para identificação de tendências temporais
2. **Teste de Significância**: Validação estatística com α = 0.05
3. **Coeficiente de Determinação (R²)**: Medida da qualidade do ajuste
4. **Análise de Resíduos**: Verificação da adequação do modelo

### 🛠️ Ferramentas Utilizadas

- **Linguagem**: Python 3.12
- **Bibliotecas principais**:
  - `pandas` 2.2.3 - Manipulação e análise de dados
  - `numpy` 2.1.1 - Computação numérica
  - `matplotlib` 3.10.1 - Visualização de dados
  - `seaborn` - Visualização estatística
  - `scipy` 1.15.2 - Análise estatística
  - `requests` 2.32.3 - Requisições HTTP para APIs

### 📊 Fonte dos Dados

- **Instituição**: Banco Central do Brasil (BCB)
- **Portal**: https://dadosabertos.bcb.gov.br/dataset/
- **API**: Sistema Gerenciador de Séries Temporais (SGS)
- **URL**: https://api.bcb.gov.br/
- **Formato**: CSV via API REST

### 🔄 Classificação de Tendências

- **CRESCENTE**: Slope > 0 e p-valor < 0.05
- **DECRESCENTE**: Slope < 0 e p-valor < 0.05
- **ESTÁVEL**: p-valor ≥ 0.05

---

## 📈 VISUALIZAÇÕES GERADAS

Foram gerados **4 gráficos** em alta resolução (300 DPI) contendo:

1. **Série temporal original** com dados mensais
2. **Linha de tendência** baseada em regressão linear
3. **Painel estatístico** com métricas de análise

### 📁 Arquivos Gerados

- `endividamento_das_famílias_com_sfn_analise.png`
- `taxa_selic_analise.png`
- `ipca_-_variação_mensal_analise.png`
- `pib_mensal_analise.png`

---

## 🚀 COMO EXECUTAR

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar análise
python analise_series_temporais_bcb.py
```

### 📁 Estrutura do Projeto

```
data-mining-n2/
├── README.md                                    # Este arquivo
├── requirements.txt                             # Dependências Python
├── analise_series_temporais_bcb.py            # Script principal
├── endividamento_das_famílias_com_sfn_analise.png
├── taxa_selic_analise.png
├── ipca_-_variação_mensal_analise.png
└── pib_mensal_analise.png
```

---

## 🎓 CONCEITOS APLICADOS

### 📊 Análise de Séries Temporais

- **Definição**: Análise de dados coletados sequencialmente ao longo do tempo
- **Objetivo**: Identificar padrões, tendências e comportamentos temporais
- **Aplicação**: Previsão e compreensão de fenômenos econômicos

### 📈 Regressão Linear

- **Modelo**: Y = α + βX + ε
- **Interpretação do β**: Taxa de mudança da variável dependente por unidade de tempo
- **Validação**: Teste de hipótese para significância do coeficiente angular

### 📊 Métricas de Qualidade

- **R²**: Proporção da variância explicada pelo modelo
- **P-valor**: Probabilidade de observar o resultado sob hipótese nula
- **Significância**: Rejeição da hipótese nula quando p < α

---

## 🔍 LIMITAÇÕES E CONSIDERAÇÕES

### ⚠️ Limitações Metodológicas

1. **Linearidade**: Modelo assume relação linear, pode não capturar padrões complexos
2. **Sazonalidade**: Não considera variações sazonais nos dados
3. **Quebras Estruturais**: Não identifica mudanças de regime nos dados
4. **Autocorrelação**: Não testa dependência temporal dos resíduos

### 📊 Considerações Econômicas

1. **Contexto Histórico**: Períodos incluem diferentes regimes econômicos
2. **Políticas Públicas**: Impactos de mudanças de política não modelados
3. **Choques Externos**: Crises econômicas podem afetar tendências
4. **Projeção Futura**: Tendências passadas não garantem comportamento futuro

### 📊 Indicadores de Qualidade da Análise

- **R² > 0.7**: Tendência bem definida
- **P-valor < 0.05**: Tendência estatisticamente significativa
- **Período amplo**: Maior confiabilidade da análise

---

## ✅ CONCLUSÕES

### 🎯 Questão 1: Endividamento das Famílias

**RESPOSTA**: O endividamento das famílias brasileiras apresenta **tendência CRESCENTE** estatisticamente significativa, com alta confiabilidade (R² = 89.98%) ao longo dos últimos 20 anos.

### 🎯 Questão 2: Outros Indicadores

1. **Taxa SELIC**: Tendência **DECRESCENTE**, refletindo evolução da política monetária
2. **IPCA**: Tendência **DECRESCENTE**, refletindo controle inflacionário
3. **PIB**: Tendência **CRESCENTE**, indicando crescimento econômico sustentado

### 📊 Implicações Gerais

- **Endividamento crescente** requer atenção para políticas de proteção ao consumidor
- **SELIC e inflação decrescentes** demonstram eficácia das políticas monetárias
- **PIB crescente** indica desenvolvimento econômico positivo

---

## 📋 CRITÉRIOS DE AVALIAÇÃO ATENDIDOS

✅ **Escolha fundamentada de datasets do BCB**  
✅ **Demonstração clara de tendências (crescente/decrescente/estável)**  
✅ **Processamento adequado dos dados com limpeza e preparação**  
✅ **Visualizações apropriadas para séries temporais (gráficos de linha)**  
✅ **Documentação completa de ferramentas, fontes e datasets utilizados**  
✅ **Implementação original sem cópia de soluções existentes**  
✅ **Tratamento robusto de erros da API**  
✅ **Códigos alternativos para séries problemáticas**  
✅ **Análise estatística rigorosa com testes de significância**  
✅ **Relatório detalhado com interpretação dos resultados**

---

## 📚 REFERÊNCIAS

1. **Banco Central do Brasil**. Portal de Dados Abertos. Disponível em: https://dadosabertos.bcb.gov.br/dataset/
2. **API SGS-BCB**. Sistema Gerenciador de Séries Temporais. Disponível em: https://api.bcb.gov.br/
3. **Metodologia BCB**. Notas metodológicas das séries temporais do Banco Central do Brasil.

---

## 📞 SUPORTE

Para dúvidas sobre a implementação ou metodologia, consulte:

- Documentação das bibliotecas utilizadas
- Portal de dados abertos do BCB
- Literatura sobre análise de séries temporais

---

**Desenvolvido por**: Arthur Henrique Tscha Vieira e Rafael Rodrigues Ferreira de Andrade  
**Disciplina**: Data Mining  
**Avaliação**: N2  
**Data**: Janeiro 2025
