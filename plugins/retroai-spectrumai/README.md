# RetroAI — Oficina dos Clássicos v0.3.0

Núcleo técnico portátil para investigação de TK90X/TK95/ZX Spectrum e TK2000.

- `skills/diagnostico-tk/SKILL.md`: método, regras de consulta, citações e segurança.
- `fontes-publicas.json`: índice com 23 entradas de fontes GitHub.
- `scripts/consultar_fontes.py`: buscador Python 3 (somente biblioteca padrão, sem token).
- `plugin.json`: metadados para plataformas que suportem este formato.

A skill determina **como** consultar fontes; a leitura de páginas requer ferramenta de navegação/GitHub do ambiente. Em Python 3 com internet:

```sh
python scripts/consultar_fontes.py --modelo TK2000 --termos "cassete zener" --abrir
```

Para diagnóstico real, confirme revisão, esquema, alimentação, pinagem e medições. Referências de forks/reconstruções e FPGA não equivalem ao circuito original. Nenhum serviço de IA está incluso no ZIP, nem há garantia de instalação automática. Projeto: https://github.com/phtomas/RetroAI
