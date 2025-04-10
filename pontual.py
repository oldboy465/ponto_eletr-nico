from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import schedule

# Função para executar a rotina de automação
def automacao_rotina():
    # Configurar o driver do Firefox
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--disable-notifications")  # Desativa notificações
    driver = webdriver.Firefox(options=firefox_options)

    try:
        # Acessar o link
        driver.get("https://sis.sig.uema.br/sigrh/login.jsf;jsessionid=ACEBB9D6ABCE71B96C62A032E2CF57B6.s1i1")
        time.sleep(4)

        # Preencher o campo de CPF
        cpf_field = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/form/table/tbody/tr[1]/td/input")
        cpf_field.send_keys("03773068352")
        time.sleep(0.5)

        # Preencher o campo de senha
        senha_field = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/form/table/tbody/tr[2]/td/input")
        senha_field.send_keys("undertaker")
        time.sleep(0.5)

        # Clicar no botão de login
        login_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/form/table/tfoot/tr/td/input")
        login_button.click()
        time.sleep(4)

        # Continuar com os próximos passos
        next_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/table/tbody/tr/td/form/div[1]/div[4]/a/table/tbody/tr/td[2]/p")
        next_element.click()
        time.sleep(4)

        final_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/table/tbody/tr[1]/td/form/table/tfoot/tr/td/input[1]")
        final_element.click()
        time.sleep(4)

    finally:
        # Fechar a guia
        driver.quit()
        print("Rotina concluída e guia fechada.")

# Perguntar ao usuário o horário desejado para execução
horario = input("Em que horário você deseja executar essa rotina? (Formato HH:MM): ")

# Agendar a execução da rotina
schedule.every().day.at(horario).do(automacao_rotina)

print(f"Rotina agendada para {horario}. Aguardando execução...")

# Manter o script rodando para verificar o agendamento
while True:
    schedule.run_pending()
    time.sleep(1)