<div align="center">

# TPC2 · Conversor de Markdown para HTML

**Processamento de Linguagens e Compiladores · 2026**

<img src="../foto.png" alt="Dinis Macedo, A111531" width="150">

**Dinis Macedo** · `a111531`

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-→-HTML-informational)

</div>

---

## 🎯 Objetivo

Criar em **Python** um pequeno conversor de **Markdown para HTML**, cobrindo os elementos descritos na secção *Basic Syntax* da Cheat Sheet de Markdown.

## 📋 Elementos suportados

| Elemento | Sintaxe Markdown | Resultado HTML |
|---|---|---|
| Cabeçalho 1 | `# texto` | `<h1>texto</h1>` |
| Cabeçalho 2 | `## texto` | `<h2>texto</h2>` |
| Cabeçalho 3 | `### texto` | `<h3>texto</h3>` |
| Negrito | `**texto**` | `<b>texto</b>` |
| Itálico | `*texto*` | `<i>texto</i>` |
| Lista numerada | `1. item` | `<ol><li>item</li></ol>` |
| Link | `[texto](url)` | `<a href="url">texto</a>` |
| Imagem | `![alt](path)` | `<img src="path" alt="alt"/>` |

---

## 🔍 Exemplos

### Cabeçalhos

Linhas iniciadas por `#`, `##` ou `###`.

**Entrada**
```md
# Exemplo
```

**Saída**
```html
<h1>Exemplo</h1>
```

### Negrito

Pedaços de texto entre `**`.

**Entrada**
```md
Este é um **exemplo** ...
```

**Saída**
```html
Este é um <b>exemplo</b> ...
```

### Itálico

Pedaços de texto entre `*`.

**Entrada**
```md
Este é um *exemplo* ...
```

**Saída**
```html
Este é um <i>exemplo</i> ...
```

### Lista numerada

**Entrada**
```md
1. Primeiro item
2. Segundo item
3. Terceiro item
```

**Saída**
```html
<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>
```

### Link

Formato `[texto](endereço URL)`.

**Entrada**
```md
Como pode ser consultado em [página da UC](http://www.uc.pt)
```

**Saída**
```html
Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>
```

### Imagem

Formato `![texto alternativo](path para a imagem)`.

**Entrada**
```md
Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...
```

**Saída**
```html
Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...
```

---

<div align="center">
<sub>Processamento de Linguagens e Compiladores · 2026</sub>
</div>
