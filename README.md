# JWT EdDSA Base44
The token is a base44 encoded string separated by spaces.
As it uses base 44, the token can be used in an alphanumeric QR Code. The technique allows more data to be stored in a QR code.

## Caracteristics
- Edwards-curve Digital Signature Algorithm (EdDSA) using Ed25519 curve
- Base44 encoding

## Example of token
```
ICGTHFI$E8U7MN44OB$M4/A4$*C2SD8U7HN4GBDH0B$M4/A4%SF24F8U7.M4TO4 9HFWBF VQC1H7X4MVEM*2I6LPQBKGKITVMNOMAB5K78+IVLHCWNJ8-W*LIQXA%B9PSLA:PU-5*W83F0H-0*B10A7DEDGVLPC5*:WT/3
```