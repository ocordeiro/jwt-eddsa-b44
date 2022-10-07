import json
import base44
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key

def sign(json_data, private_key):

    private_key = load_pem_private_key(private_key, password=None)

    jwt_header = {
        "typ": "JWT",
        "alg": "EdDSA",
        "ver": "1"
    }

    jwt_header = json.dumps(jwt_header)
    jwt_header = base44.encode(bytes(jwt_header, "utf8")).decode('utf8')

    jwt_body = base44.encode(bytes(json_data, "utf8")).decode('utf8')
    jwt_content = str(jwt_header) + " " + str(jwt_body)

    jwt_signature = private_key.sign(bytes(jwt_content, "utf8"))
    jwt_signature = base44.encode(jwt_signature).decode('utf8')

    return jwt_content + " " + str(jwt_signature)

def verify(jwt_content, public_key):

    public_key = load_pem_public_key(public_key)

    jwt_header, jwt_body, jwt_signature = jwt_content.split(" ")

    jwt_content = jwt_header + " " + jwt_body
    
    jwt_signature = base44.decode(jwt_signature)
    
    public_key.verify(jwt_signature, bytes(jwt_content, "utf8"))

    return base44.decode(jwt_body)