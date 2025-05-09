import numpy as np
import matplotlib.pyplot as plt

# Parâmetros para simular o lucro com variação de preço
custos = 20  # custo fixo de produção
precos = np.linspace(30, 100, 100)
quantidade_vendida = 300 - 2 * (precos - 30)  # simulação de queda na demanda

lucros = (precos - custos) * quantidade_vendida

# Encontrar o preço ótimo
indice_max = np.argmax(lucros)
preco_otimo = precos[indice_max]
lucro_maximo = lucros[indice_max]

print(f"💰 Preço ótimo: R${preco_otimo:.2f}")
print(f"📈 Lucro máximo: R${lucro_maximo:.2f}")

# Plot
plt.plot(precos, lucros, label="Lucro")
plt.axvline(preco_otimo, color="red", linestyle="--", label=f"Preço ótimo: R${preco_otimo:.2f}")
plt.title("Otimização do Preço de Venda")
plt.xlabel("Preço de Venda (R$)")
plt.ylabel("Lucro Total (R$)")
plt.legend()
plt.show()
