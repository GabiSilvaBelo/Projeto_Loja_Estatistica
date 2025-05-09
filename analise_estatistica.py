import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leitura dos dados
df = pd.read_csv("dados_vendas.csv")

# Cálculo do lucro por produto
df["lucro_total"] = (df["preco_unitario"] - df["custo_unitario"]) * df["quantidade_vendida"]

# Estatísticas descritivas
print("📊 Estatísticas:")
print(df.describe())

# Produto com maior lucro
produto_top = df.loc[df["lucro_total"].idxmax()]
print(f"\n🏆 Produto mais lucrativo: {produto_top['produto']} com R${produto_top['lucro_total']}")

# Gráfico de lucros
sns.barplot(x="produto", y="lucro_total", data=df)
plt.title("Lucro Total por Produto")
plt.ylabel("Lucro (R$)")
plt.show()
