# Práctica AWS CDK

Este repositorio contiene la solución del ejercicio práctico de **AWS CDK con Python** para el semillero. 

---

## 1. ¿Qué se construyó?

A través de código en Python e Infraestructura como Código (IaC) con AWS CDK:
1. **AWS Lambda**: Se creó una función serverless en Node.js 20 con una **Function URL** pública sin autenticación que retorna `"Hello World!"`.
2. **Amazon S3**: Se aprovisionó un bucket de S3 configurado con eliminación automática (`RemovalPolicy.DESTROY` y `autoDeleteObjects=True`).
3. **Carga Automática**: Se utilizó el módulo `aws_s3_deployment` para subir automáticamente un archivo llamado `hola.txt` con el contenido `"hola mundo"`.

---

## 2. Comandos exactos ejecutados

### A. Preparación del entorno local
```bash
# Instalación global del CLI de CDK mediante npm
npm install -g aws-cdk

# Verificación de la versión de CDK con npx
npx cdk --version

# Inicialización del proyecto CDK en Python
npx cdk init app --language python

# Activación del entorno virtual de Python
source .venv/bin/activate

# Instalación de las dependencias requeridas (aws-cdk-lib y constructs)
pip install -r requirements.txt
```

### B. Configuración de AWS y Síntesis
```bash
# Verificación del código e inspección de la plantilla de CloudFormation
npx cdk synth

# Configuración de credenciales de AWS CLI
aws configure

# Preparación del entorno de AWS para CDK (Bootstrapping)
npx cdk bootstrap
```

### C. Despliegue de la infraestructura
```bash
# Despliegue de la pila en la cuenta de AWS
npx cdk deploy
```

### D. Verificación de los recursos en vivo
```bash
# Pruebas a la URL pública de la función Lambda
curl https://ectno25sl656tkvv7ng5jtnpte0ivkst.lambda-url.us-east-1.on.aws/

# Inicio de sesión en AWS SSO (en caso de expiración del token)
aws sso login

# Lectura directa del archivo subido en el bucket S3
aws s3 cp s3://cdkstack-semillerodatabucketb4d48d6d-sjonz9qgqyvq/hola.txt -
```

### E. Destrucción de la infraestructura
```bash
# Eliminación completa de los recursos en AWS para evitar costos
npx cdk destroy
```
