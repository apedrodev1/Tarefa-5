from flask import Flask, request, jsonify
import pickle
import boto3
from io import BytesIO

# Função para carregar o modelo do S3
def load_model_from_s3(bucket_name, model_file_name):
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket_name, Key=model_file_name)
    bytestream = BytesIO(obj['Body'].read())
    model = pickle.load(bytestream)
    return model

app = Flask(__name__)

# Carregar modelo do S3
model = load_model_from_s3('sprint5-hotelreservations', 'random_forest_model_hotel_reservations.pkl')

@app.route('/api/v1/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        # Extrair features do JSON
        features = [
            data.get('no_of_adults', 0),  # Usando 0 como valor padrão
            data.get('no_of_children', 0),
            # Adicione aqui outros campos
        ]
        
        # Certifique-se de que as features estejam na mesma ordem usada para treinar o modelo
        
        # Fazer a previsão usando o modelo
        result = model.predict([features])[0]  # O resultado será um array; pegamos o primeiro elemento
        
        # Retornar o resultado como JSON
        return jsonify({"result": int(result)})  # Convertendo o resultado para int, se necessário
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=True)
    

import boto3

# Inicializar o cliente do S3
s3 = boto3.client('s3', 
                  aws_access_key_id='AKIATZZ27WR7ZX7KICGS', 
                  aws_secret_access_key='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')

# Nome do bucket e do arquivo
bucket_name = 'sprint5-hotelreservations'
file_name = 'caminho/do/seu/arquivo'

# Realizar o upload
s3.upload_file(file_name, bucket_name, 'nome-no-s3')

print("Upload realizado com sucesso.")

