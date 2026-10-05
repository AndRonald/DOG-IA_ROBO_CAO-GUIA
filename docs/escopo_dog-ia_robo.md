Projeto AC-3 e AC-4: Robô Guia Assistivo

Foco: Mobilidade Urbana para Pessoas com Deficiência Visual
Entregas: Avaliações Continuadas AC-3 (Fase 1) e AC-4 (Fase 2)

Mudança importante: Nesta etapa, os alunos deverão atuar em grupos, e não mais em duplas.

1. Contexto e Apelo Social

Muitas pessoas com deficiência visual enfrentam diariamente barreiras críticas de mobilidade. A solução tradicional mais eficiente, o cão-guia, é extremamente cara, leva até dois anos para ser treinada e possui uma fila de espera que pode durar anos no Brasil.

Além disso, situações presentes no ambiente urbano tornam a locomoção ainda mais difícil e perigosa, como:

Calçadas esburacadas;

Orelhões e outros obstáculos;

Galhos de árvores, que podem estar acima do alcance de bengalas tradicionais;

Travessias de pedestres sem sinalização sonora;

Obstáculos suspensos ou aéreos;

Falta de sinalização adequada para pessoas com deficiência visual.

Esses fatores transformam trajetos simples em tarefas de alto risco.

O Desafio

Como cientistas da computação, o objetivo é desenvolver o protótipo de um Robô Guia Autônomo em um ambiente simulado.

O robô deverá atuar à frente do usuário, auxiliando na locomoção de forma autônoma e segura.

Objetivos do Robô

O sistema deverá ser capaz de:

Navegar e mapear a cidade/calçadas de forma autônoma e segura;

Detectar obstáculos em 3D, especialmente:

Obstáculos aéreos ou suspensos;

Buracos;

Reconhecer sinalizações urbanas utilizando Visão Computacional, incluindo:

Faixas de pedestres;

Status dos semáforos;

Emitir alertas de voz ou som para orientar o usuário em tempo real sobre o percurso.

2. Entregáveis Obrigatórios

Ao final do projeto, cada grupo deverá entregar os seguintes artefatos:

2.1 Arquitetura do Sistema

Deverá conter diagramas completos representando:

Nós do ROS 2;

Tópicos;

Serviços;

Ações;

Árvore de transformações (TF2).

2.2 Artefatos Técnicos — Código-Fonte

O repositório Git deverá conter:

Pacotes ROS 2 em Python;

Modelos URDF/Xacro;

Arquivos .launch.py;

Configurações do Nav2;

Demais arquivos necessários para execução do projeto.

2.3 Documentação e Relatório Técnico

O relatório deverá apresentar detalhadamente:

Descrição da solução;

Metodologia utilizada;

Experimentos realizados;

Resultados obtidos;

Análise dos resultados.

2.4 Vídeo de Demonstração

Deverá ser produzido um vídeo de até 3 minutos, mostrando o robô cumprindo as missões no simulador de forma 100% autônoma.

2.5 Apresentação em Sala

Cada grupo terá até 10 minutos para apresentar o projeto.

3. Cronograma e Avaliação

O projeto será dividido em duas fases:

AC-3 — Fase 1: 1,0 ponto;

AC-4 — Fase 2: 1,0 ponto.

As tarefas serão liberadas aula a aula, seguindo uma metodologia incremental.

Cronograma Geral
Fase	Data	Atividade	Pontuação
AC-3 — Fase 1	05/10	Setup de Ambiente, WSL2/Linux, ROS 2 e Docker	0,25
AC-3 — Fase 1	26/10	Modelagem URDF/Xacro do Robô e Sensores 3D	0,25
AC-3 — Fase 1	09/11	Mapeamento SLAM 2D e Navegação com Nav2	0,50
AC-4 — Fase 2	16/11	Visão Computacional — Semáforos / Faixas	0,25
AC-4 — Fase 2	23/11	Integração de Áudio e Testes de Campo	0,25
AC-4 — Fase 2	30/11	Apresentação Final e Fechamento do Projeto	0,50

Valor total do projeto: 2,0 pontos

4. FASE 1 — Infraestrutura, Modelagem e Navegação

AC-3 — Valor: 1,0 ponto

Aula 05/10 — Preparação e Setup do Ambiente
Objetivo

Garantir que 100% dos integrantes do grupo estejam com a infraestrutura de desenvolvimento pronta.

Tarefas do Grupo

Configurar o ambiente utilizando:

Ubuntu 22.04; ou

WSL2 no Windows.

Validar a instalação de:

ROS 2 Humble / Jazzy;

Gazebo;

RViz2.

Garantir suporte a GPU/WSLg quando aplicável.

Criar o repositório Git do grupo.

Criar o workspace do ROS 2:

ros2_ws/

Check de Validação — 0,25 ponto

Cada integrante deverá executar o Gazebo utilizando o comando de teste gráfico no terminal.

Critério: todos os integrantes devem possuir o ambiente funcionando corretamente.

Aula 26/10 — Modelagem do Robô Guia e Sensores
Objetivo

Criar a estrutura física simulada do robô assistivo.

Tarefas do Grupo

Desenvolver o modelo Xacro/URDF do robô, contendo:

Rodas motrizes;

Roda boba;

Câmera RGB-D;

LiDAR 2D.

Sensores

A Câmera RGB-D deverá:

Fornecer visão 3D;

Ser posicionada de forma inclinada;

Auxiliar na detecção de obstáculos suspensos.

O LiDAR 2D deverá:

Ser instalado no chassi;

Auxiliar na percepção do ambiente;

Fornecer dados para navegação.

Configuração do Gazebo

