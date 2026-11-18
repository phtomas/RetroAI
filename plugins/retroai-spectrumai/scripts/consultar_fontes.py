#!/usr/bin/env python3
"""RetroAI: localizar fontes públicas verificadas no catálogo GitHub (sem token)."""
import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

URL = "https://raw.githubusercontent.com/phtomas/RetroAI/main/plugins/retroai-spectrumai/fontes-publicas.json"
LOCAL = Path(__file__).resolve().parents[1] / "fontes-publicas.json"
USER_AGENT = "RetroAI-OficinaViva/0.2 (+https://github.com/phtomas/RetroAI)"


def obter_texto(url):
    if not url.startswith("https://raw.githubusercontent.com/"):
        raise ValueError("Somente raw.githubusercontent.com é permitido")
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=12) as reply:
        if reply.status != 200:
            raise RuntimeError("HTTP " + str(reply.status))
        data = reply.read(2_000_001)
        if len(data) > 2_000_000:
            raise ValueError("arquivo excede 2MB")
        return data.decode("utf-8")


def carregar_indice(offline=False):
    if offline:
        return json.loads(LOCAL.read_text(encoding="utf-8")), "copia local"
    try:
        return json.loads(obter_texto(URL)), URL
    except (OSError, ValueError, urllib.error.URLError, json.JSONDecodeError) as exc:
        if LOCAL.is_file():
            print("AVISO: índice remoto indisponível: " + str(exc), file=sys.stderr)
            print("Usando cópia local; atualidade NÃO confirmada.", file=sys.stderr)
            return json.loads(LOCAL.read_text(encoding="utf-8")), "copia local (fallback)"
        raise


def tokens(value):
    return set(re.findall(r"[a-z0-9à-ÿ_]+", value.casefold()))


def pesquisar(indice, modelo, termos):
    wanted = tokens(termos)
    out = []
    for item in indice["entries"]:
        if modelo != "TODOS" and item["modelo"] != modelo:
            continue
        searchable = tokens(" ".join([item["id"], item["keywords"], item["tipo"], item["repo"], item["observacao"]]))
        score = len(wanted & searchable)
        if wanted and not score:
            continue
        out.append((score, item))
    return [entry for _score, entry in sorted(out, key=lambda x: (-x[0], x[1]["id"]))]


def url_raw(item):
    return "https://raw.githubusercontent.com/{}/{}/{}".format(item["repo"], item["branch"], item["path"])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--modelo", choices=["TK90X", "TK2000", "TODOS"], default="TODOS")
    parser.add_argument("--termos", default="", help="palavras de busca sobre documentação")
    parser.add_argument("--offline", action="store_true", help="somente índice local; nenhuma consulta online")
    parser.add_argument("--abrir", action="store_true", help="verificar leitura do README das 3 primeiras fontes selecionadas")
    args = parser.parse_args(argv)
    try:
        indice, origem = carregar_indice(args.offline)
    except Exception as exc:
        print("ERRO: índice indisponível: " + str(exc), file=sys.stderr)
        return 2
    hits = pesquisar(indice, args.modelo, args.termos)
    print("Origem do índice:", origem, "| entradas:", len(indice["entries"]), "| resultados:", len(hits))
    if not hits:
        print("Sem correspondência. Confira o termo ou consulte o índice manualmente.")
    for item in hits:
        print("\n[{}] {} ({})".format(item["modelo"], item["repo"], item["tipo"]))
        print("Arquivo:", item["path"])
        print("URL:", url_raw(item))
        print("Cuidado:", item["observacao"])
    if args.abrir:
        if args.offline:
            print("\nOFFLINE: --abrir ignorado, documentos não foram consultados.")
        else:
            for item in hits[:3]:
                try:
                    content = obter_texto(url_raw(item))
                    print("\nLEITURA OK: {} ({} caracteres)".format(item["repo"], len(content)))
                    for line in content.splitlines():
                        if line.strip():
                            print("Início:", line.strip()[:180])
                            break
                except Exception as exc:
                    print("FALHA AO ABRIR {}: {}".format(item["repo"], exc))
    print("\nIMPORTANTE: índice não valida pinagem ou valores; leia o esquema e confirme revisão.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
