import aws_cdk as cdk
from aws_cdk import (
    Stack,
    CfnOutput,
    RemovalPolicy,
    aws_lambda as _lambda,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
)
from constructs import Construct


class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # 1. Crear la función Lambda
        my_function = _lambda.Function(
            self,
            "HelloWorldFunction",
            runtime=_lambda.Runtime.NODEJS_20_X,
            handler="index.handler",
            code=_lambda.Code.from_inline("""
exports.handler = async function(event) {
    return {
        statusCode: 200,
        body: JSON.stringify('Hello World!'),
    };
};
"""),
        )

        # URL pública para la Lambda
        my_function_url = my_function.add_function_url(
            auth_type=_lambda.FunctionUrlAuthType.NONE
        )

        # 2. Crear el Bucket S3
        my_bucket = s3.Bucket(
            self,
            "SemilleroDataBucket",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        # 3. Subir automáticamente el archivo hola.txt con el contenido "hola mundo"
        s3deploy.BucketDeployment(
            self,
            "DeployHolaMundoFile",
            sources=[s3deploy.Source.data("hola.txt", "hola mundo")],
            destination_bucket=my_bucket,
        )

        # Salidas impresas en consola
        CfnOutput(
            self,
            "LambdaFunctionUrlOutput",
            value=my_function_url.url,
            description="URL publica de la funcion Lambda",
        )
        CfnOutput(
            self,
            "S3BucketNameOutput",
            value=my_bucket.bucket_name,
            description="Nombre del bucket S3",
        )