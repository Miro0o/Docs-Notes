# Troubleshooting

[TOC]



## Res


## 👉 OpenSSL crypto error: [('PEM routines', 'PEM_read_bio', 'no start line')]

According to [http://www.pyopenssl.org/en/stable/api/crypto.html#OpenSSL.crypto.load_certificate](http://www.pyopenssl.org/en/stable/api/crypto.html#OpenSSL.crypto.load_certificate),`load_certificate()` takes a buffer (string will do) containing the certificate, not a filename. 

Your need to do:
```python
	with open(filename, "r") as my_cert_file:
    my_cert_text = my_cert_file.read()
    cert = load_certificate(FILETYPE_PEM, my_cert_text)
```


[OpenSSL crypto error: ('PEM routines', 'PEM_read_bio', 'no start line')]: https://stackoverflow.com/questions/37120860/openssl-crypto-error-pem-routines-pem-read-bio-no-start-line


## Ref

