# JWT EdDSA Base44
O token é encodado em base44 e é composto por 3 partes separadas por espaço " ".
Por utilizar base44 o token poder ser utilizado em QRCode alfanumérico. A técnica permite que mais dados sejam armazenados em um código QR.

## Caracteristicas:
- Algoritmo de assinatura digital EdDSA, basedo em Edwards Curves (Ed25519)
- Encodado em base44 para ser utilizado em QRCode alfanumérico

# Exemplo de token
```
ICGTHFI$E8U7MN44OB$M4/A4$*C2SD8U7HN4GBDH0B$M4/A4%SF24F8U7.M4TO4 9HFWBF VQC1H7X4MVEM*2I6LPQBKGKITVMNOMAB5K78+IVLHCWNJ8-W*LIQXA%B9PSLA:PU-5*W83F0H-0*B10A7DEDGVLPC5*:WT/3
```