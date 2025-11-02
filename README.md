# ramlib_algorithms_automatic_simulator
This is a simulator which helps you to analise each of the ramlib algorithms and make comparison of each's performances

# RandomLib - Biblioteca de Geração de Números Aleatórios

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)

Uma biblioteca avançada para geração de números pseudoaleatórios baseada em múltiplas fontes de tempo do sistema, com sistema automático de avaliação e análise estatística.

## Características Principais

- **Múltiplas Fontes de Entropia**: Utiliza milissegundos, microssegundos, nanossegundos e timestamp
- **Quatro Algoritmos Diferentes**: Implementa diversas abordagens para geração aleatória
- **Sistema de Avaliação Automática**: Simulador que executa N iterações e analisa resultados
- **Análise Estatística Completa**: Identifica padrões e distribuição dos números gerados
- **Classificação por Desempenho**: Sistema de scoring para avaliar qualidade da aleatoriedade
- **100% Independente**: Não depende de bibliotecas externas além do Python padrão

## Estrutura do Projeto
Algoritmos Implementados
New Algorithm
   
- Combina seed customizado com operações matemáticas

- Foco em distribuição uniforme

Random Algorithm
   
- Utiliza múltiplas fontes de tempo

- Operações bitwise para aumentar entropia

Last Algorithm
   
- Abordagem híbrida com cálculos complexos

- Balance entre performance e aleatoriedade

Original (randrange)
   
- Referência usando a biblioteca padrão do Python
  
- Para comparação e benchmarking


**Sistema de Avaliação**

O simulador automático inclui:

- Métricas Coletadas

- Frequência de repetição por número

- Porcentagem de distribuição

- Números mais e menos frequentes

- Análise de padrões temporais

**Sistema de Scoring*

# Classificação para números mais repetidos
- ≤ 11.0%  → 🟢 PERFEITO
- ≤ 13.0%  → 🟢 ÓTIMO  
- ≤ 14.5%  → 🟡 BOM
- < 17.5%  → 🟠 ACEITÁVEL
- ≥ 17.5%  → 🔴 NÃO ACEITÁVEL

# Classificação para números menos repetidos
- ≥ 9.0%   → 🟢 PERFEITO
- ≥ 8.0%   → 🟢 ÓTIMO
- **>** 7.0%   → 🟡 BOM
- ≥ 5.5%   → 🟠 ACEITÁVEL
- < 5.5%   → 🔴 NÃO ACEITÁVEL


 # Casos de Uso
Jogos e Simulações: Dados virtuais, sorteios, roleta

Testes e QA: Geração de dados de teste

Criptografia Educacional: Estudo de geração de seeds

Pesquisa Acadêmica: Análise de algoritmos pseudoaleatórios

Machine Learning: Inicialização de pesos neuronais




**Licença**

Este projeto está licenciado sob a Apache License 2.0 - veja o arquivo LICENSE para detalhes.

**Autor**

Sam Jamsh - Desenvolvedor e pesquisador em algoritmos

