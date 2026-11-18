# IALAB — RetroAI Oficina dos Clássicos

**Status: scaffold em Git, NÃO instalado ou executado no IALAB.** Sem serviço hospedado.

## Arquitetura proposta
- Skill pública: protocolo, segurança e citações.
- MCP Python local em stdio: catálogo público, seleção de links por modelo, consulta a notas autorizadas.
- RAG v0: SQLite FTS5, somente arquivos Markdown autorais revisados em pasta allowlist local.
- RAG v1: embeddings locais na RTX 3060, separação por fontes, versionamento e evidências após testes.
- KiCad: integração separada; primeiro leitura e ERC/DRC; edição de esquemáticos e PCBs em branch/sandbox, sempre com revisão humana.

## Política
Nunca importar Drive privado, livros, ROMs, manuais ou fotos de terceiros para o índice aberto; preferir URLs públicas dos respectivos autores. Dos protótipos próprios, citar só o já disponível no Git. Nenhuma ferramenta de gravação ou energização de hardware.

## Execução prevista (Python 3.11+)
1. Instalar MCP SDK 2.x no ambiente virtual do laboratório: pip install "mcp>=2,<3"
2. Criar a base local: python lab/rag.py init
3. Executar MCP sob cliente que suporta stdio: python lab/mcp_server.py
4. Colocar exclusivamente notas autorizadas na pasta lab/knowledge/approved e reconstruir o índice local.

## Portões
- G0 — Escopo, autoria e política de acesso: DOCUMENTADO
- G1 — Testes unitários da busca e índices: PENDENTE
- G2 — Testar descoberta e chamadas MCP em cliente: PENDENTE
- G3 — Testar recuperação com citações e proteção contra falsificação: PENDENTE
- G4 — KiCad: netlist, ERC, DRC e inspeção de revisões: PENDENTE
- G5 — Bancada real com medição reproduzível: PENDENTE

## KiCad
Conforme documentação oficial, IPC API do KiCad 9/10 atende prioritariamente ao editor PCB; suporte no esquemático surge com KiCad 11. KiCad 10 pode usar arquivos de esquema e kicad-cli, sem afirmar API interativa oficial no esquemático. Não declarar Gerber pronto apenas por passar DRC.

Fonte: https://dev-docs.kicad.org/en/apis-and-binding/ipc-api/for-addon-developers/
