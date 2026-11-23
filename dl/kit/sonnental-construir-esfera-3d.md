# Como construir a esfera do símbolo Sonnental em 3D

Este guia descreve a geometria por completo, para quem precisar refazer a esfera em qualquer programa de 3D (Rhino, Blender, Fusion 360, SolidWorks, OpenSCAD) ou pedir a outra IA.

Arquivos deste kit:

- `construir_esfera_sonnental.py`: script que gera os STL das duas versões (Python 3, `pip install numpy manifold3d`).
- `esfera_2026_bordas.csv`: bordas da fenda da versão 2026, uma linha por grau.
- `esfera_2018_bordas.csv`: bordas da fenda da reconstrução do modelo original de 2018, uma linha por grau.

## 1. A ideia

A esfera é uma casca oca com um sol (uma esfera menor) no centro. Da casca foi retirada uma tira em espiral, como quem descasca uma maçã. O que sobra é uma fita única e contínua. Ela começa na calota de cima, dá voltas em torno do sol e termina na calota de baixo. As calotas são as duas pontas da fita, e não peças inteiras.

O símbolo é simétrico: girando 180 graus em torno do eixo que vai da frente para trás, ele fica igual. A calota de cima vira a de baixo.

## 2. Convenções

- O eixo z é vertical, para cima. A frente do símbolo é o lado voltado para quem olha. No Blender, a frente fica em −Y.
- θ (theta) é o ângulo em volta do eixo vertical, em graus. Vale 0 no meio da frente e cresce para a direita de quem olha: 90 é a lateral direita, 180 as costas, 270 a lateral esquerda. Como a espiral dá mais de uma volta, θ passa de 360. θ e θ+360 caem no mesmo meridiano, uma volta acima.
- φ (phi) é a latitude, em graus: 0 no equador, +90 no polo de cima, −90 no polo de baixo.
- Um ponto de raio r fica em: x = r·cos φ·sen θ, y = −r·cos φ·cos θ, z = r·sen φ.
- A fenda (a tira retirada) é descrita por duas curvas: a borda de baixo, φ_inf(θ), e a borda de cima, φ_sup(θ), para θ entre θ_ini e θ_fim. Em cada θ, tudo o que está na casca entre φ_inf e φ_sup é retirado.
- A borda de baixo da fenda é o topo da fita da volta de baixo. A borda de cima é a base da fita da volta de cima ou, na última volta, a borda da calota de cima.

## 3. Versão 2026 (oficial para qualquer réplica física)

### Medidas

| Item | Valor |
|---|---|
| Esfera | perfeita (redonda), raio externo R. Na bola impressa, R = 110 mm (22 cm de diâmetro) |
| Casca | espessura 4 mm em R = 110 (R/27,5) |
| Sol | esfera concêntrica de raio 0,66·R (72,6 mm, diâmetro 145 mm) |
| Fita | 37 graus de latitude de largura, constante em toda a volta |
| Fenda | 21 graus de latitude, constante, fechando em ponta viva nas duas calotas |
| Passo da espiral | 58 graus de latitude por volta: K = 58/360 = 0,16111 grau de latitude por grau de θ |
| Extensão da fenda | de θ_ini = −185 a θ_fim = 545 graus (2,03 voltas) |

### Fórmulas das bordas da fenda (em graus)

1. Base da fita da volta de cima, para θ ≤ 185: φ_sup(θ) = K·θ − 18,5
2. Topo da fita da volta de baixo, para θ ≥ 175: φ_inf(θ) = K·(θ − 360) + 18,5
3. Borda da calota de cima (borda de cima da fenda na última volta, θ > 185):
   - até θ_A = 389,655: φ_sup(θ) = K·(θ − 360) + 18,5 + 21 (fenda constante)
   - de θ_A até θ_B = 439,655: φ_sup(θ) = 48,306 − (K/100)·(θ_B − θ)² (a borda nivela suavemente, sem dobra)
   - de θ_B até 545: φ_sup(θ) = 48,306 (latitude constante)
   - em θ = 545 as duas bordas valem 48,306: a fenda fecha em ponta viva.
4. Metade de baixo, por simetria, para θ < 175: φ_inf(θ) = −φ_sup(360 − θ).

As fórmulas geram exatamente a tabela `esfera_2026_bordas.csv`.

