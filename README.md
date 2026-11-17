DOG-IA_ROBO_CAO-GUIA
DOG-IA V2 — AC-4

# Integrantes

| R.A. | Nome |
|---|---|
| 100954 | Pedro Augusto Brito Castilho Pereira |
| 99242 | Gustavo Mattos da Silva |
| 102648 | Ronald Araujo Viana |

O arquivo principal do projeto é o dog_ia_v2.py. Ele preserva os recursos gráficos presentes no código original e incorpora as novas melhorias por meio de classes simples, com explicações e comentários em português.

Como executar o programa

Nesta pasta, o ambiente já está configurado com Python 3.12 e Pygame 2.6.1.

Para iniciar o programa, execute:

powershell
.\.venv\Scripts\python.exe .\dog_ia_v2.py


Caso utilize outro computador com Python instalado, primeiro instale as dependências:

powershell
python -m pip install -r requirements.txt
python dog_ia_v2.py


Ao iniciar, o sistema direciona o robô ao Mercado. Os comandos disponíveis são:

1 — Ir ao Mercado.
2 — Ir à Farmácia.
3 — Ir à Padaria.
4 — Ir para Casa após realizar uma viagem.
Espaço — Alternar entre o controle manual e o modo IA.
Seta esquerda/direita — Girar o robô.
Seta para cima — Movimentar para frente.
Clique esquerdo — Selecionar um destino sem obstáculos.
Clique direito — Adicionar um obstáculo ao cenário.
R — Reiniciar a simulação.
Esc — Encerrar o programa.

O modo manual também possui mecanismos de proteção, respeitando a barreira de segurança e o sistema de frenagem de emergência.

Para executar sem efeitos sonoros, utilize o argumento --sem-audio.

Funcionalidades desenvolvidas
Sistema de semáforo: possui cinco etapas de sinalização, com passagem do tempo simulada e circulação de veículos nos dois sentidos. Os veículos apresentam aceleração, desaceleração, controle de distância e uma taxa de 12% de desrespeito ao sinal.
Proteção na travessia: existe uma barreira na calçada que protege o robô e seu tutor. A travessia somente é iniciada quando o semáforo permite, existe tempo suficiente para atravessar e a pista está livre.
Planejamento de caminhos: utiliza o algoritmo A* em uma grade de 10 pixels, com heurística octile. Também aplica margens de segurança de 30, 22 e 38 pixels, considera um custo de 0,45 no piso tátil e recalcula o percurso quando o robô permanece 3,5 segundos sem avançar.
Sensor LiDAR: realiza medições utilizando Rect.clipline, com ruído gaussiano de 1,5 pixel, possibilidade de falha de leitura de 2% e aplicação de uma mediana temporal com três medições por raio.
Prevenção de acidentes: calcula a posição futura dos veículos considerando um intervalo de um segundo, permitindo acionar a frenagem de emergência antes de uma possível colisão.
Acompanhamento pelo tutor: o tutor possui um sistema de movimentação independente, seguindo o caminho percorrido pelo robô.
Controle pela guia: a velocidade é reduzida de acordo com a tensão exercida na guia.
Alertas sonoros: foram adicionados avisos sintéticos com reprodução em estéreo.
Telemetria e testes de desempenho: permitem coletar informações e executar benchmarks sem abrir uma janela gráfica ou inicializar os sistemas de vídeo e áudio.

Além disso, o toldo localizado na parte inferior do cenário teve sua posição alterada de x=520 para x=470. Essa mudança permite liberar a saída da faixa depois da aplicação das margens de segurança dos obstáculos suspensos.

Testes e avaliação de desempenho

Para avaliar o funcionamento do sistema, foram utilizados os seguintes comandos:

powershell
.\.venv\Scripts\python.exe dog_ia_v2.py --benchmark 20 --seed 1 --saida benchmark_seed_1.json

.\.venv\Scripts\python.exe dog_ia_v2.py --benchmark 20 --seed 7 --saida benchmark_seed_7.json

.\.venv\Scripts\python.exe validar_dog_ia.py

Resultados alcançados

Os testes realizados apresentaram os seguintes resultados:

Seed	Viagens	Sucesso	Tempo médio	Colisões	Quase-colisões	Freios
1	20	100%	13,530 s	0	0	1
7	20	100%	13,470 s	0	0	0

O benchmark realiza viagens alternadas entre o Mercado, a Farmácia e a Padaria, incluindo o retorno para Casa.

Cada deslocamento é iniciado em uma nova simulação, mantendo a sequência de eventos aleatórios durante todo o experimento.

O tempo máximo permitido para cada viagem é de 120 segundos simulados, podendo ser modificado pelo parâmetro --tempo-limite.

Uma viagem é considerada bem-sucedida quando o destino é alcançado sem ocorrer colisão. O cálculo do tempo médio considera somente as viagens concluídas com sucesso.

Uma quase-colisão é registrada quando a distância entre o robô e um obstáculo fica abaixo de 12 pixels, mesmo sem acontecer contato físico.

Os registros de colisões e aproximações são contabilizados por ocorrência envolvendo cada entidade e obstáculo, evitando que vários quadros de um mesmo episódio sejam contabilizados separadamente.

Validações realizadas

Foram implementadas 11 verificações para avaliar diferentes aspectos do funcionamento do sistema:

Funcionamento correto do semáforo.
Atuação da barreira de proteção.
Frenagem de veículos nos dois sentidos.
Sistema de acompanhamento e distância entre veículos.
Comportamento dos veículos que desrespeitam o sinal.
Capacidade de sair de um obstáculo em formato de U.
Utilização adequada da faixa de pedestres.
Funcionamento do filtro de leituras dos sensores.
Atuação do sistema de frenagem preventiva.
Influência da tensão da guia sobre a velocidade.
Realização de viagens de ida e volta na mesma simulação.

Também foi produzida uma imagem para conferência visual do cenário, disponível no arquivo preview_dog_ia.png.

Considerações finais

Os resultados demonstram que, nos cenários didáticos utilizados nos experimentos, o sistema conseguiu concluir todas as viagens testadas, sem registrar colisões ou quase-colisões.

Entretanto, esses resultados representam apenas as condições específicas avaliadas e não significam que o sistema esteja livre de riscos em todas as situações possíveis.
