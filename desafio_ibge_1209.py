from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
import time

# configurações iniciais

# criando pasta dados caso não exista
download_dir = os.path.join(os.getcwd(), "dados")
os.makedirs(download_dir, exist_ok=True)

# função de logs
def log(msg):
    print(f"[STEP] {msg}")

# função de click por seletor
def click(locator, value, name="", human=False, retries=3):
    log(f"click: {name}")

    for i in range(retries):
        try:
            el = wait.until(
                EC.presence_of_element_located((locator, value))
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                el
            )

            wait.until(
                EC.element_to_be_clickable((locator, value))
            )

            if human:
                actions.move_to_element(el).pause(0.1).click().perform()
            else:
                driver.execute_script(
                    "arguments[0].click();",
                    el
                )

            return

        except Exception as e:
            log(f"falha click {name} tentativa {i+1}: {e}")
            time.sleep(0.5)

    raise Exception(f"falhou click: {name}")

# função para verificação de download
def aguardar_download(nome_arquivo, timeout=30):
    caminho = os.path.join(download_dir, nome_arquivo)

    if os.path.exists(caminho):
        os.remove(caminho)

    inicio = time.time()

    while time.time() - inicio < timeout:

        if os.path.exists(caminho):

            arquivo_temp = caminho + ".crdownload"

            if not os.path.exists(arquivo_temp):
                log("download concluído")
                return

        time.sleep(1)

    raise Exception("arquivo não foi baixado")


# tenta a automação inteira até 3 vezes
for tentativa in range(1, 4):

    driver = None

    try:

        # configuração de página do chrome
        log(f"INICIANDO TENTATIVA {tentativa}/3")

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--incognito")

        options.add_experimental_option("prefs", {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

        driver.execute_cdp_cmd("Page.setDownloadBehavior", {
            "behavior": "allow",
            "downloadPath": download_dir
        })

        wait = WebDriverWait(driver, 40)
        actions = ActionChains(driver)

        # início automação - abrindo página inicial
        log("abrindo site")
        driver.get("https://sidra.ibge.gov.br/")

        # navegação de página até tabela
        click(By.XPATH, "//a[contains(text(),'Pesquisas')]", "Pesquisas")
        click(By.XPATH, "//span[normalize-space()='População']", "População")
        click(By.XPATH, "//a[contains(.,'Censo Demográfico')]", "Censo")
        click(By.XPATH, "//a[contains(.,'Demográfico 2022')]", "2022")
        click(By.XPATH, "//a[contains(.,'População por Idade e Sexo')]", "Idade e Sexo")
        click(By.XPATH, "//a[@href='/tabela/1209']", "Tabela 1209")

        # ajuste de preferências tabela
        click(By.XPATH, "//button[@data-cmd='alternarSomatorio']", "Somatorio")
        time.sleep(1)

        click(By.XPATH, "//span[normalize-space()='Total']", "Total")
        click(By.XPATH, "//span[normalize-space()='60 a 69 anos']", "60-69")
        click(By.XPATH, "//span[normalize-space()='70 anos ou mais']", "70+")

        click(By.XPATH, "//li[@id='arvore-355e-1']//button[@class='sidra-toggle']")
        click(By.XPATH, "//li[@id='arvore-435e-1']//button[@class='sidra-toggle']")

        # abrindo e preenchendo pop-up de download
        log("abrindo download")

        click(By.ID, "botao-downloads", "download", human=True)

        log("aguardando modal")

        wait.until(EC.presence_of_element_located((By.NAME, "nome-arquivo")))
        nome = driver.find_element(By.NAME, "nome-arquivo")

        log("Escolhendo campo Nome do Arquivo")

        for i in range(3):
            actions.send_keys(Keys.TAB).perform()
            time.sleep(1)


        log("preenchendo nome")

        driver.execute_script("arguments[0].focus();",nome)

        active = driver.switch_to.active_element
        active.send_keys("populacao_60mais_1209")

        time.sleep(1)

        log("Selecionando campo Formato")

        actions.send_keys(Keys.TAB).perform()

        time.sleep(1)

        log("formato")

        active = driver.switch_to.active_element
        active.send_keys("CSV (BR)")

        time.sleep(1)

        # download do arquivo CSV
        log("download final")

        click(By.ID, "opcao-downloads", "download final", human=True)

        aguardar_download("populacao_60mais_1209.csv")

        log("finalizado com sucesso")

        break

    except Exception as e:

        log(f"ERRO NA TENTATIVA {tentativa}/3: {e}")

        if tentativa == 3:
            raise

    finally:

        if driver:
            driver.quit()