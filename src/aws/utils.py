from storages.backends.s3boto3 import S3Boto3Storage
from storages.backends.s3boto import S3BotoStorage

# Utilizando o Boto3
# Por motivos de instabilidade, configurar os controles de acesso ACLs como 'falso' no aws s3
# StaticRootS3BotoStorage = lambda: S3Boto3Storage(location='static')
# MediaRootS3BotoStorage  = lambda: S3Boto3Storage(location='media')

# Utilizando o Boto
StaticRootS3BotoStorage = lambda: S3BotoStorage(location='static')
MediaRootS3BotoStorage  = lambda: S3BotoStorage(location='media')