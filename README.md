## Alunos / Autores
* Acácio Ramos Salgueiro (1161161268)
* Myrelly Byanka Araújo De Oliveira (1172157763)

# Trabalho Prático 1
## Descrição
O trabalho prático consiste na implementação de um programa que permita cadastrar e testar autômatos finitos. A solução deve permitir que o usuário cadastre seu próprio autômato finito determinístico, não-determinístico ou não-determinístico com transições vazias, indicando os estados, as transições e valores do alfabeto. Após o cadastro deve ser possível testar se uma determinada palavra faz parte ou não da linguagem representada pelo autômato.

Caso cadastre um não-determinístico, deve-se aplicar a transformação para o determinístico e fazer o teste da palavra usando o autômato determinístico (neste caso, apresente o autômato determinístico antes de testar a palavra).

A leitura do autômato deve ser feita a partir de um arquivo texto contendo as informações. Vamos utilizar o mesmo padrão utilizado no site FSM Simulator. Utilizem o símbolo **$** como palavra vazia.

**Formato do arquivo de texto lido para construção do autômato**

```
#states
#initial
#accepting
#alphabet
#transitions
```

> Não é preciso criar a parte visual. Todo o código pode ser rodado e os resultados exibidos via linha de comando.

> Não devem ser utilizadas bibliotecas que implementem autômatos, os alunos devem implementar os próprios métodos de reconhecimento e transformação dos autômatos. O uso de bibliotecas podem ser usadas para a representação do autômato.

> Os alunos devem criar, até 7 dias após a liberação da atividade, um repositório no GitHub com um arquivo README contendo o nome dos componentes do grupo. O repositório deve ser privado e seguir as regras de criação descritas mais a frente neste documento. Esse README deve ser atualizado até a data da entrega com um breve manual de como rodar o código.

> **Atenção**
> * A atividade pode ser feita em grupos de até 3 pessoas.
> * Deve ser implementado, preferencialmente, nas linguagens: Python, Java ou C++. A implementação em outra linguagem deve ser discutida com o professor.
> * O código produzido deve ser versionado em um repositório do GitHub.
> * Junto com o código deve ter um arquivo README.md atualizado com as instruções de como o projeto deve ser testado (trabalhos que não apresentarem as instruções, serão desconsiderados).
> * O grupo deve garantir que o trabalhos será executado sem erros de compilação. Projetos com erro de compilação serão desconsiderados.

## Avaliação
Serão avaliados a corretude do algoritmo proposto, organização do código produzido e autoria do projeto. Ao longo da unidade, os grupos serão questionados sobre o andamento do trabalho. Essa avaliação pode influenciar a nota final. Cada trabalho será apresentado ao professor em aula específica conforme o cronograma da disciplina. Durante a apresentação, os alunos serão questionados à respeito do que foi produzido

A evolução do projeto no GitHub será acompanhanda ao longo da unidade. Todos os alunos envolvidos no projeto devem contribuir com a construção do código. Isso será acompanhado pelos commits realizados no repositório.

> A pontuação está descrita no memorial de avaliação

## Regras para criação do GitHub
* Um aluno do grupo cria o GitHub com o nome `lfa_trabalhopratico1_20212`.
* O repositório deve ser criado de forma privada.
* Os demais alunos do grupo devem ser adicionados como colaboradores.
* Adicionem o usuário adolfounit como colaborador do projeto.
* Após a entrega final, os alunos devem deixar o repositório como público e, se quiserem, podem alterar o nome do repositório.
## Entrega
Até a data prevista para entrega da atividade, o grupo pode atualizar o repositório cadastrado. Após a data da entrega não serão consideradas as alterações feitas. Até a data, os alunos devem marcar como concluída a tarefa correspondente no Classroom. Não serão aceitas entregas fora do prazo.

> Não serão aceitos projetos que não foram desenvolvidos pelo aluno ou pela dupla. Qualquer tipo de cópia será desconsiderada e os alunos envolvidos na cópia receberão nota 0 para toda atividade.
