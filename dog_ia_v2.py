
    
  

                                                                  
def executar_benchmark(quantidade, seed, tempo_limite):
                                                                          
                                                                     
    rng = random.Random(seed)
    resultados = []
    ultimo_destino = DESTINOS[1]
    for i in range(quantidade):
        if i % 2 == 0:
            inicio = DESTINOS[4][1]
            ultimo_destino = DESTINOS[(i // 2) % 3 + 1]
            nome, ponto = ultimo_destino
        else:
            inicio = ultimo_destino[1]
            nome, ponto = DESTINOS[4]
        sim = Simulacao(inicio=inicio, rng=rng)
        sim.selecionar_destino(ponto, nome)
        for _ in range(math.ceil(tempo_limite * FPS)):
            sim.atualizar(1 / FPS)
            if sim.chegou or sim.robo.estado == "SEM_ROTA":
                break
        sucesso = sim.chegou and sim.metricas["colisoes"] == 0
        resultado = {"viagem": i + 1, "destino": nome, "sucesso": sucesso,
                     "chegou": sim.chegou, "estado_final": sim.robo.estado,
                     **{k: round(v, 3) if isinstance(v, float) else v for k, v in sim.metricas.items()},
                     "estados": sim.estados}
        resultados.append(resultado)
        print(f"Viagem {i + 1:02d} | {nome:8s} | {'OK' if sucesso else 'FALHA'} | "
              f"{sim.metricas['tempo']:.2f} s | colisões: {sim.metricas['colisoes']}")
    tempos = [r["tempo"] for r in resultados if r["sucesso"]]
    resumo = {"seed": seed, "viagens": quantidade, "sucessos": len(tempos),
              "taxa_sucesso": len(tempos) / quantidade,
              "tempo_medio_s": round(sum(tempos) / len(tempos), 3) if tempos else None,
              "colisoes": sum(r["colisoes"] for r in resultados),
              "quase_colisoes": sum(r["quase_colisoes"] for r in resultados),
              "freios_emergencia": sum(r["freios_emergencia"] for r in resultados)}
    print("\nResumo (sucesso = chegada sem colisão; tempo médio apenas dos sucessos):")
    print(json.dumps(resumo, indent=2, ensure_ascii=False))
    return {"resumo": resumo, "resultados": resultados}


def main():
    parser = argparse.ArgumentParser(description="Simulador assistivo DOG-IA V2")
    parser.add_argument("--benchmark", type=int, nargs="?", const=20, default=0, metavar="N")
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--tempo-limite", type=float, default=120.0, metavar="SEGUNDOS")
    parser.add_argument("--saida", help="Salva os resultados do benchmark em JSON")
    parser.add_argument("--sem-audio", action="store_true")
    args = parser.parse_args()
    if args.benchmark < 0 or not math.isfinite(args.tempo_limite) or args.tempo_limite <= 0:
        parser.error("A quantidade de viagens deve ser >= 0 e o tempo-limite deve ser positivo.")
    if args.benchmark:
                                                                                
        resultado = executar_benchmark(args.benchmark, args.seed, args.tempo_limite)
        if args.saida:
            with open(args.saida, "w", encoding="utf-8") as arquivo:
                json.dump(resultado, arquivo, indent=2, ensure_ascii=False)
        return

    pygame.display.init()
    pygame.font.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("DOG-IA V2 — Cão-Guia Autônomo")
    clock = pygame.time.Clock()
    fontes = (pygame.font.SysFont("arial", 19, bold=True), pygame.font.SysFont("arial", 14),
              pygame.font.SysFont("arial", 12, bold=True))
    sim = Simulacao(seed=args.seed, audio=not args.sem_audio)
    sim.selecionar_destino(DESTINOS[1][1], DESTINOS[1][0])
    rodando = True
    acumulador = 0.0
    try:
        while rodando:
                                                                                
                                                                              
            acumulador += min(clock.tick(FPS) / 1000.0, 0.25)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        rodando = False
                    elif evento.key == pygame.K_SPACE:
                        sim.modo_autonomo = not sim.modo_autonomo
                        if sim.modo_autonomo and sim.alvo:
                            sim.robo.planejar(sim.planejador, sim.alvo)
                    elif pygame.K_1 <= evento.key <= pygame.K_4:
                        nome, ponto = DESTINOS[evento.key - pygame.K_0]
                        sim.selecionar_destino(ponto, nome)
                    elif evento.key == pygame.K_r:
                        sim = Simulacao(seed=args.seed, audio=not args.sem_audio)
                        sim.selecionar_destino(DESTINOS[1][1], DESTINOS[1][0])
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = evento.pos
                    if mx >= 260:
                        mx -= 260
                        if evento.button == 1:
                            sim.selecionar_destino((mx, my), "Ponto escolhido")
                        elif evento.button == 3:
                            sim.adicionar_obstaculo(mx, my)
            teclas = pygame.key.get_pressed()
            comando = (int(teclas[pygame.K_RIGHT]) - int(teclas[pygame.K_LEFT]),
                       int(teclas[pygame.K_UP]))
            while acumulador >= 1 / FPS:
                sim.atualizar(1 / FPS, comando)
                acumulador -= 1 / FPS
            if not sim.robo.leituras_lidar:
                sim.robo.ler_lidar(sim.obstaculos)
            desenhar_simulacao(tela, sim, fontes)
            pygame.display.flip()
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
