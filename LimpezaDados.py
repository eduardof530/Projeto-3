import pandas as pd

# --- Carregar dados (assumindo arquivos na mesma pasta) ---
orders = pd.read_csv("olist_orders_dataset.csv", parse_dates=["order_purchase_timestamp", "order_delivered_carrier_date"])
items = pd.read_csv("olist_order_items_dataset.csv")
products = pd.read_csv("olist_products_dataset.csv")
customers = pd.read_csv("olist_customers_dataset.csv")
sellers = pd.read_csv("olist_sellers_dataset.csv")

# --- 1. Tratar valores ausentes e inconsistências ---

print("Valores nulos em orders:")
print(orders.isnull().sum())

print("\nValores nulos em items:")
print(items.isnull().sum())

print("\nValores nulos em products:")
print(products.isnull().sum())

print("\nValores nulos em customers:")
print(customers.isnull().sum())

print("\nValores nulos em sellers:")
print(sellers.isnull().sum())

# Preencher datas com erros como NaT
orders['order_delivered_carrier_date'] = pd.to_datetime(orders['order_delivered_carrier_date'], errors='coerce')

# Remover linhas com valores críticos ausentes
orders = orders.dropna(subset=['order_id', 'order_purchase_timestamp'])
items = items.dropna(subset=['order_id', 'product_id'])
products = products.dropna(subset=['product_id'])
customers = customers.dropna(subset=['customer_id'])
sellers = sellers.dropna(subset=['seller_id'])

# Garante que só fiquem os products que estão também em items
products = products[products['product_id'].isin(items['product_id'])]

# Garante que só fiquem os items com products válidos
items = items[items['product_id'].isin(products['product_id'])]

# --- 2. Padronizar formatos de dados ---

# Garantir IDs como string
orders['order_id'] = orders['order_id'].astype(str)
items['order_id'] = items['order_id'].astype(str)
items['product_id'] = items['product_id'].astype(str)
products['product_id'] = products['product_id'].astype(str)
customers['customer_id'] = customers['customer_id'].astype(str)
sellers['seller_id'] = sellers['seller_id'].astype(str)

# Padronizar categorias para minúsculo e sem espaços extras
products['product_category_name'] = products['product_category_name'].str.lower().str.strip()

# Padronizar estados para maiúsculo em customers e sellers
customers['customer_state'] = customers['customer_state'].str.upper()
sellers['seller_state'] = sellers['seller_state'].str.upper()

# --- 3. Criar novas colunas derivadas ---

# Tempo entre compra e entrega (dias)
orders['delivery_time_days'] = (orders['order_delivered_carrier_date'] - orders['order_purchase_timestamp']).dt.days

# Valor total do pedido (preço do item + frete)
items['total_price'] = items['price'] + items['freight_value']

# --- 4. Garantir tabelas prontas para análise ---

# Remover pedidos com delivery_time_days negativo ou nulo
orders = orders[(orders['delivery_time_days'] >= 0) & (orders['delivery_time_days'].notna())]

# Resetar índices
orders = orders.reset_index(drop=True)
items = items.reset_index(drop=True)
products = products.reset_index(drop=True)
customers = customers.reset_index(drop=True)
sellers = sellers.reset_index(drop=True)

print("\nTabelas após limpeza e preparação:")
print(f"Orders: {orders.shape}")
print(f"Items: {items.shape}")
print(f"Products: {products.shape}")
print(f"Customers: {customers.shape}")
print(f"Sellers: {sellers.shape}")

# --- 5. Salvar arquivos limpos ---

orders.to_csv("orders_limpos.csv", index=False)
items.to_csv("items_limpos.csv", index=False)
products.to_csv("products_limpos.csv", index=False)
customers.to_csv("customers_limpos.csv", index=False)
sellers.to_csv("sellers_limpos.csv", index=False)

print("Arquivos limpos salvos com sucesso!")
