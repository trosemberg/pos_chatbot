# Trabalho Pos Chat Bot

Alunos:

Pedro Caiafa Marques

Tomás Rosário Rosemberg

Para arvore de dialogo, criamos 7 nós para conseguirmos ter um dialogo fluido que entregue as respostas que queremos.

Para nosso Trabalho, criamos 5 Intents:
- O "Cancelar" para conseguirmos cancelar a operação após entrarmos no prompt para alimentar as variáveis.
- O "Diário" para lidar com dados de cotações de dolar em datas singulares.
- O "Período" para conseguiirmos pegar a variação da cotação de dolar dentro de um período.
- O "Saudação" para conseguirmos saudar o usuário do chatbot.
- O "Tchau" para nos despedirmos do usuário.

![Intents](./imagens/Intents.png)

![Arvore_de_Dialogo](./imagens/Arvore_de_Dialogo.png)

- Temos o nó de Boas vindas, com mensagem de boas vindas, indicando as funcionalidades do chatbot. (Este nó não é acionando durante o dialogo inicial do facebook messenger) 

![Bem_Vindo](./imagens/Bem_Vindo.png)

- Por dia é o nó responsavel por lidar com dialogo sobre cotação do dolar em uma data especifica. Nele configuramos o prompt para obtenção de uma variável (data) e um handler para lidar caso queria cancelar antes de inserir esse dado. Com essa variável data, acionamos nossa cloud function via web hook para que possamos fazer uma request e pegarmos a cotação do dolar naquela data.

![Por_Dia](./imagens/Por_Dia.png)

- Período é o nó responsável por charmar o webhook passando duas datas, para assim responder qual a variação do dólar entre essas duas datas e o seu valor em ambas as datas.

![Periodo](./imagens/Periodo.png)

- Nó para indicarmos continuidade na conversa, reapresentando as opções de uso do chatbot. 

![Pos_Resposta](./imagens/Pos_Resposta.png)

- Nó para o chat bot ser capaz de se despedir do usuário.

![Tchau](./imagens/Tchau.png)

- Nó de Saudação ao usuário

![Saudacao](./imagens/Saudacao.png)

- Nó para caso não previsto.

![Em_Outros_Casos](./imagens/Em_Outros_Casos.png)
