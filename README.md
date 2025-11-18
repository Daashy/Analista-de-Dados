# Meu Primeiro Projeto em Power BI: Da Planilha Bruta ao Dashboard Profissional  

Nos últimos dias desenvolvi um projeto completo de análise: transformar uma planilha simples do Excel em um dashboard de vendas totalmente funcional no Power BI. O objetivo principal foi estruturar um fluxo completo — da ingestão dos dados até a visualização final — seguindo boas práticas técnicas.  
  
## Passo 1 — Ingestão dos Dados  

Os dados foram importados diretamente do Excel por meio da opção Obter Dados > Pasta de Trabalho.  
Nesse processo, o Power BI carregou as tabelas Vendas e Lojas para o ambiente de análise, permitindo iniciar o trabalho de preparação e limpeza.
  
## Passo 2 — Tratamento e Transformações no Power Query  
  
Ao entrar no Editor do Power Query, os dados apresentavam problemas comuns encontrados em fontes operacionais:  
  
*- Erros de digitação*  
*- Colunas inconsistentes*  
*- Tipos de dados incorretos*  
*- Informações unificadas em um único campo*  

**As principais transformações aplicadas foram:**    
  
*- Substituir Valores para correção de entradas incorretas*  
*- Colocar Cada Palavra em Maiúscula para padronização de atributos textuais*  
*- Dividir Coluna por Delimitador para separar quantidade e preço unitário*  
*- Alterar Tipo de Dados para garantir leitura correta dos campos*  
*- Adicionar Coluna Personalizada para calcular Valor Venda (Quantidade × Preço Unitário)*  
  
Ao final, os dados foram estruturados de forma consistente e preparados para a modelagem.  
  
## Passo 3 — Modelagem de Dados  
  
Na Exibição de Modelo, foi criado o relacionamento entre Vendas e Lojas utilizando o campo Código da Loja.
Esse relacionamento possibilitou análises integradas, com contexto correto entre transações e suas respectivas lojas.
  
## Passo 4 — Construção de Medidas em DAX  
  
Com a base modelada, foram utilizadas inicialmente medidas implícitas fornecidas pelo próprio Power BI (como soma e contagem).
Em seguida, foi criada uma medida explícita para cálculo de comissão:  
  
*Comissão = SUM(Vendas[Valor Venda]) * 0.05*  
A medida se mantém totalmente dinâmica, adaptando-se a qualquer filtro aplicado no relatório.  
  
## Passo 5 — Desenvolvimento dos Visuais  
  
A etapa de visualização considerou clareza, hierarquia e facilidade de leitura.  
**Foram utilizados:**  
*- Cartões para KPIs principais*  
*- Gráfico de Colunas Clusterizado para análise mensal e por loja*  
*- Gráfico de Rosca para proporção por meio de pagamento*  
*- Tabelas com formatação condicional para representar variações e valores comparativos*  
*- Também foram ajustadas as Interações entre Visuais, garantindo respostas adequadas de filtros e segmentações.*  
  
## Passo 6 — Finalização e Design  
  
Para reforçar identidade visual, foi aplicado um template criado no PowerPoint, seguido da padronização de cores e ajustes com o Pincel de Formatação.  
Ícones, formas e organização de layout foram refinados para entregar uma experiência visual limpa e eficiente.  
  
# Conclusão  
  
O projeto demonstra o fluxo completo de construção de um dashboard no Power BI, passando por ingestão, transformação, modelagem, criação de medidas e montagem visual. O resultado final é um dashboard interativo, funcional e com estrutura adequada para análises futuras.  
  
*Caso queira visualizar o projeto ou discutir melhorias e práticas relacionadas ao Power BI, estou disponível para troca de ideias.*
