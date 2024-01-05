from tkinter import E
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import smtplib
import time
import json

dados = {
    "impressoras": []
}

# Configurações
chrome_options = Options()
chrome_options.add_argument('--headless')  # Remova o modo headless para visualizar o navegador
chrome_options.add_argument('--disable-gpu')


def samsung():
    # Endereço IP da impressora
    ip_imp_samsung = ["http://192.168.1.81/sws/index.html", "http://192.168.1.84/sws/index.html"]

    for ip in ip_imp_samsung:
        try:
            # Configurações do WebDriver
            driver = webdriver.Chrome(options=chrome_options)
            wait = WebDriverWait(driver, 20)  # Aumente o tempo de espera

            # Abrir o navegador e acessar o endereço IP da impressora
            driver.get(ip)

            #informações da pagina princinpal
            modelo = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/fieldset/div/div/div/div/div/div/div[3]/div/div/div/div[1]/div[2]'))).text
            host_name_imp = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/fieldset/div/div/div/div/div/div/div[3]/div/div/div/div[2]/div[2]'))).text
            serie_number = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/fieldset/div/div/div/div/div/div/div[3]/div/div/div/div[3]/div[2]'))).text
            ipv4_address = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/fieldset/div/div/div/div/div/div/div[3]/div/div/div/div[4]/div[2]'))).text
            mac_address = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/fieldset/div/div/div/div/div/div/div[3]/div/div/div/div[6]/div[2]'))).text
            printer_status = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/fieldset/div/div/div/div/div/div/div[2]/div/div/div[1]/span'))).text
            printer_alert = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/fieldset/div/div/div/div/div/div/div[2]/div/div/div[2]/span/a'))).text

            # Clicar na aba "informacao"
            informacao_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/table/tbody/tr/td[3]/table')))
            time.sleep(2)
            informacao_button.click()

            # Adicione um tempo de espera explícito após clicar em "informacao"
            wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div/div/div/ul/div/li/ul/li[3]/div')))

            # Clicar na aba "Contadores de uso"
            contadores_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div/div/div/ul/div/li/ul/li[3]/div')))
            time.sleep(2)
            contadores_button.click()

            # Obter o total de impressões
            total_impressoes = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/fieldset[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div/div[1]/div[2]/div/div[3]/table/tbody/tr/td[6]/div'))).text

            #clicar na aba "suprimentos"
            suprimentos_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div/div/div/ul/div/li/ul/li[2]/div')))
            time.sleep(2)
            suprimentos_button.click()

            status_toner = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/div/div[1]/div/div/fieldset/div/div/div/div[2]/div/div/fieldset/div/div/div[1]/div[1]/div/div'))).text
            nivel_toner = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/div/div[1]/div/div/fieldset/div/div/div/div[2]/div/div/fieldset/div/div/div[2]/div[1]/div/div'))).text
            qtd_imp = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/div/div[1]/div/div/fieldset/div/div/div/div[2]/div/div/fieldset/div/div/div[3]/div[1]/div/div'))).text
            capac_toner = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/div/div[1]/div/div/fieldset/div/div/div/div[2]/div/div/fieldset/div/div/div[4]/div[1]/div/div'))).text
            model_toner = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/div/div[1]/div/div/fieldset/div/div/div/div[2]/div/div/fieldset/div/div/div[5]/div[1]/div/div'))).text
            serie_toner = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/div/div[1]/div/div/fieldset/div/div/div/div[2]/div/div/fieldset/div/div/div[6]/div[1]/div/div'))).text
            
            if(ip == "http://192.168.1.81/sws/index.html"):
                dados_impressora = {
                    "local": "ADM",
                    "modelo": modelo,
                    "host": host_name_imp,
                    "serie": serie_number,
                    "total_imp": total_impressoes,
                    "ip": ipv4_address,
                    "status": printer_status,
                    "mac": mac_address,
                    "alert": printer_alert,
                    "toners": [
                        {
                            "status": status_toner,
                            "nivel": nivel_toner,
                            "qtd": qtd_imp,
                            "capacidade": capac_toner,
                            "modelo": model_toner,
                            "serie": serie_toner
                        }
                    ]
                }
            else:
                dados_impressora = {
                "local": "Apoio 1",
                "modelo": modelo,
                "host": host_name_imp,
                "serie": serie_number,
                "total_imp": total_impressoes,
                "ip": ipv4_address,
                "status": printer_status,
                "mac": mac_address,
                "alert": printer_alert,
                "toners": [
                    {
                        "status": status_toner,
                        "nivel": nivel_toner,
                        "qtd": qtd_imp,
                        "capacidade": capac_toner,
                        "modelo": model_toner,
                        "serie": serie_toner
                    }
                ]
            }
                
            dados['impressoras'].append(dados_impressora) 

    
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

        finally:
            # Fechar o navegador
            driver.quit()

def engenharia():
    # Endereço IP da impressora
    ip = "https://192.168.1.55/hp/device/DeviceStatus/Index"


    # Configurações do WebDriver
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--disable-web-security')
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 20)  # Aumente o tempo de espera
    

    # Abrir o navegador e acessar o endereço IP da impressora
    driver.get(ip)

    #informação da tela principal
    printer_alert = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[2]/form/div/div[1]/div/div/span[2]'))).text

    time.sleep(2)
    #ir para a aba de configuração
    driver.get("https://192.168.1.55/hp/device/InternalPages/Index?id=ConfigurationPage")

    #informacoes da pagina configuração
    modelo = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[1]/div/p[3]/strong'))).text
    host_name_imp = ''
    serie_number = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[1]/div/p[5]/strong'))).text
    ipv4_address = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[2]/div/p[16]/strong'))).text
    mac_address = ''
    printer_status = ''

    # Ir para a aba "status suprimento"
    driver.get("https://192.168.1.55/hp/device/InternalPages/Index?id=SuppliesStatus")

    amarelo_status = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/p[1]/strong'))).text
    amarelo_nivel = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div/p[1]'))).text
    amarelo_impresso = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/p[4]/strong'))).text
    amarelo_modelo = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div/p[2]/span'))).text
    amarelo_serie =wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/p[3]/strong'))).text

    magenta_status = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/p[1]/strong'))).text
    magenta_nivel = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div/p[1]'))).text
    magenta_impresso = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/p[4]/strong'))).text
    magenta_modelo = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div/p[2]/span'))).text
    magenta_serie =wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/p[3]/strong'))).text

    ciano_status = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/p[1]/strong'))).text
    ciano_nivel = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/div/p[1]'))).text
    ciano_impresso = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/p[4]/strong'))).text
    ciano_modelo = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/div/p[2]/span'))).text
    ciano_serie =wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/p[3]/strong'))).text

    black_status = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/p[1]/strong'))).text
    black_nivel = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div/p[1]'))).text
    black_impresso = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/p[4]/strong'))).text
    black_modelo = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div/p[2]/span'))).text
    black_serie =wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/p[3]/strong'))).text

    dados_impressora = {
            "local": "Engenharia",
            "modelo": modelo,
            "host": host_name_imp,
            "serie": serie_number,
            "total_imp": "",
            "ip": ipv4_address,
            "status": printer_alert,
            "mac": "",
            "alert": "",
            "toners": [
                {
                    "status": amarelo_status,
                    "nivel": amarelo_nivel,
                    "qtd": amarelo_impresso,
                    "capacidade": "",
                    "modelo": amarelo_modelo,
                    "serie": amarelo_serie
                },
                    {
                    "status": magenta_status,
                    "nivel": magenta_nivel,
                    "qtd": magenta_impresso,
                    "capacidade": "",
                    "modelo": magenta_modelo,
                    "serie": magenta_serie
                },
                {
                    "status": ciano_status,
                    "nivel": ciano_nivel,
                    "qtd": ciano_impresso,
                    "capacidade": "",
                    "modelo": ciano_modelo,
                    "serie": ciano_serie
                },
                {
                    "status": black_status,
                    "nivel": black_nivel,
                    "qtd": black_impresso,
                    "capacidade": "",
                    "modelo": black_modelo,
                    "serie": black_serie
                }
            ]
        }
            
    dados['impressoras'].append(dados_impressora) 
    

    # Fechar o navegador
    driver.quit()