### Peças e cores (impressão em 3 peças, cada uma de uma cor)

| Peça | Região | Cor |
|---|---|---|
| Cinza | só a faixa da frente: θ de −100 a +100, entre φ_sup(θ) e φ_inf(θ+360). Os dois cortes são planos verticais em θ = ±100, 10 graus atrás das laterais | cinza #99A7AA, de preferência translúcido (fumê), para o sol aparecer através dela |
| Azul | calota de cima e a volta da fita que passa por trás, em cima | azul #045AA0 |
| Verde | a volta de baixo que passa por trás e a calota de baixo | verde #BFBF32 |
| Sol | esfera de 0,66·R | amarelo-ouro (marca: #F7BF13) |

Conferência numérica com R = 110 mm: casca inteira 428,1 cm³; azul 163,1 cm³; cinza 102,0 cm³; verde 163,1 cm³.

## 4. Versão 2018 (reconstrução do modelo original do Lore)

- O arquivo original do Rhinoceros se perdeu. Esta versão foi reconstruída em novembro de 2026 a partir da única imagem que restou do modelo (vista de frente) e do desenho de 2018.
- A esfera é achatada: altura = 0,93 × largura.
- Sol de raio 0,615·R, mantido redondo (a imagem não permite saber se era achatado).
- A fenda vai de θ = −240 a 600 graus (2,33 voltas). As bordas não seguem uma fórmula simples: estão na tabela `esfera_2018_bordas.csv`, uma linha por grau, já antes do achatamento. Para montar, gere a casca redonda e depois escale só o eixo z por 0,93.
- A fita fica entre 31 e 33 graus, quase constante.
- As costas não aparecem na imagem. Foram deduzidas pela mesma simetria de 180 graus da frente.
- No Rhino, as cores eram provisórias: fita azul-esverdeada e sol laranja.

## 5. Passo a passo em qualquer programa

1. Crie uma esfera de raio R e subtraia uma esfera de raio R − espessura. Isso é a casca.
2. Para cada θ da tabela (de grau em grau, ou mais fino), calcule os dois pontos das bordas da fenda na superfície da esfera: (θ, φ_inf) e (θ, φ_sup). Ligue os pontos de baixo numa curva e os de cima noutra.
3. Monte o sólido de corte: para cada θ, um setor fino que vai de dentro da casca (0,45·R) até fora dela (1,5·R), entre as duas latitudes. Una os setores em sequência (loft ou sweep) e subtraia esse sólido da casca.
4. Coloque o sol, uma esfera de 0,66·R no centro (0,615·R na versão 2018).
5. Para as peças coloridas da versão 2026, corte a casca com o sólido da faixa da frente (θ de −100 a +100, entre φ_sup(θ) e φ_inf(θ+360)). O resto se separa em duas partes: a de cima é a azul e a de baixo é a verde.

Dicas por programa:

- Rhino e Grasshopper: gere os pontos pelas fórmulas ou pela tabela, faça Interpolate Curve nas duas bordas, projete na esfera e use Split na superfície. Depois dê espessura (OffsetSrf, sólido) para dentro.
- Blender: rode o script em Python ou importe os STL. Para editar, use um modificador Solidify com 4 mm para dentro.
- Fusion 360 e SolidWorks: importe os pontos (x, y, z) como spline 3D, crie a superfície de corte e use Split Body ou Combine (corte).
- OpenSCAD: monte o sólido de corte como polyhedron com os setores de cada θ e use difference().

## 6. Texto para pedir a outra IA

> Modele em 3D a esfera do símbolo da Sonnental. É uma casca esférica oca, raio externo R = 110 mm, espessura 4 mm, com uma esfera maciça concêntrica de raio 72,6 mm dentro (o sol). Da casca é retirada uma fenda em espiral, como a casca de uma maçã descascada, deixando uma fita única de 37 graus de latitude de largura, constante. A fenda tem 21 graus de latitude, constante. Use θ como azimute (0 na frente, que é −Y, crescendo para a direita de quem olha, passando de 360) e φ como latitude. A fenda vai de θ = −185 a 545 graus. Borda de cima da fenda: φ = 0,16111·θ − 18,5 para θ ≤ 185. Borda de baixo: φ = 0,16111·(θ − 360) + 18,5 para θ ≥ 175. Na última volta, a borda da calota de cima segue φ = 0,16111·(θ − 360) + 39,5 até θ = 389,655, depois φ = 48,306 − 0,0016111·(439,655 − θ)² até θ = 439,655, e fica em 48,306 até θ = 545, onde a fenda fecha em ponta. A metade de baixo é simétrica: φ_inf(θ) = −φ_sup(360 − θ) para θ < 175. Divida a casca em 3 peças: cinza é a faixa da frente entre θ = −100 e +100; o resto em cima é azul (#045AA0) e embaixo verde (#BFBF32). Volumes de conferência: casca 428,1 cm³, peças 163,1 / 102,0 / 163,1 cm³.


## Anexo: script construir_esfera_sonnental.py

Copie o bloco abaixo para um arquivo chamado `construir_esfera_sonnental.py` (ou baixe o .py na pasta Como construir, no Drive).

```python
"""
Constrói a esfera do símbolo Sonnental em 3D e salva os arquivos STL.

  python3 construir_esfera_sonnental.py 2026            # esfera oficial de 2026 (paramétrica)
  python3 construir_esfera_sonnental.py 2018            # reconstrução do modelo original de 2018 (lê a tabela CSV)
  python3 construir_esfera_sonnental.py 2026 --raio 110 # raio externo em mm (padrão 110)

Requisitos: Python 3.9+, numpy e manifold3d  (pip install numpy manifold3d)

Convenções: z para cima; a FRENTE do símbolo olha para -Y (vista frontal do Blender).
theta = ângulo em volta do eixo vertical, em graus: 0 na frente, positivo para a DIREITA de quem olha,
continuando por trás (pode passar de 360, porque a espiral dá mais de uma volta).
lat = latitude em graus (0 no equador, +90 no polo de cima).
Ponto da superfície: x = r cos(lat) sen(theta), y = -r cos(lat) cos(theta), z = r sen(lat).
"""
import sys, csv, os, struct
import numpy as np
from manifold3d import Manifold, Mesh, OpType

def parametros_2026():
    # fita de largura constante W, fenda de largura constante G; a espiral sobe W+G graus de latitude por volta
    W, G = 37.0, 21.0
    K = (W + G) / 360.0                  # graus de latitude por grau de theta
    DL = 50.0                            # trecho em que a borda da calota nivela (graus de theta)
    TS0 = 440.0 - DL
    E = round(TS0 + G / K + DL / 2)      # fim da fenda (ponta da calota de cima) = 545
    S = 360 - E                          # começo da fenda (ponta da calota de baixo) = -185
    TS = E - G / K - DL / 2              # onde a borda da calota começa a nivelar
    TF = TS + DL                         # daqui até E a borda fica em latitude constante
    LCAP = K * (E - 360) + W / 2         # latitude da borda nivelada da calota de cima (48,3 graus)
    th = np.arange(S, E + 1e-9, 0.25)
    P = np.full(th.shape, np.nan); Q = np.full(th.shape, np.nan)
    m = th >= 720 - E; Q[m] = K * (th[m] - 360) + W / 2            # borda de baixo da fenda = topo da fita da volta de baixo
    m = th <= E - 360; P[m] = K * th[m] - W / 2                    # borda de cima da fenda = base da fita da volta de cima
    m = th > E - 360; t = th[m]                                    # borda de cima da fenda na última volta = borda da calota
    P[m] = np.where(t <= TS, K * (t - 360) + W / 2 + G, np.where(t < TF, LCAP - (K / (2 * DL)) * (TF - t) ** 2, LCAP))
    m = th < 720 - E; Q[m] = -np.interp(360 - th[m], th, P)       # simetria: o símbolo gira 180 graus em torno do eixo frente-trás
    return dict(th=th, Q=Q, P=P, S=S, E=E, achatamento=1.0, raio_sol=0.66, corte_cor=100.0)

def parametros_2018(caminho):
    th, Q, P = [], [], []
    with open(caminho, newline='', encoding='utf-8') as f:
        for r in csv.DictReader(f):
            th.append(float(r['theta_graus'])); Q.append(float(r['fenda_borda_inferior_lat_graus'])); P.append(float(r['fenda_borda_superior_lat_graus']))
    th = np.array(th); return dict(th=th, Q=np.array(Q), P=np.array(P), S=th[0], E=th[-1], achatamento=0.93, raio_sol=0.615, corte_cor=None)

def cunha(th, lo, hi, R):
    """Sólido que corta a casca: para cada theta, um setor fino entre as latitudes lo e hi, do raio 0,45R ao 1,5R."""
    V = []
    for t, a, b in zip(np.radians(th), np.radians(lo), np.radians(hi)):
        d = np.array([np.sin(t), -np.cos(t), 0.0])
        for r, l in [(0.45, a), (1.5, a), (1.5, b), (0.45, b)]:
            l = np.clip(l, -np.pi / 2 + 1e-3, np.pi / 2 - 1e-3)
            V.append(R * r * (np.cos(l) * d + np.array([0, 0, np.sin(l)])))
    V = np.array(V, np.float32); N = len(th); F = []
    for i in range(N - 1):
        for j in range(4):
            a, b = 4 * i + j, 4 * i + (j + 1) % 4; c, e = 4 * (i + 1) + (j + 1) % 4, 4 * (i + 1) + j
            F += [[a, b, c], [a, c, e]]
    F += [[0, 2, 1], [0, 3, 2]]; e = 4 * (N - 1); F += [[e, e + 1, e + 2], [e, e + 2, e + 3]]
    F = np.array(F, np.uint32)
    m = Manifold(Mesh(vert_properties=V, tri_verts=F))
    if m.volume() <= 0: m = Manifold(Mesh(vert_properties=V, tri_verts=F[:, ::-1].copy()))
    return m

def salvar_stl(m, nome):
    mm = m.to_mesh(); v = mm.vert_properties[:, :3]; f = mm.tri_verts
    with open(nome, 'wb') as out:
        out.write(b'Sonnental'.ljust(80, b' ')); out.write(struct.pack('<I', len(f)))
        for a, b, c in f:
            p = v[[a, b, c]]; n = np.cross(p[1] - p[0], p[2] - p[0]); n = n / (np.linalg.norm(n) or 1)
            out.write(struct.pack('<12fH', *n, *p[0], *p[1], *p[2], 0))
    print('salvo', nome, '%.1f cm3' % (m.volume() / 1000))

def main():
    versao = sys.argv[1] if len(sys.argv) > 1 else '2026'
    R = float(sys.argv[sys.argv.index('--raio') + 1]) if '--raio' in sys.argv else 110.0
    T = 4.0 * R / 110.0                                   # espessura da casca: 4 mm numa esfera de 220 mm
    aqui = os.path.dirname(os.path.abspath(__file__))
    p = parametros_2026() if versao == '2026' else parametros_2018(os.path.join(aqui, 'esfera_2018_bordas.csv'))
    th = p['th']; lo, hi = p['Q'], np.maximum(p['P'], p['Q'] + 0.05)
    esfera = lambda r: Manifold.sphere(r, 512)
    casca = esfera(R) - esfera(R - T) - cunha(th, lo, hi, R)
    if p['achatamento'] != 1.0: casca = casca.scale([1, 1, p['achatamento']])
    salvar_stl(casca, f'esfera_{versao}_casca_inteira.stl')
    salvar_stl(esfera(p['raio_sol'] * R), f'esfera_{versao}_sol.stl')
    if p['corte_cor']:
        # peça cinza = só a faixa da frente, de -corte a +corte graus; o resto vira azul (em cima) e verde (embaixo)
        c = p['corte_cor']; t = np.arange(-c, c + 1e-9, 0.25)
        faixa = cunha(t, np.interp(t, th, p['P']), np.interp(t + 360, th, p['Q']), R)
        cinza = casca ^ faixa; resto = (casca - faixa).decompose()
        resto = [r for r in resto if r.volume() > 1]
        cima = [r for r in resto if sum(r.bounding_box()[2::3]) > 0]; baixo = [r for r in resto if sum(r.bounding_box()[2::3]) <= 0]
        juntar = lambda cs: Manifold.batch_boolean(cs, OpType.Add) if len(cs) > 1 else cs[0]
        salvar_stl(juntar(cima), f'esfera_{versao}_peca_azul.stl'); salvar_stl(cinza, f'esfera_{versao}_peca_cinza.stl'); salvar_stl(juntar(baixo), f'esfera_{versao}_peca_verde.stl')

if __name__ == '__main__':
    main()

```
