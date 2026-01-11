---
titulo: "Harlequin: imagem 2×2 / artefatos — incompatibilidade por mistura de CIs 74HC"
data: 2026-01-11
plataforma: "ZX Spectrum Harlequin (réplica TTL)"
tags:
  - zx-spectrum
  - harlequin
  - ttl
  - 74hc00
  - 74hc08
  - video
  - sincronismo
  - incompatibilidade
  - marcas
---

# Resumo (1 linha)
Sintoma de vídeo “4 telas” + artefatos foi causado por **mistura de 74HC de marcas diferentes** (HLF + Texas Instruments) em posições críticas.

# Sintoma observado
- Imagem parecendo **2×2 telas** (quatro quadros repetidos).
- **Artefatos**/“lixo” na base da tela.
- Ocorre inclusive com **ROM de diagnósticos**.

# Placa / contexto
- Projeto: **Harlequin** (ULA discreta com TTL/CMOS).
- CIs envolvidos:
  - **U27, U23, U21 = 74HC00** (NAND)
  - “Também troquei alguns **74HC08**” (AND)

# Diagnóstico / causa raiz
- Os 74HC00 **marca HLF** funcionavam em **testador de CI**, porém apresentavam falha **in-circuit** quando usados junto com 74HC da **Texas Instruments**.
- Substituir os **HLF** por **Texas Instruments** resolveu.

> Observação técnica: em projetos como o Harlequin, várias portas (NAND/AND/etc) participam de **timing e geração seequencial** de vídeo. Mesmo quando dois CIs são “compatíveis” em pinagem e família (74HC), diferenças de **atraso de propagação**, **edge rate**, **capacitâncias** e **níveis de entrada/saída** podem comer a margem de tempo e causar efeitos geométricos no vídeo.

# Evidência / como foi confirmado
1) CIs “passavam” no testador.
2) Após troca:
   - U27/U23/U21 (74HC00) por **TI**
   - + alguns 74HC08
3) O Harlequin passou a funcionar normalmente.

# Correção aplicada (passo-a-passo curto)
1. Identificar CIs críticos do timing (no seu caso: **U27/U23/U21 = 74HC00**).
2. Substituir **todos** os 74HC00 HLF por **um único fabricante confiável** (ex.: TI / Nexperia).
3. Se ainda houver instabilidade, padronizar também os 74HC08 e demais CIs do bloco de vídeo/timing.

# Prevenção (para próximas montagens)
- Evitar misturar “74HC” de fabricantes/clones desconhecidos em **blocos de vídeo/timing**.
- Padronizar por fabricante e, se possível, por **lote**.
- Confirmar que é **74HC** (não 74HCT/74LS), pois limiares de entrada diferem.

# Palavras-chave para busca futura (cole no seu buscador)
- "Harlequin 2x2 screen"
- "Harlequin quad screen"
- "Harlequin 74HC00 brand incompatibility"
- "HLF 74HC00 Texas Instruments"
- "U27 U23 U21 74HC00 Harlequin"
- "pass in tester fail in circuit 74HC"

# Relato original (texto)
"I had… U27, U23, U21 (74HC00) chips that are ok in my tester but seems that HLF brand can't be used alongside Texas IC's - replaced with Texas and working now... So I replaced them and also some 08's too..."
