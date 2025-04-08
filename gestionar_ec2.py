import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Cliente EC2
ec2 = boto3.client('ec2', region_name='us-east-1')

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Cliente EC2
ec2 = boto3.client('ec2', region_name='us-east-1')

# Cliente S3
s3 = boto3.client('s3')

# Función para listar las instancias EC2 y su estado
def list_ec2_instances():
    try:
        instances = ec2.describe_instances()
        if 'Reservations' in instances and len(instances['Reservations']) > 0:
            print("Listado de Instancias EC2:")
            for reservation in instances['Reservations']:
                for instance in reservation['Instances']:
                    instance_id = instance['InstanceId']
                    state = instance['State']['Name']
                    public_ip = instance.get('PublicIpAddress', 'No disponible')
                    print(f"Instancia ID: {instance_id}, Estado: {state}, IP Pública: {public_ip}")
        else:
            print("No hay instancias EC2 disponibles.")
    except (NoCredentialsError, PartialCredentialsError):
        print("Error: No se encontraron credenciales válidas para AWS.")
    except Exception as e:
        print(f"Error al listar las instancias EC2: {str(e)}")

# Función para listar los buckets de S3 y sus objetos
def list_s3_buckets():
    try:
        response = s3.list_buckets()
        if 'Buckets' in response:
            print("\nListado de Buckets S3 y sus Objetos:")
            for bucket in response['Buckets']:
                print(f"Bucket: {bucket['Name']}")
                objects = s3.list_objects_v2(Bucket=bucket['Name'])
                if 'Contents' in objects:
                    for obj in objects['Contents']:
                        print(f"  - {obj['Key']} (Última modificación: {obj['LastModified']})")
                else:
                    print("  No hay objetos en este bucket.")
        else:
            print("No hay buckets S3 disponibles.")
    except Exception as e:
        print(f"Error al listar los buckets S3: {str(e)}")

# Función para generar reporte de uso de recursos
def generate_usage_report():
    try:
        print("\n=== Reporte Automático de Uso de Recursos ===\n")
        list_ec2_instances()
        list_s3_buckets()
        print("\n=== Fin del Reporte ===")
    except Exception as e:
        print(f"Error al generar el reporte: {str(e)}")

# Ejecutar el script
if __name__ == "__main__":
    generate_usage_report()

                    public_ip = instance.get('PublicIpAd