def logistica():
    ip = "https://192.168.1.43/sws/index.html"

    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--disable-web-security')

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 20)

    driver.get(ip)

    modelo = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/fieldset/div/div/div/div/div/div/div[3]/div/div/div/div[1]/div[2]'))).text
    host = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/fieldset/div/div/div/div/div/div/div[3]/div/div/div/div[2]/div[2]'))).text
    serie = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/fieldset/div/div/div/div/div/div/div[3]/div/div/div/div[3]/div[2]'))).text
    ipv4 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/fieldset/div/div/div/div/div/div/div[3]/div/div/div/div[4]/div[2]'))).text
    mac = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/fieldset/div/div/div/div/div/div/div[3]/div/div/div/div[6]/div[2]'))).text
    status = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/fieldset/div/div/div/div/div/div/div[2]/div/div/div[1]/span'))).text
    alerta = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/fieldset/div/div/div/div/div/div/div[2]/div/div/div[2]/span/a'))).text
    
    #botao informacao
    inf_but = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[4]/div/div/div/table/tbody/tr/td[3]/table/tbody/tr/td[2]/em/button')))
    time.sleep(2)
    inf_but.click()

    cont_but = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div/div/div/ul/div/li/ul/li[3]/div/a/span')))
    time.sleep(2)
    cont_but.click()

    total_imp = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/fieldset[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div/div[1]/div[2]/div/div[3]/table/tbody/tr/td[6]/div'))).text
    
    #suprimentos botao
    sup_botao = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div/div/div/ul/div/li/ul/li[2]/div')))
    time.sleep(2)
    sup_botao.click()

    status_toner = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/div/div[1]/div/div/fieldset/div/div/div/div[2]/div/div/fieldset/div/div/div[1]/div[1]/div/div'))).text
    nivel_toner = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/div/div[1]/div/div/fieldset/div/div/div/div[2]/div/div/fieldset/div/div/div[2]/div[1]/div/div'))).text
    qtd_imp = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/div/div[1]/div/div/fieldset/div/div/div/div[2]/div/div/fieldset/div/div/div[3]/div[1]/div/div'))).text
    capac_toner = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/div/div[1]/div/div/fieldset/div/div/div/div[2]/div/div/fieldset/div/div/div[4]/div[1]/div/div'))).text
    model_toner = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/div/div[1]/div/div/fieldset/div/div/div/div[2]/div/div/fieldset/div/div/div[5]/div[1]/div/div'))).text
    serie_toner = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/div/div[1]/div/div/fieldset/div/div/div/div[2]/div/div/fieldset/div/div/div[6]/div[1]/div/div'))).text

    #unidade de imagem 
    status_img = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/div/div[3]/div/div/fieldset/div/div/div/div[2]/div/div/fieldset/div/div/div[1]/div[1]/div/div'))).text
    nivel_img = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/div/div[3]/div/div/fieldset/div/div/div/div[2]/div/div/fieldset/div/div/div[2]/div[1]/div/div'))).text
    qtd_imp_img = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/div/div[3]/div/div/fieldset/div/div/div/div[2]/div/div/fieldset/div/div/div[3]/div[1]/div/div'))).text
    capac_img = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/div/div[3]/div/div/fieldset/div/div/div/div[2]/div/div/fieldset/div/div/div[4]/div[1]/div/div'))).text
    model_img = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/div/div[3]/div/div/fieldset/div/div/div/div[2]/div/div/fieldset/div/div/div[5]/div[1]/div/div'))).text
    serie_img = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/div/div/div/div/div[3]/div/div/fieldset/div/div/div/div[2]/div/div/fieldset/div/div/div[6]/div[1]/div/div'))).text

    
    dados_impressora = {
        "local": "Logística",
        "modelo": modelo,
        "host": host,
        "serie": serie,
        "total_imp": total_imp,
        "ip": ipv4,
        "status": status,
        "mac": mac,
        "alert": alerta,
        "toners": [
            {
                "status": status_toner,
                "nivel": nivel_toner,
                "qtd": qtd_imp,
                "capacidade": capac_toner,
                "modelo": model_toner,
                "serie": serie_toner
            }
        ],
        "imagem": [
            {
                "status": status_img,
                "nivel": nivel_img,
                "qtd": qtd_imp_img,
                "capacidade": capac_img,
                "modelo": model_img,
                "serie": serie_img
            }
        ]
    }

    dados['impressoras'].append(dados_impressora)

def fabrica():
    ip = "http://192.168.1.79/"

    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--disable-web-security')

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 20)

    driver.get(ip)

    status = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div/div/div[2]/form/div[2]/dl/dd[1]/div/span'))).text

    #maintence botao
    maintence = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/div[3]/a')))
    time.sleep(2)
    maintence.click()

    modelo = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div/div/div[2]/form/div[5]/dl/dd[1]'))).text
    serie = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div/div/div[2]/form/div[5]/dl/dd[2]'))).text
    host = ''
    ipv4 = '192.168.1.79'
    mac = ''
    alerta = ''

    status_toner = ''
    qtd_imp = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div/div/div[2]/form/div[6]/dl/dd[1]'))).text
    nivel_toner = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div/div/div[2]/form/div[7]/dl/dd[2]'))).text
    tambor_nivel = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div/div/div[2]/form/div[7]/dl/dd[1]'))).text
    capac_toner = ''
    model_toner = ''
    serie_toner = ''

    dados_impressora = {
        "local": "Fábrica",
        "modelo": modelo,
        "host": host,
        "serie": serie,
        "total_imp": qtd_imp,
        "ip": ipv4,
        "status": status,
        "mac": mac,
        "alert": alerta,
        "toners": [
            {
                "status": status_toner,
                "nivel": nivel_toner,
                "qtd": '',
                "capacidade": capac_toner,
                "modelo": model_toner,
                "serie": serie_toner
            }
        ],
        "tambor": tambor_nivel
    }

    dados['impressoras'].append(dados_impressora)

