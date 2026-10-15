# Informações sobre os dados

Este documento apresenta informações sobre os dados eleitorais fictícios usados no projeto, incluindo a estrutura do arquivo CSV e os tipos de dados de cada coluna.

## Estrutura do arquivo CSV

O arquivo CSV, chamado `eleicoes.csv`, contém as seguintes colunas:

| Nome da coluna | Descrição | Tipo de dado | Exemplo |
|-------------|-------------|-----------|---------|
| ano         | Ano da eleição | int64 | 2024 |
| estado      | Estado onde ocorreu a eleição | category | SP |
| cidade      | Cidade onde ocorreu a eleição | category | São Paulo |
| zona        | Zona eleitoral | category | 1 |
| secao       | Seção eleitoral | category | 1 |
| cargo       | Cargo em disputa | category | Prefeito |
| candidato   | Nome do candidato | category | John Doe |
| partido     | Partido político | category | ABC |
| numero      | Número do candidato | category | 12345 |
| votos       | Número de votos recebidos | int64 | 1000 |

## Exemplo de dados

| ano | estado | cidade | zona | secao | cargo | candidato | partido | numero | votos |
|-----|--------|--------|------|-------|-------|-----------|---------|--------|-------|
| 2024 | SP     | São Paulo | 0001 | 0001  | Prefeito | John Doe  | ABC     | 12345  | 1000  |

## Tamanho do conjunto de dados

O arquivo CSV contém um conjunto de dados com 32 linhas e 10 colunas, cada uma representando um registro único de votação.

## Observações

- O tipo de dado `category` é usado em colunas com um conjunto limitado de valores possíveis para otimizar o uso de memória.
- O tipo de dado `int64` é usado em colunas numéricas para garantir cálculos precisos e uma faixa de valores suficiente.
