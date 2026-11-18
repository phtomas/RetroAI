# RetroAI — Oficina dos Clássicos: um assistente técnico para toda a comunidade

O **RetroAI — Oficina dos Clássicos** nasceu para ajudar a compreender e reparar **TK90X, TK95, ZX Spectrum e TK2000**: interpretar esquemas, investigar falhas de Z80, ULA, ROM e RAM, planejar medições e distinguir hipóteses de evidências.

## Por que o projeto ganhou um caminho independente?

Durante a tentativa de publicação no diretório público de plugins, a **skill técnica passou nas verificações mostradas pelo portal**. Entretanto, naquele momento a OpenAI não aceitava novas submissões públicas de plugins compostos **apenas por skills**. **Não foi um veto individual ao RetroAI ou a seu autor, nem uma reprovação de seu conteúdo:** tratava-se de uma restrição da modalidade de publicação.

A limitação nos levou a manter **a base técnica disponível no GitHub**, permitindo consulta e adaptação para assistentes de IA compatíveis. Essa base não é um assistente universal de instalação com um clique: cada plataforma possui seus próprios formatos, políticas, recursos e limites de uso.

## Como usar hoje

1. Acesse o [repositório do RetroAI](https://github.com/phtomas/RetroAI).
2. Consulte a documentação e baixe o pacote ZIP disponível na pasta [`releases`](../releases). Use a versão **0.2.1** do ZIP, que inclui índice de 23 fontes técnicas públicas, protocolo de consulta e script de busca sem chave de API; a versão 0.1.0 é legada.
3. Em um ambiente que suporte a importação desse tipo de plugin ou de skills, siga o procedimento do aplicativo. Se não houver importação direta, os arquivos técnicos podem servir como referência de instruções para um assistente compatível; isso requer adaptação e respeito às condições de uso dos arquivos.
4. Ao solicitar ajuda, informe **modelo, revisão da placa, sintomas, modificações e medições já realizadas**; inclua fotos legíveis e o esquema correto, quando possível.

**Exemplo de pergunta:** “Meu TK90X apresenta tela preta. O que devo medir nas linhas de energia, no clock e no RESET do Z80 antes de trocar componentes?”

## E o nosso robozinho técnico?

Ainda não podemos garantir a comodidade de tirar o celular do bolso, abrir o bom e velho ChatGPT e chamar imediatamente o técnico de retrocomputação. Quem sabe, no futuro, possamos colocar no ar **nosso próprio robô técnico**, acessível pelo navegador e pelo celular, para conversar sobre TK, ZX e muito mais? **Essa é uma possibilidade futura, não um serviço já disponível.**

**Segurança e método:** nada é “funcionou” sem prova. Isole e meça antes de adivinhar. Desenergize o equipamento para inspeções e reparos, respeite os riscos elétricos e confira a revisão correta do esquema.

**Endereço permanente do projeto:** https://github.com/phtomas/RetroAI

## Consultar as fontes técnicas no GitHub

Acesse o [catálogo de fontes públicas](../plugins/retroai-spectrumai/fontes-publicas.json) e a [skill atualizada](../plugins/retroai-spectrumai/skills/diagnostico-tk/SKILL.md). Em Python 3, com acesso à rede, execute a partir da raiz deste repositório:

```sh
python plugins/retroai-spectrumai/scripts/consultar_fontes.py --modelo TK2000 --termos "placa revisão" --abrir
```

Não precisa de token, API paga, MCP hospedado pelo autor nem IALAB ligado. O script consulta arquivos de repositórios **públicos** no GitHub. O uso integrado depende de o assistente ter navegação web, conector GitHub ou capacidade de executar o script. Não há garantia de instalação automática em todos os aplicativos.

**Atenção:** distinguir TK2000 original, réplicas, revisões, expansões e projetos FPGA; conservar os créditos de Rubem/frubem, Clemar, hkzlab e demais autores upstream. Não copiar material de terceiros sem verificar a licença.

## Política de fontes (acervo Drive)

O acervo privado RetroAI/Retropie foi utilizado apenas para identificar referências. **Não é disponibilizado aos usuários da skill.** Esta aponta links públicos dos autores originais, mantendo créditos; não redistribui ROMs, manuais, livros, scans, esquemas, programas ou protótipos privados. Para TKGA/TKbus, apenas o que já consta da prévia pública do Git é referenciável; não confundir simulação com homologação física.
