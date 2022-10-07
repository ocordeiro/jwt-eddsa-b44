import json
import pyqrcodeng as pyqrcode
import jwt

private_key = b"""-----BEGIN PRIVATE KEY-----d
MC4CAQAwBQYDK2VwBCIEIE/O8gYJBDInm1G+SW65uDJ8nmUNU+DBdcQLHZRR/ra4
-----END PRIVATE KEY-----"""

public_key = b"""-----BEGIN PUBLIC KEY-----
MCowBQYDK2VwAyEAG5vyTfslFJmeKs4U3OuAfZjBPcP+WtN3mQxFpy+tiVE=
-----END PUBLIC KEY-----"""

json_data = json.dumps({
    "nome": "FULANO CICLANO DE TAL DA SILVA SANTOS",
    "cpf": "12345678901",
    "cargo": "POLICIAL MILITAR",
    "filiacao": "FULANA CICLANA DE TAL DA SILVA SANTOS",
    "matricula": "123456789",
    "posicao": "SOLDADO 1ª CLASSE",
    "dataNascimento": "17/12/1980",
    "numeroCartao": "XXXXXXXXX",
    "origem": "POLÍCIA MILITAR DO RIO GRANDE DO NORTE",
    "uf": "RN",
    "validade": "Indeterminada",
})

jwt_token = jwt.sign(json_data, private_key)

qrcode = pyqrcode.create(jwt_token, error='L', mode='alphanumeric')

print(qrcode)

data = jwt.verify(jwt_token, public_key)
