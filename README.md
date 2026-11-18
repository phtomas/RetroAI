# RetroAI — SpectrumAI

Assistente técnico comunitário para **TK90X, TK95, ZX Spectrum e TK2000**: diagnóstico, circuitos, Z80, ULA, ROM, RAM, vídeo, teclado, restauração e expansões.

**Princípio:** Nada é “funcionou” sem prova. Isole e meça antes de adivinhar.

## Um projeto que não depende de um único fornecedor

Ao tentar publicar o RetroAI no diretório público do ChatGPT, a **skill passou nas verificações técnicas mostradas pelo portal**. Contudo, a OpenAI não aceitava, naquele momento, novas submissões públicas de plugins constituídos exclusivamente por *skills*. **Não houve veto individual ao RetroAI nem reprovação do conteúdo do projeto**: a restrição era à modalidade de submissão.

Por isso, a base técnica do RetroAI está disponível aqui para consulta e adaptação a ambientes compatíveis. O objetivo é que o conhecimento circule e possa ser utilizado pela comunidade sem depender exclusivamente do catálogo de uma plataforma. **Isso não significa compatibilidade universal, instalação automática ou publicação aprovada no diretório OpenAI.**

## Oficina Viva — fontes públicas consultáveis (v0.2.1)

O núcleo técnico atualizado está em [SKILL.md](plugins/retroai-spectrumai/skills/diagnostico-tk/SKILL.md), com [catálogo JSON de fontes](plugins/retroai-spectrumai/fontes-publicas.json) (23 referências públicas indexadas, TK90X e TK2000) e [buscador Python sem chave de API](plugins/retroai-spectrumai/scripts/consultar_fontes.py).

Em ambientes com Python 3 e acesso à internet:

```sh
python plugins/retroai-spectrumai/scripts/consultar_fontes.py --modelo TK2000 --termos "cassete zener" --abrir
python plugins/retroai-spectrumai/scripts/consultar_fontes.py --modelo TK90X --termos "ula temporizacao"
```

O buscador consulta o índice no GitHub e, com `--abrir`, verifica a leitura das três primeiras fontes. **Não interpreta esquemas automaticamente nem substitui o técnico.** Assistentes com ferramentas de navegação/GitHub podem seguir diretamente o protocolo do SKILL.md. Sem ferramenta de rede, a skill **não pode** alegar consulta atualizada; o leitor também pode enviar arquivos.

A ampliação para TK2000 inclui a [reconstrução de Clemar Folly](https://github.com/clemarfolly/Microdigital-TK2000), o [índice de projetos de Rubem](https://github.com/frubem/Project-TK2000) e projetos especializados. O TK2000 original, as reconstruções, os forks e as expansões **não são intercambiáveis**. Atribuições e licenças de terceiros continuam próprias.

## Política de acervo e créditos

As pastas privadas **RetroAI** e **Retropie** do Drive foram auditadas apenas para identificar temas, autoria e referências. **Nenhum arquivo privado do Drive foi publicado**. O catálogo aponta exclusivamente a arquivos já públicos nos sites e repositórios de seus autores, priorizando o upstream antes de forks. Não espelhamos ROMs, manuais, livros, fotos nem projetos de terceiros sem licença expressa. Dos protótipos do autor, referenciamos somente o que já estava público no Git.

## Obter o pacote

[Baixar o pacote público RetroAI-SpectrumAI-v0.2.1.zip](releases/RetroAI-SpectrumAI-v0.2.1.zip) (recomendado; política links-only) · [ZIP antigo v0.1.0](releases/RetroAI-SpectrumAI-v0.1.0.zip) (legado, sem consulta indexada)

Este ZIP é uma **reconstrução pública portátil do núcleo técnico**, não uma exportação integral do plugin instalado na conta do autor. Não contém credenciais, documentos privados do Google Drive ou documentação de terceiros não licenciada para redistribuição.

### Como utilizar

- **Por ZIP:** ambientes que aceitam instalação de plugins a partir de arquivos podem importar o pacote, conforme a política e os recursos de cada aplicativo.
- **Em agentes compatíveis com skills:** o material pode servir como base para adaptação à estrutura suportada pelo ambiente; não presuma que o ZIP funcione diretamente em todas as ferramentas.
- **Diretamente no ChatGPT:** a publicação pública de um plugin skills-only ainda não estava disponível para esta submissão; por isso, não anunciamos instalação de um clique no diretório.

Leia o [guia curto para os leitores](docs/Guia-de-uso-RetroAI.md).

## Um técnico TK/ZX no bolso?

Sabemos que a experiência mais simples seria abrir o aplicativo no celular e chamar imediatamente o técnico de TK/ZX. Ainda não oferecemos isso de forma universal. Em uma etapa futura, podemos estudar um **robozinho técnico próprio**, acessível pela web e pelo celular, com conteúdo de TK, ZX e outros micros. Trata-se de uma intenção, **não de serviço já publicado**.

## Exemplo de pergunta

> Meu TK90X mostra tela preta. Como verifico as linhas de energia, o clock e o RESET do Z80 antes de trocar componentes?

Informe modelo, revisão, sintomas, alterações, fotos e medições reais.

## Segurança, suporte e direitos

As respostas devem separar fatos medidos de hipóteses. Desenergize para reparos e confira sempre a revisão e a pinagem no esquema correto. Cada usuário deve conectar e autorizar seus **próprios** documentos quando desejar consultas externas.

- [Guia para os leitores](docs/Guia-de-uso-RetroAI.md)
- [Suporte](SUPPORT.md)
- [Privacidade](PRIVACY.md)
- [Termos de uso](TERMS.md)

**Observação sobre reutilização:** a disponibilidade pública dos arquivos não substitui uma licença formal de uso, modificação e redistribuição. Antes de oferecer versões derivadas publicamente, confirme a licença aplicável. Nosso objetivo é definir uma licença permissiva específica para os materiais de autoria do projeto, respeitando sempre os direitos de terceiros.
