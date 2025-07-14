import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar estilo dos gráficos
sns.set(style="whitegrid")

# Carregar dados (arquivos devem estar na mesma pasta do script)
orders = pd.read_csv("olist_orders_dataset.csv", parse_dates=["order_purchase_timestamp"])
items = pd.read_csv("olist_order_items_dataset.csv")
products = pd.read_csv("olist_products_dataset.csv")

# Converter para datetime a coluna de entrega
orders['order_delivered_carrier_date'] = pd.to_datetime(orders['order_delivered_carrier_date'])

# 1) Distribuição do tempo de entrega
orders['delivery_time_days'] = (orders['order_delivered_carrier_date'] - orders['order_purchase_timestamp']).dt.days
delivery_times_valid = orders['delivery_time_days'][orders['delivery_time_days'] >= 0]

plt.figure(figsize=(10,5))
sns.histplot(delivery_times_valid, bins=30)
plt.title("Distribuição do tempo de entrega (valores positivos)")
plt.xlabel("Dias para entrega")
plt.ylabel("Frequência")
plt.show()

# 2) Média e mediana do preço por categoria de produto
items_products = items.merge(products, on="product_id")
preco_por_categoria = items_products.groupby("product_category_name")['price'].agg(['mean', 'median']).sort_values(by='mean', ascending=False)
print("\nMédia e mediana do preço por categoria de produto:")
print(preco_por_categoria.head(10))

# 3) Boxplot para identificar outliers no preço dos produtos
plt.figure(figsize=(10,5))
sns.boxplot(x=items['price'])
plt.title("Boxplot dos preços dos produtos")
plt.show()

# 4) Correlação e dispersão entre preço do produto e valor do frete
correlation = items[['price', 'freight_value']].corr()
print("\nCorrelação entre preço e frete:")
print(correlation)

plt.figure(figsize=(10,5))
sns.scatterplot(x='price', y='freight_value', data=items, alpha=0.5)
plt.title("Dispersão: Preço x Frete")
plt.xlabel("Preço do produto")
plt.ylabel("Valor do frete")
plt.show()

# 5) Volume de pedidos por mês (sazonalidade)
orders['order_month'] = orders['order_purchase_timestamp'].dt.to_period('M')
pedidos_por_mes = orders.groupby('order_month').size()

plt.figure(figsize=(12,6))
pedidos_por_mes.plot(kind='line', marker='o')
plt.title("Volume de pedidos por mês")
plt.xlabel("Mês")
plt.ylabel("Número de pedidos")
plt.xticks(rotation=45)
plt.show()
