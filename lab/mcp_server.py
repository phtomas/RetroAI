"""RetroAI — Oficina dos Clássicos: servidor MCP local somente leitura.

Requer Python 3.11+ e pacote mcp 2.x. Sem rede e sem execução de comandos.
"""
from pathlib import Path
import json
import sys

from mcp.server.mcpserver import MCPServer

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CATALOG = ROOT / "plugins" / "retroai-spectrumai" / "fontes-publicas.json"
sys.path.insert(0, str(HERE))
from rag import search as search_notes  # noqa: E402

mcp = MCPServer("RetroAI — Oficina dos Clássicos")


def _sources() -> list[dict]:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    assert data.get("publication") == "links-only", "Catálogo sem política links-only"
    return data["entries"]


def _present(entry: dict) -> dict:
    # Apenas metadados, nenhum corpo de documento protegido.
    return {
        "id": entry["id"],
        "modelo": entry["modelo"],
        "categoria": entry["tipo"],
        "autor_origem": entry["repo"].split("/")[0],
        "repositorio": entry["repo"],
        "caminho": entry["path"],
        "url": "https://github.com/{}/blob/{}/{}".format(
            entry["repo"], entry["branch"], entry["path"]
        ),
        "advertencia": entry["observacao"],
        "status": "referencia_publica_nao_validacao_eletrica",
    }


@mcp.tool()
def listar_fontes(modelo: str = "TODOS") -> list[dict]:
    """Lista links do catálogo público por modelo; sem baixar ou copiar arquivos."""
    modelo = modelo.upper().strip()
    if modelo not in {"TODOS", "TK90X", "TK2000", "TK95", "ZX SPECTRUM"}:
        return [{"erro": "modelo nao catalogado"}]
    target = "TK90X" if modelo in {"TK95", "ZX SPECTRUM"} else modelo
    return [_present(e) for e in _sources() if target == "TODOS" or e["modelo"] == target]


@mcp.tool()
def buscar_fontes(termos: str, modelo: str = "TODOS", limite: int = 8) -> list[dict]:
    """Seleciona fontes pela descrição e palavras-chave, sem fingir ter lido esquemas."""
    tokens = {x.casefold() for x in termos.split() if x.strip()}
    fontes = listar_fontes(modelo)
    if not tokens:
        return fontes[:max(1, min(limite, 20))]
    ranked = []
    for item in fontes:
        original = next((x for x in _sources() if x["id"] == item["id"]), None)
        if original is None:
            continue
        haystack = " ".join(str(original.get(k, "")) for k in
                            ("repo", "keywords", "tipo", "observacao")).casefold()
        score = sum(term in haystack for term in tokens)
        if score:
            ranked.append((score, item))
    ranked.sort(key=lambda x: (-x[0], x[1]["id"]))
    return [e for _, e in ranked[:max(1, min(limite, 20))]]


@mcp.tool()
def buscar_notas_autorizadas(consulta: str, limite: int = 5) -> dict:
    """Pesquisa apenas notas locais explicitamente aprovadas, com referência."""
    return search_notes(consulta, limite)


if __name__ == "__main__":
    mcp.run()
