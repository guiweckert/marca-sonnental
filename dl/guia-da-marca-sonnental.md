# Guia da marca Sonnental

Este é o guia da marca da Sonnental Energia, consolidado em novembro de 2026 a partir do estudo de 2018, da revisão e do Manual de Identidade Visual de 2019, do redesenho de 2025 e da esfera 3D de 2026. Quando um documento antigo disser algo diferente, vale o que está aqui.

Este guia serve para quem trabalha com a marca e para qualquer IA (ChatGPT, Gemini, Claude ou outra): anexe este arquivo à conversa e peça para seguir as regras daqui.

## Resumo em 30 segundos

- Sonnental vem do alemão e quer dizer "vale do sol". O símbolo é um sol envolvido por uma fita em espiral, em três cores.
- **Logo em uso: a versão 2D de 2025.** A principal é a com volume e degradê, sobre fundo branco.
- **Réplica física (impressão 3D, escultura, fachada): a esfera de 2026**, perfeita, com a fita na mesma largura em toda a volta. Ela não é usada como logo plano.
- **Nunca redesenhar, recolorir, distorcer ou "reconstruir" o logo.** Sempre usar os arquivos oficiais.
- Quatro cores do manual: azul `#045AA0`, amarelo `#F7BF13`, cinza `#99A7AA`, verde `#BFBF32`.

## Onde estão os arquivos oficiais

Página da marca, com a esfera em 3D, a história e todos os arquivos para baixar: https://guiweckert.github.io/marca-sonnental/

Os mesmos arquivos ficam no Google Drive da Sonnental: **6. Comunicacao › Marca Sonnental (arquivos oficiais)**

Subpastas: **1. Marca 2D (versão 2025)** com SVG, PNG e PDF; **2. Esfera 3D (versão 2026)** com Imagens, Modelo 3D, Impressão 3D e Como construir.

### Os 14 arquivos 2D

Cada um existe em `.svg`, `.png` (fundo transparente, 3000 px de largura na marca e 2000 px no símbolo) e `.pdf`, com o mesmo nome:

| Arquivo | Quando usar |
|---|---|
| `sonnental-marca-degrade` | **Principal.** Telas e impressos sobre fundo branco. Padrão para documentos, propostas, relatórios, slides |
| `sonnental-simbolo-degrade` | Símbolo sozinho, principal. Ícone, avatar, favicon, quando o nome já aparece perto |
| `sonnental-marca-chapada` / `sonnental-simbolo-chapado` | Sem degradê: sobre fotos, estampa, adesivo, bordado colorido |
| `sonnental-marca-branca` | Branca preenchida: sobre fundo escuro ou foto |
| `sonnental-marca-branca-contorno` / `sonnental-simbolo-branco-contorno` | Branca em contorno: sobre o azul, o cinza ou o verde da marca |
| `sonnental-simbolo-branco` | Símbolo branco preenchido: fundos escuros |
| `sonnental-marca-preta` / `sonnental-simbolo-preto` | Uma tinta: carimbo, gravação a laser, fax, impressão monocromática |
| `sonnental-marca-preta-contorno` / `sonnental-simbolo-preto-contorno` | Uma tinta em traço: gravação fina, bordado de linha |
| `sonnental-simbolo-cinza` / `sonnental-simbolo-cinza-contorno` | Marca d'água, aplicação discreta |

Regra prática para documentos: PNG de `sonnental-marca-degrade`, recortado pelo canal alfa (o PNG vem com margem transparente), e composto sobre branco antes de entrar no PDF. Em cabeçalho com faixa colorida da marca, `sonnental-marca-branca-contorno`. Para impressão profissional, mande o SVG ou o PDF.

### Arquivos 3D (esfera de 2026)

- **Imagens** (PNG sem fundo): `sonnental-esfera-2026-frente`, `sonnental-esfera-2026-tres-quartos`, `sonnental-marca-completa-3d` (esfera com o letreiro em volume).
- **Modelo 3D** (limpo, sem furos nem encaixes, para visualizar, renderizar e apresentar): `sonnental-esfera-2026.glb` (com cores; abre no Visualizador 3D do Windows, no PowerPoint e no Blender), `.blend` e as 4 partes em STL. 220 mm de diâmetro.
- **Impressão 3D**: peças preparadas para imprimir (casca em 3 cores, sol oco para LED ou maciço, base com gabarito, letreiro e pedestal). Os furos e pinos de gabarito existem **só** nesses arquivos; nunca usar essas peças em imagem, render ou apresentação.
- **Como construir**: guia completo, script Python (`construir_esfera_sonnental.py 2026|2018`) e as tabelas das bordas da fenda (CSV, uma linha por grau).

