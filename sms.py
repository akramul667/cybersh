# Encoded By PyEncryptor
# A Product Of ToxicNoob
# https://github.com/Toxic-Noob

import marshal, base64, zlib

exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))