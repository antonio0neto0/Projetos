# selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as CondicaoEsperada
from random import randint

def iniciar_driver():
    chrome_options = Options()
    # Fonte de opções de switches https://peter.sh/experiments/chromium-command-line-switches/

    arguments = ['--lang=pt-BR', '--window-size=1300,1000',
                '--incognito']
    ''' Common arguments
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-us , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada)
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU
    '''
    for argument in arguments:
        chrome_options.add_argument(argument)

    caminho_padrao_para_download = 'E:\\Storage\\Desktop'

    # Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/32352ad08ee673a4d43e8593ce988b224f6482d3/chrome/common/pref_names.cc
    chrome_options.add_experimental_option("prefs", {
        'download.default_directory': caminho_padrao_para_download,
        # Atualiza diretório para diretório passado acima
        'download.directory_upgrade': True,
        # Setar se o navegar deve pedir ou não para fazer download
        'download.prompt_for_download': False,
        "profile.default_content_setting_values.notifications": 2,  # Desabilita notificações
        # Permite realizar múltiplos downlaods multiple downloads
        "profile.default_content_setting_values.automatic_downloads": 1,
    })

    driver = webdriver.Chrome(options=chrome_options)
    
    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )
    return driver,wait

email = input('Digite seu email ou usuario: ')
senha = input('Digite sua senha: ')
comentario = input('Digite seu comentario: ')

# ações repetitivas:
def preencher_campo(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep((randint(1, 5)/40))

driver, wait = iniciar_driver()
# Entrar no site do instagram
driver.get('https://www.instagram.com/')
driver.maximize_window()

# Clicar e digitar meu usuário
campo_email = wait.until(CondicaoEsperada.element_to_be_clickable(
    (By.XPATH, "//input[@name='username']")))
preencher_campo(email, campo_email)
sleep(0.8)
# Clicar e digitar minha senha
campo_senha = wait.until(CondicaoEsperada.element_to_be_clickable(
    (By.XPATH, "//input[@name='password']")))
preencher_campo(senha, campo_senha)
sleep(0.8)
# Clicar no campo entrar
botao_entrar = wait.until(CondicaoEsperada.element_to_be_clickable(
    (By.XPATH, "//div[text()='Entrar']")))
sleep(3)
botao_entrar.click()
sleep(15)

driver.get('https://www.instagram.com/lucasranngel/')
sleep(5)
    # Clicar na última  postagem
postagem = wait.until(CondicaoEsperada.visibility_of_any_elements_located((
    By.XPATH, '//div[@class="_aagw"]')))
postagem[0].click()
sleep(3)

 # Verificar se postagem foi curtida, caso não tenha sido, clicar curtir, caso já tenha sido, aguardar 24hrs
try:
    verifica_curtida =wait.until(CondicaoEsperada.visibility_of_any_elements_located((
        By.XPATH, '//section//div[@role="button"]//*[@aria-label="Curtir"]')))
except:
    print('A imagem já havia sido curtida.')
    
else:
    botao_curtir = wait.until(CondicaoEsperada.visibility_of_any_elements_located((
        By.XPATH, '//article[@role="presentation"]//section//div[@role="button"]')))
    sleep(5)
    driver.execute_script('arguments[0].click()', botao_curtir[0])
    print('Deu certo! A imagem acabou de ser curtida.')
    

# digitar
campo_comentario = driver.find_element(By.XPATH, '//textarea[@class="x1i0vuye xvbhtw8 x1ejq31n xd10rxx x1sy0etr x17r0tee x5n08af x78zum5 x1iyjqo2 x1qlqyl8 x1d6elog xlk1fp6 x1a2a7pz xexx8yu x4uap5 x18d9i69 xkhd6sd xtt52l0 xnalus7 xs3hnx8 x1bq4at4 xaqnwrm"]')
sleep(1)
campo_comentario.click()
sleep(1)
campo_comentario = driver.find_element(By.XPATH, '//textarea[@class="x1i0vuye xvbhtw8 x1ejq31n xd10rxx x1sy0etr x17r0tee x5n08af x78zum5 x1iyjqo2 x1qlqyl8 x1d6elog xlk1fp6 x1a2a7pz xexx8yu x4uap5 x18d9i69 xkhd6sd xtt52l0 xnalus7 xs3hnx8 x1bq4at4 xaqnwrm focus-visible"]')

preencher_campo(comentario, campo_comentario)

#clicar enviar
campo_comentario.send_keys(Keys.ENTER)
print('Deu certo! O seu comentario foi enviado.')
print('Pressione ENTER para encerrar!')


input('')