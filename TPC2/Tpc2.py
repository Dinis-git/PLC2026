import re


def markdownToHtml(text):
    text = CabecalhoToHtml(text)
    text = BoldToHtml(text)
    text = ItalicoToHtml(text)
    text = ListaNumeradaToHtml(text)
    text = ImagemToHtml(text)
    text = LinkToHtml(text)
    return text


def CabecalhoToHtml(text):
    regex = r'^(#{1,3})\s+(.+)$'

    def transformaCabecalho(match):
        nivel = len(match.group(1))
        titulo = match.group(2)
        return f'<h{nivel}>{titulo}</h{nivel}>'

    return re.sub(regex, transformaCabecalho, text, flags=re.MULTILINE)


def BoldToHtml(text):
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)


def ItalicoToHtml(text):
    return re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)


def ListaNumeradaToHtml(text):
    bloco = r'(?:^\d+\.[ \t]+.+(?:\n|$))+'
    item = r'^\d+\.[ \t]+(.+)$'

    def transformaLista(match):
        itens = re.findall(item, match.group(0), flags=re.MULTILINE)
        lis = '\n'.join(f'<li>{i}</li>' for i in itens)
        return f'<ol>\n{lis}\n</ol>\n'

    return re.sub(bloco, transformaLista, text, flags=re.MULTILINE)


def ImagemToHtml(text):
    regex = r'!\[(.*?)\]\((.+?)\)'

    def transformaImagem(match):
        alt = match.group(1)
        url = match.group(2)
        return f'<img src="{url}" alt="{alt}">'

    return re.sub(regex, transformaImagem, text)


def ImagemToHtml(text):
    regex = r'!\[(.*?)\]\((.+?)\)'

    def transformaImagem(match):
        alt = match.group(1)
        url = match.group(2)
        return f'<img src="{url}" alt="{alt}"/>'

    return re.sub(regex, transformaImagem, text)


def LinkToHtml(text):
    regex = r'\[(.+?)\]\((.+?)\)'

    def transformaLink(match):
        texto = match.group(1)
        url = match.group(2)
        return f'<a href="{url}">{texto}</a>'

    return re.sub(regex, transformaLink, text)


# =====================================================================
#  TESTES
# =====================================================================

OL = '<ol>\n{}\n</ol>'

