# Label-Propagation
Algoritmo de detecção de comunidades em redes baseado no algoritmo de label propagation.

# Como clonar
git clone <https://github.com/GiovannaPazP/Label-Propagation.git>
cd <pasta>

# Como criar o ambiente conda
conda env create -f environment.yml

# Relatório

Os testes funcionaram da seguinte forma:
Para cada um dos arquivos foram executados 10x o algoritmo de detecção de comunidades label propagation. Nessas execuções os rótulos obtidos foram normalizados para permitir contagem (verificação de igualdade do conjunto) e então é contado a quantidade de vezes que o conjunto aparece.

Os testes não foram feitos com seed fixa.

## rede1_duas_comunidades.csv
De 8 em 10 vezes foi capaz de identificar corretamente as partições, separando em grupos com rótulos {3,4,5} e {0, 1, 2}. (imagem: rede1_1)
2 em 10 vezes separou  em {1,2,3,4,5,6}. (imagem: rede1_2)

## rede2.csv
Essa rede foi mais instável.

4 em 10 vezes foi capaz de identificar corretamente as partições, separando em grupos com rótulos {4,5,6} e {0, 1, 2, 3}. (imagem: rede2_2)
6 em 10 vezes separou em {1,2,3,4,5,6}, sendo o mais comum. (imagem: rede2_1)

# Problemas
A rede2.csv é mais dificil de dividir as partições, mais instável. Isso ocorre devido ao nó 4 ficar com conexões empatadas e ao envolvimento da aleatoriedade na hora de escolher o rótulo.