## Cores

As quatro cores do manual de 2019, com o significado do estudo de 2018:

| Cor | Hex | Significado |
|---|---|---|
| Azul | `#045AA0` | Tecnologia. O mar |
| Amarelo | `#F7BF13` | O núcleo: o sol e todas as energias da Terra, em movimento |
| Cinza | `#99A7AA` | Elegância e sobriedade. O ar |
| Verde | `#BFBF32` | Sustentabilidade. A terra |

- Em documentos, páginas e gráficos, use estas quatro.
- Os arquivos do logo usam as cores do próprio desenho do manual de 2019, que não são exatamente os códigos escritos nele. O manual pinta os quadrados de cor com `#005AA4`, `#FFC100`, `#94A9AC` e `#C1C112`. O logo chapado usa azul `#007DD0` por fora e `#00427D` por dentro, verde `#C1C112` e `#828809`, sol `#FFC100` e cinza `#94A9AC` translúcido; o letreiro tem "Sonnental" em `#3F4144` e "energia" em `#8A8F91`.
- **Isso é como a marca foi definida e não muda.** Os códigos oficiais continuam os escritos no manual (os quatro da tabela acima) e o logo continua com as cores do desenho. Não recolorir o logo para "bater" com os códigos, nem trocar os códigos pelas cores pintadas.
- O degradê de 2025 tinha ficado com o azul mais claro e acinzentado que o de 2019; em novembro de 2026 esse azul voltou aos tons do arquivo de 2019. Os arquivos da pasta oficial já são os corrigidos.
- O amarelo é cor de destaque (linhas, ícones, um número), não de fundo de texto corrido nem de texto sobre branco (pouco contraste).
- Em alertas e escalas de documentos, no máximo 2 níveis bem distintos (atenção em amarelo, crítico em vermelho `#C00000`); sem roxo.

## Letras

- **Ginora Sans** no nome "Sonnental" e **Open Sans Bold Italic** na assinatura "energia". Essas letras fazem parte do logo: **nunca escrever o logotipo com uma fonte qualquer**; use o arquivo.
- No texto dos materiais, Open Sans é a escolha natural (gratuita, Google Fonts). Em Word e Excel que vão sair da empresa, Calibri, porque esses arquivos não carregam a fonte junto e quem abre pode não ter a Open Sans.

## Regras de uso

- **Fundo**: a versão com degradê só sobre fundo branco. Sobre foto, a chapada ou a branca. Sobre azul, cinza ou verde da marca, o logo vai todo em branco.
- **Tamanho mínimo**: 6 × 6,5 mm para o símbolo sozinho; 26 × 6 mm para o logo com o nome.
- **Margem de segurança**: a medida x é o diâmetro do sol do símbolo. Uma medida x livre em volta do logo com o nome; meia medida em volta do símbolo sozinho.
- **Proporção**: sempre escalar mantendo a proporção.

**Não fazer:**
- Redesenhar, vetorizar de novo, "melhorar" ou gerar o símbolo com IA de imagem.
- Recolorir, trocar o degradê, aplicar sombra, contorno extra, brilho ou efeito.
- Distorcer, girar, espelhar ou cortar o símbolo.
- Usar a esfera 3D de 2026 como logo plano (vista de frente ela perde a leitura de "S" que o símbolo tem; foi testado e descartado).
- Usar letreiros antigos ("energy solutions", "energia renovável", letreiro em Open Sans de 2018) ou o arquivo do manual de 2019 quando houver o de 2025.
- Usar as peças de impressão 3D (com furos e pinos) em imagem ou apresentação.

## A esfera 3D de 2026 (referência para réplica física)

Casca esférica oca com um sol concêntrico. Da casca foi retirada uma fenda em espiral, como a casca de uma maçã descascada, sobrando uma fita única e contínua: começa na calota azul de cima, passa por trás, vira a faixa cinza na frente, passa por trás de novo e termina na calota verde de baixo. Girando 180° em torno do eixo frente-trás, o símbolo fica igual.

