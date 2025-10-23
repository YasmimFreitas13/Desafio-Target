# 💻 Desafios Técnicos de Estágio - Target Sistemas

Olá! Meu nome é Yasmim e este repositório é a minha solução para os desafios técnicos propostos no processo seletivo de estágio da Target Sistemas.

Desenvolver estas soluções foi uma excelente oportunidade para aplicar e reforçar conceitos de lógica e eficiência em Python.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem de Programação:** Python 3.x
* **Bibliotecas Nativas:** `json`
* **Controle de Versão:** Git e GitHub

## 🚀 Como Executar

Para rodar os desafios, clone o repositório, navegue até a pasta do desafio desejado (`cd Desafio_X`) e execute: `python <nome_do_arquivo>.py`.

---

## 📝 Detalhamento e Justificativas Técnicas

Abaixo, detalho cada desafio, destacando a lógica central e as decisões técnicas tomadas:

### Desafio 1: Lógica de Soma
**Lógica:** O código replica a lógica do pseudocódigo, garantindo que o incremento de `K` ocorra antes da soma. O resultado final é a soma de 1 a 13.

### Desafio 2: Sequência de Fibonacci
**Decisão Técnica (Eficiência):** A abordagem principal foi focar na **eficiência de memória**. Em vez de gerar e armazenar toda a sequência em uma lista, o código gera os números dinamicamente (`a, b = b, a + b`), parando assim que atinge ou ultrapassa o número informado. Isso é ideal para verificar números muito grandes.

### Desafio 3: Estatísticas de Faturamento Diário
**Decisão Técnica (Processamento de Dados):** Optei por utilizar o arquivo **JSON** pela facilidade de manipulação em Python. O ponto crucial foi a manipulação da média: utilizei *list comprehension* para criar uma lista com **apenas os faturamentos maiores que zero**, garantindo que a média fosse calculada conforme o requisito.

### Desafio 4: Percentual de Representação por Estado
**Decisão Técnica (Estrutura de Dados):** Utilizei um dicionário Python para mapear o estado ao seu faturamento. Isso permitiu calcular o total facilmente (`sum(.values())`) e iterar de forma limpa para aplicar a fórmula do percentual para cada estado.

### Desafio 5: Inversão de String
**Decisão Técnica (Restrição):** Respeitando a restrição de não usar funções prontas (`reverse()` ou `[::-1]`), a solução utiliza um laço `for` com `range(start, stop, step)` para percorrer a *string* **do último índice até o primeiro**, construindo manualmente a string invertida através da concatenação.

---

## 💡 Próximos Passos

Agradeço a oportunidade de resolver esses desafios. Estou animado(a) com a possibilidade de aplicar estas e outras habilidades no ambiente de desenvolvimento da Target Sistemas!

Yasmim Freitas 🧡