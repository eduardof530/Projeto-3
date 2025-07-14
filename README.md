# Projeto-4

# Projeto-4

# 📊 Análise de Dados - E-commerce Brasileiro (Olist)

Este projeto realiza uma análise completa do comportamento de pedidos, produtos, vendedores e frete com base nos dados públicos da empresa Olist. Ele foi desenvolvido como projeto final de um curso de análise de dados, abrangendo limpeza, exploração, visualização e geração de insights a partir dos dados.

---

## 📁 Base de Dados

- Dataset utilizado: **Brazilian E-Commerce Public Dataset by Olist**
- Disponível em: [https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

---

## 🛠️ Ferramentas Utilizadas

- **Python** (Pandas, Matplotlib, Seaborn)
- **Looker Studio** (Visualizações interativas)
- **PyCharm**
- **GitHub Desktop** (versionamento)
- **GitHub Pages** (repositório do projeto)

---

## 📂 Organização do Projeto

- `orders_limpos.csv` – Dados limpos dos pedidos
- `items_limpos.csv` – Itens de pedidos tratados
- `products_limpos.csv` – Dados de produtos
- `customers_limpos.csv` – Dados de clientes
- `sellers_limpos.csv` – Dados de vendedores
- `analise_exploratoria.py` – Código Python com análises e gráficos
- `limpeza_preparacao.py` – Código de limpeza e criação de colunas derivadas
- `dashboard_looker_studio` – Link para visualização (veja abaixo)

---

## 📈 Principais Análises e Gráficos Criados

1. **Gráfico de barras - Quantidade de produtos por categoria**  
   - Representa a diversidade de produtos disponíveis em cada categoria.  
   - Insight: Categorias como “cama, mesa e banho” e “beleza e saúde” apresentam alta variedade, indicando foco da empresa nessas áreas.  
   - Observação: Este gráfico ajuda a identificar portfólios amplos e possíveis oportunidades para ampliar ou reduzir ofertas em determinadas categorias.

2. **Gráfico de linha - Valor total das vendas ao longo do tempo**  
   - Exibe a variação mensal do valor total vendido entre 2016 e 2018.  
   - Insight: Houve crescimento gradual nas vendas até o final de 2017, com uma leve queda em 2018, sugerindo sazonalidades ou mudanças de mercado.

3. **Gráfico de dispersão - Comparativo de preço e frete por vendedor**  
   - Analisa a relação entre o preço dos produtos e o valor do frete cobrados por diferentes vendedores.  
   - Insight: Identificação de outliers com fretes muito altos, sugerindo necessidade de revisão nas políticas de frete ou possíveis erros cadastrais.

4. **Tabela dinâmica - Valor total de vendas por vendedor**  
   - Mostra o desempenho financeiro de cada vendedor na plataforma.  
   - Insight: Alguns vendedores concentram grande parte das vendas, indicando potencial foco para negociações ou parcerias estratégicas.

5. **Gráfico de pizza - Distribuição percentual dos status dos pedidos**  
   - Percentual de pedidos entregues, cancelados, em transporte, etc.  
   - Insight: Mais de 95% dos pedidos foram entregues com sucesso, demonstrando eficiência logística.

---

## 📊 Dashboard Interativo

> ✅ Veja o dashboard completo no Looker Studio:  
[🔗 Link para o Dashboard](#) *(https://lookerstudio.google.com/reporting/b39400ac-2060-4146-b647-a9e920057ebc)*

Inclui:  
- Filtros interativos por ano e categoria  
- Métricas por vendedor, produto, e tempo de entrega  
- Navegação em uma única página  

---

## ▶️ Como Usar

1. Faça o download do dataset completo pelo link do Kaggle.  
2. Coloque os arquivos CSV na mesma pasta dos scripts Python.  
3. Execute o script `limpeza_preparacao.py` para gerar os arquivos tratados.  
4. Explore os gráficos gerados com `analise_exploratoria.py`.  
5. No Looker Studio, importe os arquivos `*_limpos.csv` para criar visualizações interativas.  

---

## 📌 Observações Finais

- Alguns valores extremos (outliers) foram mantidos para análise crítica.  
- Os dados foram tratados com base em critérios de completude e consistência.  
- A análise visa identificar padrões de venda, entrega e categorias relevantes ao negócio.  

---

## 👨‍💻 Autor

Projeto desenvolvido por [Eduardo Farias] como parte da avaliação final do curso de análise de dados da EBAC.