Configurar os plugins necessários para:

Controle diferencial;

Publicação de odometria;

Publicação dos dados dos sensores.

Check de Validação — 0,25 ponto

O robô deverá:

Carregar corretamente no Gazebo;

Responder aos comandos de teleoperação através de:

/cmd_vel


Publicar as transformações TF;

Não apresentar erros no RViz2.

Aula 09/11 — Mapeamento Autônomo e Navegação
Objetivo

Permitir que o robô navegue de forma autônoma pelo ambiente urbano simulado.

Tarefas do Grupo
1. Mapeamento

Utilizar o SLAM Toolbox para mapear o ambiente urbano no Gazebo.

2. Navegação

Configurar a stack do Nav2, incluindo:

Costmap local;

Costmap global;

Planejadores de trajetória;

Parâmetros necessários para navegação autônoma.

3. Distância de Segurança

Configurar o Raio de Inflação do Costmap para garantir uma distância segura entre o robô e os obstáculos.

Check de Validação — 0,50 ponto

O grupo deverá entregar:

Primeira versão da documentação;

Robô navegando de forma autônoma;

Navegação até um ponto estipulado através do RViz2.

5. FASE 2 — Inteligência, Percepção e Apresentação

AC-4 — Valor: 1,0 ponto

Aula 16/11 — Visão Computacional Aplicada
Objetivo

Dar "olhos inteligentes" ao robô assistivo.

Tarefas do Grupo

Criar um nó em Python integrando:

ROS 2;

OpenCV;

cv_bridge.

O nó deverá processar as imagens da câmera para realizar uma das seguintes tarefas:

Detectar a cor do semáforo:

🟢 Verde;

🔴 Vermelho.

Identificar uma faixa de pedestres no chão.

Lógica de Segurança

O sistema deverá possuir uma lógica que impeça o robô de atravessar a rua quando o sinal estiver vermelho.

Check de Validação — 0,25 ponto

O robô deverá:

Detectar o sinal vermelho através da imagem simulada;

Interromper sua trajetória;

Permanecer aguardando enquanto o sinal estiver vermelho.

Aula 23/11 — Interação Humano-Robô (HRI) e Polimento
Objetivo

Traduzir as informações obtidas pelos sensores e pelo sistema de navegação para o usuário com deficiência visual.

Tarefas do Grupo
1. Sistema de Áudio

Criar um nó de áudio utilizando bibliotecas de Text-to-Speech (TTS) em Python.

O sistema deverá emitir orientações como:

"Sinal vermelho, aguarde na calçada."

"Em frente em 5 metros."

"Obstáculo suspenso detectado."

2. Testes de Estresse

Realizar testes para avaliar:

Robustez;

Funcionamento da navegação;

Detecção de obstáculos;

Detecção de semáforos;

Emissão dos alertas;

Integração entre os diferentes componentes.

Após os testes, realizar os ajustes necessários no código.

3. Vídeo de Demonstração

Gravar um vídeo de demonstração com duração de 2 a 3 minutos, apresentando o funcionamento do robô.

4. Relatório Técnico

Finalizar o relatório técnico contendo a documentação e os resultados obtidos durante o projeto.

Check de Validação — 0,25 ponto

Entregar no repositório:

Vídeo de demonstração;

Relatório técnico.

6. Aula 30/11 — Apresentação Final dos Protótipos
Objetivo

Realizar a demonstração final do projeto para a turma.

Tarefas do Grupo

Executar a simulação ao vivo utilizando:

Gazebo;

RViz2.

Durante a apresentação, o robô deverá completar a missão de guiamento do início ao fim, demonstrando as funcionalidades desenvolvidas pelo grupo.

Check de Validação — 0,50 ponto

O grupo deverá realizar:

Apresentação do projeto;

Demonstração do protótipo;

Entrega final dos 4 artefatos completos.

7. Artefatos Finais

Ao final do projeto, o repositório deverá conter os seguintes itens:

#	Artefato	Descrição
1	Código-Fonte	Pacotes ROS 2, Python, URDF/Xacro, Launch Files e configurações
2	Arquitetura	Diagramas de nós, tópicos, serviços, ações e TF2
3	Relatório Técnico	Solução, metodologia, experimentos e análise dos resultados
4	Vídeo	Demonstração do robô funcionando de forma autônoma
8. Resumo da Avaliação
AC-3 — Fase 1

Valor total: 1,0 ponto

Etapa	Pontos
Setup do ambiente	0,25
Modelagem URDF/Xacro e sensores	0,25
SLAM e Navegação com Nav2	0,50
Total	1,00
AC-4 — Fase 2

Valor total: 1,0 ponto

Etapa	Pontos
Visão Computacional	0,25
Integração de Áudio e Testes	0,25
Apresentação Final	0,50
Total	1,00
9. Resultado Esperado

Ao final das duas fases, o grupo deverá apresentar um Robô Guia Assistivo Autônomo, capaz de:

                 ┌──────────────────────┐
                 │    ROBÔ GUIA         │
                 │      ASSISTIVO       │
                 └──────────┬───────────┘
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ▼                 ▼                 ▼
      Navegação         Percepção          Interação
          │                 │                 │
          ▼                 ▼                 ▼
       SLAM /             LiDAR /          Áudio / TTS
        Nav2             RGB-D / OpenCV
          │                 │                 │
          └─────────────────┼─────────────────┘
                            │
                            ▼
                  Navegação Autônoma
                     e Segura


O sistema deverá integrar navegação, percepção, visão computacional e interação por áudio, permitindo que o robô auxilie uma pessoa com deficiência visual durante um trajeto em um ambiente urbano simulado.
