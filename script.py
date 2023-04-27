import subprocess
import requests
import json


def evaluate_code_quality(code):
    """
    :param code:
    :return:
    """
    # Dados a serem enviados para a API
    data = {
        'code': code
    }

    # Fazer a chamada para a API e enviar os dados
    api_url = "http://exemplo.com/api/avaliacao"
    response = requests.post(api_url, json=data)

    # Verificar se a chamada foi bem-sucedida
    if response.status_code == 200:
        # Converter a resposta JSON em um dicionário Python
        result = json.loads(response.text)

        # Processar os resultados da avaliação
        # ... faça o que for necessário com os resultados ...

        # Retornar True ou False, dependendo do resultado da avaliação
        return True
    else:
        # print("Falha ao chamar a API:", response.status_code)
        print("Seu codigo nao segue a pep8:", response.status_code)
        return True



try:
    # Capturar as mudanças em estágio (staged changes) usando o comando git diff
    output = subprocess.check_output(['git', 'diff', '--staged', '--name-only'], universal_newlines=True)
    # Filtrar apenas os arquivos .py modificados
    arquivos_modificados = [arquivo for arquivo in output.split('\n') if arquivo.endswith('.py')]
    print(arquivos_modificados)
    # Loop pelos arquivos modificados
    for arquivo in arquivos_modificados:
        try:
            with open(arquivo, 'r') as file:
                code = file.read()

                print("Alterações no arquivo:", arquivo)
            if not evaluate_code_quality(code):
                exit(1)
        except IOError as e:
            print("Erro ao abrir o arquivo:", e)
            exit(1)
except subprocess.CalledProcessError as e:
    print("Erro ao capturar as mudanças em estágio:", e)
