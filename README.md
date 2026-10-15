# Análise de dados eleitorais

Aplicação educacional em Python para explorar dados eleitorais fictícios de 2024. O programa lê um CSV, apresenta um resumo e permite exibir ou exportar amostras, votos por partido e candidatos eleitos para prefeito e vereador.

O código está neste repositório Git separado e é incluído como submodule em [`FGiacobe/SCTEC_Data_Analysis`](https://github.com/FGiacobe/SCTEC_Data_Analysis). Como os imports e o ambiente Python são configurados pelo projeto principal, clone e execute o projeto completo conforme as instruções abaixo.

## Requisitos

- Git.
- [`uv`](https://docs.astral.sh/uv/).
- Python 3.14 ou superior. O `uv` pode instalá-lo automaticamente.

## Clonar o projeto

Clone o repositório principal incluindo os submodules:

```sh
git clone --recurse-submodules git@github.com:FGiacobe/SCTEC_Data_Analysis.git
cd SCTEC_Data_Analysis
```

Se o projeto já foi clonado sem os submodules, inicialize-os na raiz do projeto:

```sh
git submodule update --init --recursive
```

## Instalar e executar

Na raiz do repositório principal, instale o Python necessário e sincronize as dependências:

```sh
uv python install
uv sync
```

Execute a aplicação:

```sh
uv run python -m packages.elections.main
```

O programa lê `packages/elections/data/eleicoes.csv`, exibe um resumo e uma amostra no terminal e apresenta um menu. Escolha uma das opções para exportar resultados ou selecione `5` para sair. Os CSVs exportados são gravados na pasta `packages/elections/data/`; arquivos gerados com prefixo `ex_` são ignorados pelo Git.

Para fazer um teste rápido sem exportar arquivos:

```sh
printf '5\n' | uv run python -m packages.elections.main
```

Não há uma suíte de testes automatizados configurada atualmente. O comando acima verifica que o programa inicia, carrega os dados e encerra pelo menu.

## Dados

O conjunto incluído é fictício e destinado a fins educacionais. A estrutura e os tipos das colunas estão descritos em [`docs/Data-Info.md`](docs/Data-Info.md).

## Trabalhar com o submodule

`packages/elections` tem histórico, branch e remoto próprios. Para desenvolver nele, entre na pasta e confirme que está na branch `main`:

```sh
cd packages/elections
git switch main
```

Adicione somente os arquivos que deseja publicar. Por exemplo, para publicar uma alteração neste README:

```sh
git add README.md
git commit -m "Descreve a alteração"
git push origin main
```

Depois, na raiz do repositório principal, registre o novo commit apontado pelo submodule e publique essa atualização:

```sh
cd ../..
git add packages/elections
git commit -m "Atualiza submodule elections"
git push origin main
```

São dois pushes separados: o primeiro publica o conteúdo do submodule; o segundo publica no repositório principal a referência ao commit escolhido.

Para receber atualizações já registradas pelo projeto principal:

```sh
git pull
git submodule update --init --recursive
```

Para atualizar intencionalmente o submodule para o commit mais recente da branch remota `main`, a partir da raiz do projeto:

```sh
git submodule update --remote --merge packages/elections
git add packages/elections
git commit -m "Atualiza submodule elections"
git push origin main
```

O projeto principal aponta para um commit específico do submodule. Assim, um `git pull` sozinho não move o submodule para a versão mais recente da branch remota; use os comandos de atualização acima quando necessário.
