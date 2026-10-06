# TPC1 - PLC 2026

## Dinis Macedo, a111531

<img src="../foto.png" alt="Dinis Macedo, A111531" width="150">

---

## Objetivo

Expressão regular para apanhar strings binárias que **não** contenham a substring `011`.

## Resposta

```regex
^1*0*(0|10)*1?$
```