| Item | Valor |
|---|---|
| Esfera | perfeita, raio externo R (na bola impressa, R = 110 mm, 22 cm de diâmetro) |
| Casca | R/27,5 (4 mm em R = 110) |
| Sol | esfera concêntrica de 0,66·R, amarelo-ouro |
| Fita | 37° de latitude, constante |
| Fenda | 21° de latitude, constante, fechando em ponta viva nas duas calotas |
| Passo | 58° por volta (K = 58/360) |
| Extensão da fenda | θ de −185° a 545° |
| Peças e cores | faixa da frente (θ de −100° a +100°) cinza `#99A7AA` translúcido; o resto de cima azul `#045AA0`; o resto de baixo verde `#BFBF32` |

Convenções: θ é o azimute em graus (0 na frente, −Y; positivo para a direita de quem olha; passa de 360), φ é a latitude. Ponto: x = r·cosφ·senθ, y = −r·cosφ·cosθ, z = r·senφ. Bordas da fenda:
- φ_sup(θ) = K·θ − 18,5, para θ ≤ 185
- φ_inf(θ) = K·(θ − 360) + 18,5, para θ ≥ 175
- borda da calota de cima: K·(θ − 360) + 39,5 até θ = 389,655; depois 48,306 − (K/100)·(439,655 − θ)² até θ = 439,655; depois 48,306 constante até θ = 545 (ponta)
- metade de baixo por simetria: φ_inf(θ) = −φ_sup(360 − θ), para θ < 175

Conferência com R = 110 mm: casca 428,1 cm³; peças azul 163,1, cinza 102,0 e verde 163,1 cm³. Para gerar, use o script ou os STL das pastas "Como construir" e "Modelo 3D" no Drive, em vez de remodelar do zero.

Existe também a reconstrução do modelo original de 2018 (esfera achatada a 0,93, sol de 0,615·R, fenda de −240° a 600°, bordas por tabela). Ela é histórica; a oficial é a de 2026.

## História, em ordem

- **2018 (março)**: a Sonnental começa, em Estrela/RS, no Vale do Taquari. O designer Lorenzo (Lore) cria a marca em 3D no Rhinoceros e depois a planifica. Assinatura "energy solutions" no estudo e "energia renovável" no primeiro manual; letreiro em Open Sans. Frase da época: "Fazendo o futuro, agora."
- **2019 (janeiro)**: revisão. Nome redesenhado em Ginora Sans, assinatura só "energia", cores mais sóbrias (as quatro que valem até hoje).
- **2021 (maio e junho)**: missão, visão e valores definidos; publicados em 2023.
- **2025**: curvas do símbolo refeitas para bater com a esfera. É a versão 2D em uso.
- **2026 (novembro)**: esfera reconstruída como esfera perfeita, referência para réplicas físicas. Testada como marca plana e descartada; a 2D de 2025 continua. Na mesma revisão, o azul do degradê de 2025 voltou aos tons de 2019; desenho, versão chapada e cores oficiais ficaram como estavam.

O símbolo junta seis ideias do estudo de 2018: terra, sol, ventos, água, humano e tecnologia. O sol no centro; a fita em volta é "a envolvência e a sinergia com o todo: um abraço".

## Missão, visão e valores (texto de 2023)

- **Missão**: otimizar sistemas energéticos através da customização de produtos e serviços.
- **Visão**: democratizar a energia, produzindo bem-estar e ganhos econômicos para clientes, empresa e sociedade.
- **Valores**: inteligência, inovação e tecnologia; orientação pelo mercado; autoperformance; potencialização humana; sensibilidade social.
- O negócio: estratégias energéticas. O diferencial: personalização.

## Antes de entregar algo com a marca

1. Arquivo do logo veio da pasta oficial do Drive, na versão certa para o fundo.
2. Proporção mantida, margem de segurança respeitada, tamanho acima do mínimo.
3. Nada de logotipo escrito com fonte; nada de símbolo redesenhado.
4. Cores dos elementos do documento entre as quatro do manual (mais neutros).
5. Se for peça física ou render 3D: esfera de 2026, e sem peças de gabarito em imagem.

Versão de novembro de 2026. Dúvidas sobre a marca: Guilherme (guilherme@sonnental.com.br).