TESTES = [
    # ---------- CABEÇALHOS (1-15) ----------
    ('# Exemplo', '<h1>Exemplo</h1>'),
    ('## Exemplo', '<h2>Exemplo</h2>'),
    ('### Exemplo', '<h3>Exemplo</h3>'),
    ('# Olá Mundo', '<h1>Olá Mundo</h1>'),
    ('## Segunda secção', '<h2>Segunda secção</h2>'),
    ('### Ponto 3.1', '<h3>Ponto 3.1</h3>'),
    ('# Título com números 123', '<h1>Título com números 123</h1>'),
    ('#### Quatro', '#### Quatro'),                      # só até ###
    ('#Sem espaço', '#Sem espaço'),                      # falta o espaço
    ('# A\n## B\n### C', '<h1>A</h1>\n<h2>B</h2>\n<h3>C</h3>'),
    ('Texto antes\n# Título\nTexto depois', 'Texto antes\n<h1>Título</h1>\nTexto depois'),
    ('Isto # não é cabeçalho', 'Isto # não é cabeçalho'),
    ('# Título com acentos: ção, ã, é', '<h1>Título com acentos: ção, ã, é</h1>'),
    ('#  Dois espaços', '<h1>Dois espaços</h1>'),
    ('## Título com **negrito**', '<h2>Título com <b>negrito</b></h2>'),

    # ---------- BOLD (16-30) ----------
    ('Este é um **exemplo** ...', 'Este é um <b>exemplo</b> ...'),
    ('**Tudo**', '<b>Tudo</b>'),
    ('**a** e **b**', '<b>a</b> e <b>b</b>'),
    ('Início **meio** fim', 'Início <b>meio</b> fim'),
    ('**duas palavras**', '<b>duas palavras</b>'),
    ('**negrito com números 123**', '<b>negrito com números 123</b>'),
    ('**abc', '**abc'),                                  # sem fecho
    ('abc**', 'abc**'),                                  # sem abertura
    ('Sem negrito', 'Sem negrito'),
    ('**um** **dois** **três**', '<b>um</b> <b>dois</b> <b>três</b>'),
    ('Linha 1 **a**\nLinha 2 **b**', 'Linha 1 <b>a</b>\nLinha 2 <b>b</b>'),
    ('**ç ã é**', '<b>ç ã é</b>'),
    ('Preço: **10€**', 'Preço: <b>10€</b>'),
    ('**Atenção:** leia isto', '<b>Atenção:</b> leia isto'),
    ('a**b**c', 'a<b>b</b>c'),

    # ---------- ITÁLICO (31-45) ----------
    ('Este é um *exemplo* ...', 'Este é um <i>exemplo</i> ...'),
    ('*Tudo*', '<i>Tudo</i>'),
    ('*a* e *b*', '<i>a</i> e <i>b</i>'),
    ('Início *meio* fim', 'Início <i>meio</i> fim'),
    ('*duas palavras*', '<i>duas palavras</i>'),
    ('*itálico com 123*', '<i>itálico com 123</i>'),
    ('*abc', '*abc'),                                    # sem fecho
    ('abc*', 'abc*'),                                    # sem abertura
    ('Sem itálico', 'Sem itálico'),
    ('*um* *dois* *três*', '<i>um</i> <i>dois</i> <i>três</i>'),
    ('L1 *a*\nL2 *b*', 'L1 <i>a</i>\nL2 <i>b</i>'),
    ('*ç ã é*', '<i>ç ã é</i>'),
    ('Ele disse *olá*.', 'Ele disse <i>olá</i>.'),
    ('*Nota:* importante', '<i>Nota:</i> importante'),
    ('a*b*c', 'a<i>b</i>c'),

    # ---------- LISTA NUMERADA (46-60) ----------
    ('1. Primeiro item\n2. Segundo item\n3. Terceiro item',
     OL.format('<li>Primeiro item</li>\n<li>Segundo item</li>\n<li>Terceiro item</li>')),
    ('1. Único', OL.format('<li>Único</li>')),
    ('1. A\n2. B', OL.format('<li>A</li>\n<li>B</li>')),
    ('Texto\n1. A\n2. B', 'Texto\n' + OL.format('<li>A</li>\n<li>B</li>')),
    ('1. A\n2. B\nTexto', OL.format('<li>A</li>\n<li>B</li>') + '\nTexto'),
    ('1. A\n\n1. B', OL.format('<li>A</li>') + '\n\n' + OL.format('<li>B</li>')),
    ('10. Dez\n11. Onze', OL.format('<li>Dez</li>\n<li>Onze</li>')),
    ('1. *itálico*\n2. **negrito**',
     OL.format('<li><i>itálico</i></li>\n<li><b>negrito</b></li>')),
    ('1. [UC](http://www.uc.pt)',
     OL.format('<li><a href="http://www.uc.pt">UC</a></li>')),
    ('1.Sem espaço', '1.Sem espaço'),
    ('1 Sem ponto', '1 Sem ponto'),
    ('1. A\n1. B\n1. C', OL.format('<li>A</li>\n<li>B</li>\n<li>C</li>')),
    ('5. Começa no cinco\n6. Seis', OL.format('<li>Começa no cinco</li>\n<li>Seis</li>')),
    ('Antes\n\n1. A\n2. B\n\nDepois',
     'Antes\n\n' + OL.format('<li>A</li>\n<li>B</li>') + '\n\nDepois'),
    ('1. Item com ção e é', OL.format('<li>Item com ção e é</li>')),

    # ---------- LINKS (61-72) ----------
    ('Como pode ser consultado em [página da UC](http://www.uc.pt)',
     'Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>'),
    ('[Google](https://www.google.com)', '<a href="https://www.google.com">Google</a>'),
    ('[a](x) e [b](y)', '<a href="x">a</a> e <a href="y">b</a>'),
    ('Ver [aqui](http://exemplo.pt/pagina?id=1).',
     'Ver <a href="http://exemplo.pt/pagina?id=1">aqui</a>.'),
    ('[texto com espaços](http://x.pt)', '<a href="http://x.pt">texto com espaços</a>'),
    ('[**negrito**](http://x.pt)', '<a href="http://x.pt"><b>negrito</b></a>'),
    ('[*itálico*](http://x.pt)', '<a href="http://x.pt"><i>itálico</i></a>'),
    ('[sem url]', '[sem url]'),
    ('(http://x.pt) sem texto', '(http://x.pt) sem texto'),
    ('[UC](www.uc.pt)', '<a href="www.uc.pt">UC</a>'),
    ('Link1 [a](u1)\nLink2 [b](u2)', 'Link1 <a href="u1">a</a>\nLink2 <a href="u2">b</a>'),
    ('[ção](http://x.pt/ç)', '<a href="http://x.pt/ç">ção</a>'),

    # ---------- IMAGENS (73-84) ----------
    ('Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...',
     'Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...'),
    ('![gato](gato.png)', '<img src="gato.png" alt="gato"/>'),
    ('![](vazio.png)', '<img src="vazio.png" alt=""/>'),
    ('![a](x.png) e ![b](y.png)', '<img src="x.png" alt="a"/> e <img src="y.png" alt="b"/>'),
    ('![logo](imagens/logo.jpg)', '<img src="imagens/logo.jpg" alt="logo"/>'),
    ('![texto com espaços](http://x.pt/a.png)',
     '<img src="http://x.pt/a.png" alt="texto com espaços"/>'),
    ('![sem url]', '![sem url]'),
    ('![a](x.png)\n![b](y.png)', '<img src="x.png" alt="a"/>\n<img src="y.png" alt="b"/>'),
    ('Antes ![a](x.png) depois', 'Antes <img src="x.png" alt="a"/> depois'),
    ('![ção](ç.png)', '<img src="ç.png" alt="ção"/>'),
    ('[![alt](img.png)](http://x.pt)',
     '<a href="http://x.pt"><img src="img.png" alt="alt"/></a>'),
    ('![foto 2024](fotos/2024.png)', '<img src="fotos/2024.png" alt="foto 2024"/>'),

    # ---------- MISTURAS E CASOS LIMITE (85-100) ----------
    ('# Título\nTexto com **negrito** e *itálico*.',
     '<h1>Título</h1>\nTexto com <b>negrito</b> e <i>itálico</i>.'),
    ('**a** *b*', '<b>a</b> <i>b</i>'),
    ('*a* **b**', '<i>a</i> <b>b</b>'),
    ('# **Negrito no título**', '<h1><b>Negrito no título</b></h1>'),
    ('### *Itálico no título*', '<h3><i>Itálico no título</i></h3>'),
    ('## Ver [UC](http://www.uc.pt)', '<h2>Ver <a href="http://www.uc.pt">UC</a></h2>'),
    ('**Veja** [aqui](http://x.pt)', '<b>Veja</b> <a href="http://x.pt">aqui</a>'),
    ('*Veja* ![img](a.png)', '<i>Veja</i> <img src="a.png" alt="img"/>'),
    ('# Doc\n\n1. Um\n2. Dois\n\nFim',
     '<h1>Doc</h1>\n\n' + OL.format('<li>Um</li>\n<li>Dois</li>') + '\n\nFim'),
    ('# T\n**b** *i* [l](u) ![i](p)',
     '<h1>T</h1>\n<b>b</b> <i>i</i> <a href="u">l</a> <img src="p" alt="i"/>'),
    ('1. **a**\n2. *b*\n3. [c](u)\n4. ![d](p)',
     OL.format('<li><b>a</b></li>\n<li><i>b</i></li>\n<li><a href="u">c</a></li>\n<li><img src="p" alt="d"/></li>')),
    ('Texto simples sem nada', 'Texto simples sem nada'),
    ('', ''),
    ('\n\n', ''),
    ('# T1\n1. A\n## T2\n1. B',
     '<h1>T1</h1>\n' + OL.format('<li>A</li>') + '\n<h2>T2</h2>\n' + OL.format('<li>B</li>')),
    ('**negrito *itálico* dentro**', '<b>negrito <i>itálico</i> dentro</b>'),
]

assert len(TESTES) == 100, len(TESTES)


def correr():
    falhas = 0
    for n, (entrada, esperado) in enumerate(TESTES, 1):
        obtido = markdownToHtml(entrada)
        if obtido.strip() != esperado.strip():
            falhas += 1
            print(f'--- FALHOU #{n}')
            print('entrada :', repr(entrada))
            print('esperado:', repr(esperado))
            print('obtido  :', repr(obtido))
    print(f'\n{len(TESTES) - falhas}/{len(TESTES)} testes passaram')


if __name__ == '__main__':
    correr()