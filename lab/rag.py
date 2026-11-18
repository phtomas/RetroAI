"""Índice local FTS5 de notas AUTORAIS aprovadas. Sem download de terceiros."""
from pathlib import Path
import json
import re
import sqlite3
import sys

ROOT = Path(__file__).resolve().parent
APPROVED = ROOT / "knowledge" / "approved"
DB = ROOT / "retroai-local.sqlite3"


def build() -> dict:
    APPROVED.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB)
    try:
        con.execute("DROP TABLE IF EXISTS notes")
        con.execute("CREATE VIRTUAL TABLE notes USING fts5(title, body, path UNINDEXED, tokenize='unicode61 remove_diacritics 2')")
        count = 0
        for file in sorted(APPROVED.glob("*.md")):
            if not file.is_file() or file.is_symlink() or file.stat().st_size > 100_000:
                continue
            text = file.read_text(encoding="utf-8")
            if not text.startswith("PUBLICACAO_AUTORIZADA: SIM\n"):
                continue
            if not re.search(r"(?m)^AUTORIA: .+", text):
                continue
            con.execute("INSERT INTO notes(title,body,path) VALUES(?,?,?)",
                        (file.stem, text, file.name))
            count += 1
        con.commit()
        return {"status": "ok", "notas_indexadas": count,
                "observacao": "Somente notas locais marcadas como autorizadas"}
    finally:
        con.close()


def search(query: str, limit: int = 5) -> dict:
    terms = re.findall(r"[\wÀ-ÿ]+", query, flags=re.UNICODE)[:8]
    if not terms:
        return {"resultados": [], "status": "consulta_vazia"}
    if not DB.is_file():
        return {"resultados": [], "status": "indice_nao_criado"}
    limit = max(1, min(int(limit), 10))
    expression = " OR ".join('"' + term.replace('"', '') + '"' for term in terms)
    con = sqlite3.connect(f"file:{DB.as_posix()}?mode=ro", uri=True)
    try:
        results = []
        rows = con.execute(
            "SELECT title, path, snippet(notes,1,'[',']',' … ',28) AS trecho "
            "FROM notes WHERE notes MATCH ? ORDER BY bm25(notes) LIMIT ?",
            (expression, limit)).fetchall()
        for title, path, trecho in rows:
            results.append({"titulo": title, "arquivo_local": path, "trecho": trecho,
                            "natureza": "nota_local_autorizada_nao_verificada_em_bancada"})
        return {"status": "ok", "resultados": results}
    finally:
        con.close()


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in {"init", "search"}:
        raise SystemExit("Uso: python lab/rag.py init | search termos")
    print(json.dumps(build() if sys.argv[1] == "init" else search(" ".join(sys.argv[2:])),
                     ensure_ascii=False, indent=2))
