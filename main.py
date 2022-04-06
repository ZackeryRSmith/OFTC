# coding: utf-8
#!/usr/bin/env python

import base64

id = input()

try:
    int(id)  # Test for a valid user id
    encodedBytes = base64.b64encode(str(id).encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    print(encodedStr)
except:
    print("An error has occurred while encoding (invalid user id?)")
    exit(1)

