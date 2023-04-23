from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# inicializa o driver do navegador
driver = webdriver.Chrome()

# navega até a página do formulário HTML
driver.get("https://cpag.prf.gov.br/nada_consta/index.jsf")

# solicita que o usuário insira um valor para o campo de entrada de texto
valor = input("Digite um valor para o campo de texto: ")

# localiza o campo de entrada de texto usando XPath
campo_de_texto = driver.find_element_by_xpath("//input[@name='nome']")

# insere o valor fornecido no campo de texto
campo_de_texto.send_keys(valor)

# fecha o navegador
driver.quit()