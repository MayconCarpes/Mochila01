# 🎒 Problema da Mochila 0/1 — Meta-heurísticas

Resolução do Problema da Mochila 0/1 utilizando duas meta-heurísticas:

- **Busca Tabu** (meta-heurística local)
- **Algoritmo Genético** (meta-heurística populacional)

Testadas em **9 instâncias benchmark** com soluções ótimas conhecidas, variando de 5 a 100 itens.

---

## 📁 Estrutura do Projeto

```
├── main.py                          # Ponto de entrada
├── requirements.txt                 # Dependências (python-docx)
├── data/
│   └── instances.py                 # 9 instâncias benchmark hardcoded
├── src/
│   ├── models/
│   │   ├── instance.py              # Dataclass KnapsackInstance
│   │   └── result.py                # Dataclass ExecutionResult
│   ├── algorithms/
│   │   ├── base.py                  # Classe abstrata BaseAlgorithm
│   │   ├── tabu_search.py           # Busca Tabu
│   │   └── genetic_algorithm.py     # Algoritmo Genético
│   ├── utils/
│   │   ├── repair.py                # Reparo de factibilidade
│   │   └── greedy.py                # Solução gulosa inicial
│   └── runners/
│       ├── experiment.py            # Orquestrador de experimentos
│       └── report.py                # Gerador de CSV e DOCX
├── resultados.csv                   # Planilha com todos os resultados
└── relatorio.docx                   # Relatório Word gerado
```

---

## 🧠 Algoritmos

### Busca Tabu

Meta-heurística de busca local com memória de curto prazo.

| Componente | Descrição |
|---|---|
| Solução inicial | Heurística gulosa por razão lucro/peso |
| Vizinhança | Flip de 1 bit (adicionar/remover item) |
| Lista Tabu | FIFO com tamanho fixo |
| Aspiração | Aceita movimento tabu se gera nova melhor global |
| Reparo | Remove itens de menor razão lucro/peso até factível |

**Parâmetros testados:**
- Tamanho da lista tabu: `5, 10, 20`
- Iterações máximas: `100, 500, 1000`

### Algoritmo Genético

Meta-heurística populacional inspirada na evolução biológica.

| Componente | Descrição |
|---|---|
| Representação | Vetor binário de tamanho N |
| Inicialização | População aleatória + 1 indivíduo guloso |
| Seleção | Torneio de tamanho 3 |
| Crossover | Um ponto (taxa 0.8) |
| Mutação | Bit-flip por bit |
| Elitismo | Preserva o melhor entre gerações |
| Reparo | Remove itens de menor razão lucro/peso até factível |

**Parâmetros testados:**
- População: `50, 100`
- Gerações: `100, 500, 1000`
- Taxa de mutação: `0.01, 0.05`

---

## 📊 Instâncias de Teste

| Instância | Itens | Capacidade | Ótimo | Fonte |
|-----------|-------|------------|-------|-------|
| P01 | 10 | 165 | 309 | [Burkardt (FSU)](https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html) |
| P02 | 5 | 26 | 51 | Burkardt |
| P03 | 6 | 190 | 150 | Burkardt |
| P04 | 7 | 50 | 107 | Burkardt |
| P05 | 8 | 104 | 900 | Burkardt |
| P06 | 7 | 170 | 1735 | Burkardt |
| P07 | 15 | 750 | 1458 | Burkardt |
| P08 | 24 | 6.404.180 | 13.549.094 | Burkardt |
| knapPI_1_100 | 100 | 995 | 9.147 | [Pisinger (GitHub)](https://github.com/dnlfm/knapsack-01-instances) |

---

## 🏆 Resultados

| Instância | Ótimo | Busca Tabu | Gap (%) | Alg. Genético | Gap (%) |
|-----------|-------|------------|---------|---------------|---------|
| P01 | 309 | 309 | **0.00** | 309 | **0.00** |
| P02 | 51 | 47 | 7.84 | 51 | **0.00** |
| P03 | 150 | 150 | **0.00** | 150 | **0.00** |
| P04 | 107 | 107 | **0.00** | 107 | **0.00** |
| P05 | 900 | 858 | 4.67 | 900 | **0.00** |
| P06 | 1.735 | 1.735 | **0.00** | 1.735 | **0.00** |
| P07 | 1.458 | 1.456 | 0.14 | 1.458 | **0.00** |
| P08 | 13.549.094 | 13.449.995 | 0.73 | 13.549.094 | **0.00** |
| knapPI_1_100 | 9.147 | 8.817 | 3.61 | 9.147 | **0.00** |

> ✅ O **Algoritmo Genético** encontrou a solução ótima em **todas as 9 instâncias**.
> A **Busca Tabu** atingiu o ótimo em **4 de 9**, com gap máximo de 7.84%.

---

## ⚙️ Como Executar

### Pré-requisitos

- Python 3.10+

### Instalação

```bash
git clone https://github.com/MayconCarpes/Mochila01.git
cd Mochila01
pip install -r requirements.txt
```

### Execução

```bash
python main.py
```

Gera automaticamente:
- `resultados.csv` — planilha com todos os resultados
- `relatorio.docx` — relatório Word com comparação

---

## 📈 Saídas

| Arquivo | Descrição |
|---------|-----------|
| `resultados.csv` | 189 linhas com todas as combinações (algoritmo × parâmetros × instância) |
| `relatorio.docx` | Relatório Word com introdução, descrição dos algoritmos, tabelas e conclusão |

O CSV contém as colunas:
`Instância`, `N_Itens`, `Algoritmo`, `Parâmetros`, `Melhor_Lucro`, `Ótimo_Conhecido`, `Gap(%)`, `Tempo_Médio(s)`, `Iterações/Gerações`

---

## 🔧 Tecnologias

- **Python 3** — linguagem principal
- **python-docx** — geração do relatório Word
- Sem frameworks de otimização — algoritmos implementados do zero

---

## 📝 Licença

Projeto acadêmico.
# Mochila01
