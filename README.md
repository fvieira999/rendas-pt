Notas para me orientar por enuanto
## Por enquanto ignoramos a fiabilidade dos dados, voltar a isto mais tarde quanto tivermos uma base sólida, por agora fazemos apenas:
Vamos avaliar apenas a mediana e analisar apenas por concelho, portanto só precisamos do 0014711.
Assim só precisamos também de uma tabela de 4 colunas: geocod, nome, ano, renda


## 0014711
O que é: renda por m² dos novos contratos de arrendamento, por território e por ano

formato:
dicionário de dados 
"2020": [registo, registo, ...],
"2021": [registo, registo, ...],
...
"2025": [...]

cada registo é um dicionário por sua vez:
geocod: "1A01114"        → código do território
geodsg: "Vila Franca de Xira"
dim_3_t: "2.º quartil"   → qual dos 3 valores é este
valor: "10.53"           → a renda em €/m² (vem como texto!)

Ou seja por cada conselho e cada ano temos 3 valores:
o 1.º quartil, o 2.º quartil e o 3.º quartil. O 2.º quartil é a mediana, a renda “do meio”

Nota: quando não há dados o valor é "-"
