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
