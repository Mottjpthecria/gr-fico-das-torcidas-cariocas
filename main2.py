import matplotlib.pyplot as plt

times = ['Flamengo','Vasco','Fluminense','Botafogo']
torcidas_nos_estadios = [45000 , 20000 , 15000 , 25000]

plt.figure(figsize=(10,6))
plt.bar(times, torcidas_nos_estadios, color=['red','black','green','white'], edgecolor= 'black')

plt.title('Número de torcedores nos Estádios (times cariocas)'),
plt.xlabel('times',fontsize=14)
plt.ylabel('Número de torcedores',fontsize=14)

for i, valor in enumerate(torcidas_nos_estadios):
    plt.text(i,valor + 500, str(valor), ha='center', fontsize=12)

    plt.grid(axis='y',linestyle="--",alpha=0.7)
    plt.tight_layout()
    plt.show()