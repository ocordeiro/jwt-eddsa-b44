from typing import Union

BASE44_CHARSET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ$%*+-./:"
BASE44_DICT = {v: i for i, v in enumerate(BASE44_CHARSET)}

def encode(buf: bytes) -> bytes:
    res = ""
    buflen = len(buf)
    for i in range(0, buflen & ~1, 2):
        x = (buf[i] << 8) + buf[i + 1]
        e, x = divmod(x, 44 * 44)
        d, c = divmod(x, 44)
        res += BASE44_CHARSET[c] + BASE44_CHARSET[d] + BASE44_CHARSET[e]
    if buflen & 1:
        d, c = divmod(buf[-1], 44)
        res += BASE44_CHARSET[c] + BASE44_CHARSET[d]
    return res.encode()


def decode(s: Union[bytes, str]) -> bytes:
    try:
        if isinstance(s, str):
            buf = [BASE44_DICT[c] for c in s.rstrip("\n")]
        elif isinstance(s, bytes):
            buf = [BASE44_DICT[c] for c in s.decode()]
        else:
            raise TypeError("Type must be 'str' or 'bytes'")

        buflen = len(buf)
        if buflen % 3 == 1:
            raise ValueError("Invalid base44 string")

        res = []
        for i in range(0, buflen, 3):
            if buflen - i >= 3:
                x = buf[i] + buf[i + 1] * 44 + buf[i + 2] * 44 * 44
                if x > 0xFFFF:
                    raise ValueError
                res.extend(divmod(x, 256))
            else:
                x = buf[i] + buf[i + 1] * 44
                if x > 0xFF:
                    raise ValueError
                res.append(x)
        return bytes(res)
    except (ValueError, KeyError, AttributeError):
        raise ValueError("Invalid base44 string")