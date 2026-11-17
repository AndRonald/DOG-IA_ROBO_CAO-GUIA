"""Verificações de segurança e navegação. Execute: python validar_dog_ia.py"""
import random
import unittest

import dog_ia_v2 as d


class TestesDogIA(unittest.TestCase):
    def test_ciclo_semaforico_e_tempo_minimo(self):
        sinal = d.Semaforo()
        for duracao, proxima in [(7, "AMARELO"), (2, "TODOS_VERM_1"),
                                 (1.5, "PEDESTRE"), (10, "TODOS_VERM_2"), (1.5, "VERDE")]:
            sinal.atualizar(duracao)
            self.assertEqual(sinal.fase, proxima)
        sinal.indice = 3
        sinal.tempo = 7.5
        self.assertTrue(sinal.pode_atravessar(156))
        sinal.tempo = 7.6
        self.assertFalse(sinal.pode_atravessar(156))

    def test_barreira_vermelho_e_fora_da_faixa(self):
        self.assertEqual(d.aplicar_barreira((625, 229), (625, 232), 20, False), (625, 229))
        self.assertEqual(d.aplicar_barreira((400, 229), (400, 232), 20, True), (400, 229))
        self.assertEqual(d.aplicar_barreira((625, 229), (625, 232), 20, True), (625, 232))
        self.assertEqual(d.aplicar_barreira((625, 300), (625, 303), 20, False), (625, 303))

    def test_carros_param_nos_dois_sentidos(self):
        sinal = d.Semaforo()
        sinal.indice = 3
        for sentido in (1, -1):
            carro = d.Veiculo(sentido, random.Random(5), 1)
            carro.infrator = False
            carro.x = 420 if sentido == 1 else 780
            for _ in range(300):
                carro.atualizar(1 / d.FPS, sinal, None)
            if sentido == 1:
                self.assertLessEqual(carro.rect.right, d.FAIXA_X - 18)
            else:
                self.assertGreaterEqual(carro.rect.left, d.FAIXA_X + d.FAIXA_LARGURA + 18)
            self.assertAlmostEqual(carro.velocidade, 0)

    def test_carro_parado_no_amarelo_nao_arranca(self):
        sinal = d.Semaforo()
        sinal.indice = 1
        carro = d.Veiculo(1, random.Random(5), 1)
        carro.infrator = False
        carro.x, carro.velocidade = 531, 0
        for _ in range(120):
            carro.atualizar(1 / d.FPS, sinal, None)
        self.assertEqual(carro.x, 531)

    def test_seguimento_e_infrator(self):
        sinal = d.Semaforo()
        sinal.indice = 3
        lider = d.Veiculo(1, random.Random(1), 1)
        lider.x, lider.velocidade = 531, 0
        seguidor = d.Veiculo(1, random.Random(2), 2)
        seguidor.x, seguidor.infrator = 380, True
        for _ in range(300):
            seguidor.atualizar(1 / d.FPS, sinal, lider)
        self.assertGreaterEqual(lider.rect.left - seguidor.rect.right, 23)
        infrator = d.Veiculo(1, random.Random(3), 3)
        infrator.x, infrator.infrator = 500, True
        for _ in range(120):
            infrator.atualizar(1 / d.FPS, sinal, None)
        self.assertGreater(infrator.x, d.FAIXA_X + d.FAIXA_LARGURA)

    def test_astar_escapa_do_obstaculo_em_u(self):
        obstaculos = [{"rect": d.pygame.Rect(*rect), "tipo": "solo"} for rect in
                      [(170, 70, 10, 110), (170, 70, 150, 10), (170, 170, 150, 10)]]
        plano = d.Planejador(obstaculos)
        caminho = plano.buscar((250, 125), (100, 125))
        self.assertTrue(caminho)
        self.assertGreaterEqual(max(x for x, _ in caminho), 350)
        self.assertEqual(plano.custo(plano.no((100, 125))), 0.45)

    def test_rota_urbana_usa_somente_a_faixa(self):
        plano = d.Planejador(d.criar_cenario())
        for _, ponto in d.DESTINOS.values():
            caminho = plano.buscar(d.DESTINOS[4][1], ponto)
            self.assertTrue(caminho)
            for x, y in caminho:
                self.assertTrue(plano.posicao_livre(x, y))
                if 230 < y < 440:
                    self.assertTrue(600 <= x <= 655)

    def test_mediana_rejeita_um_dropout_isolado(self):
        class SensorSemRuido:
            falha = False

            def random(self):
                return 0.01 if self.falha else 0.5

            def gauss(self, media, desvio):
                return 0

        rng = SensorSemRuido()
        robo = d.RoboCaoGuia(100, 125, rng)
        obstaculo = [{"rect": d.pygame.Rect(160, 120, 20, 10), "tipo": "solo"}]
        for _ in range(3):
            robo.ler_lidar(obstaculo)
        self.assertAlmostEqual(robo.leituras_lidar[9]["distancia"], 60)
        rng.falha = True
        robo.ler_lidar(obstaculo)
        self.assertAlmostEqual(robo.leituras_lidar[9]["distancia"], 60)
        self.assertEqual(robo.leituras_lidar[9]["tipo"], "solo")

    def test_freio_antecipa_infrator(self):
        robo = d.RoboCaoGuia(628, 292, random.Random(1))
        carro = d.Veiculo(1, random.Random(2), 1)
        carro.x, carro.velocidade, carro.infrator = 500, 150, True
        self.assertFalse(carro.rect.collidepoint(robo.x, robo.y))
        robo.decidir_navegacao((628, 543), 1 / d.FPS, d.Planejador([]), d.Semaforo(), [carro])
        self.assertEqual(robo.estado, "FREIO_EMERGENCIA")
        self.assertEqual((robo.x, robo.y), (628, 292))

    def test_arnes_reduz_velocidade(self):
        robo = d.RoboCaoGuia(100, 125)
        robo.tutor.x = 20
        robo.caminho = [(110, 125)]
        robo.decidir_navegacao((500, 125), 1 / d.FPS, d.Planejador([]), d.Semaforo(), [])
        self.assertGreater(robo.x, 100)
        self.assertLess(robo.x - 100, d.VELOCIDADE / d.FPS)

    def test_ida_e_volta_na_mesma_simulacao(self):
        sim = d.Simulacao(seed=7)
        for chave in (1, 4):
            nome, ponto = d.DESTINOS[chave]
            sim.selecionar_destino(ponto, nome)
            for _ in range(60 * d.FPS):
                sim.atualizar(1 / d.FPS)
                if sim.chegou:
                    break
            self.assertTrue(sim.chegou)
        self.assertEqual(sim.metricas["viagens_concluidas"], 2)
        self.assertEqual(sim.metricas["colisoes"], 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