def revenda():
    ip = "http://192.168.1.83/"

    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--disable-web-security')

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 20)

    driver.get(ip)
    modelo = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]'))).text
    print(modelo)
    '''
    status = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div/div/div[2]/form/div[2]/dl/dd[1]/div/span'))).text

    #maintence botao
    maintence = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/div[3]/a')))
    time.sleep(2)
    maintence.click()

    modelo = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div/div/div[2]/form/div[5]/dl/dd[1]'))).text
    serie = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div/div/div[2]/form/div[5]/dl/dd[2]'))).text
    host = ''
    ipv4 = '192.168.1.79'
    mac = ''
    alerta = ''

    status_toner = ''
    qtd_imp = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div/div/div[2]/form/div[6]/dl/dd[1]'))).text
    nivel_toner = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div/div/div[2]/form/div[7]/dl/dd[2]'))).text
    tambor_nivel = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div/div/div[2]/form/div[7]/dl/dd[1]'))).text
    capac_toner = ''
    model_toner = ''
    serie_toner = ''

    dados_impressora = {
        "local": "Fábrica",
        "modelo": modelo,
        "host": host,
        "serie": serie,
        "total_imp": qtd_imp,
        "ip": ipv4,
        "status": status,
        "mac": mac,
        "alert": alerta,
        "toners": [
            {
                "status": status_toner,
                "nivel": nivel_toner,
                "qtd": '',
                "capacidade": capac_toner,
                "modelo": model_toner,
                "serie": serie_toner
            }
        ],
        "tambor": tambor_nivel
    }

    dados['impressoras'].append(dados_impressora)'''

samsung()
engenharia()
logistica()
fabrica()
#revenda()
print(dados)
