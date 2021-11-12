import base64

secrets = "V1lXTXtZMFVfY0hBck1FZF90SDNfJE40SzN9"
secrets = base64.b64decode(secrets).decode('utf-8')
print(secrets)
