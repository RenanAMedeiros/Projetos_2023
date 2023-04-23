import pandas as pd
from selenium import webdriver
from time import sleep
from openpyxl import load_workbook
from selenium import webdriver as opcoesSelenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

df = pd.read_excel("Consulta_SDPWIN.xlsx")
 
# Tratando o arquivo importado .xlsx
 
df_ajustado = df[['Placa','Chassi','Renavam','UF','Procedencia','DataEmissaoCRV','DataEmissaoCRLV','Exercicio',
                  'Cor','MarcaModelo','Combustivel','Categoria','Carroceria','Especie','Tipo','AnoFabricacao',
                  'AnoModelo','CapPassageiro','NumMotor','Nome','Documento','NomeAnterior','IPVA_Licen','Multas',
                  'TotalIPVA','TotalLicen','TotalDPVAT','Dersa','Der','Detran','Cetesb','Renainf','Municipais',
                  'PRF','TotalMultas','CV_ComunicVenda','CV_Inclusao','CV_TipoComprador','CV_DocComprador','CV_DataVenda',
                  'CV_NotaFiscal','CV_Protocolo','IG_CodFinanceira','IG_NomeFinanceira','IG_DocProprietario','IG_NomeProprietario',
                  'IG_Inclusao','IG_NumContrato','IG_VigenciaContrato','IG_TipoTransacao','IG_TipoRestricao','G_RestricaoFinanceira1',
                  'G_RestricaoFinanceira2','G_RestricaoFinanceira3','G_RestricaoFinanceira4','G_CodFinanceira','G_NomeFinanceira',
                  'G_DocProprietario','G_NomeProprietario','G_Inclusao','G_NumContrato','G_VigenciaContrato','G_TipoTransacao',
                  'G_TipoRestricao','OrgaoAutuador','Infracao','NumAutoInfracao','DataInfracao','Valor','ValorPago','Furto',
                  'Guincho','Administrativa','Judicial','Tributaria','Renajud']]
print(df_ajustado)

# Iniciando o navegador
driver = webdriver.Chrome()

# Acessando o formulário
driver.get("https://www.ipva.fazenda.sp.gov.br/ipvanet_consulta/consulta.aspx")
driver.maximize_window()

# Iterando sobre a coluna "Placa" e enviando cada valor individualmente
for renavam,placa in  zip(df_ajustado['Placa'],df_ajustado['Renavam']):
    placa_input = driver.find_element(By.ID, "conteudoPaginaPlaceHolder_txtPlaca")
    renavam_input = driver.find_element(By.ID ,"conteudoPaginaPlaceHolder_txtRenavam")
    placa_input.send_keys(placa)
    renavam_input.send_keys(renavam)
    renavam_input.submit

        
formulario = driver.find_element(By.CLASS_NAME ,"recaptcha-checkbox-border")
formulario.click()

captcha = driver.find_element(By.ID ,"conteudoPaginaPlaceHolder_btn_Consultar")
captcha.click()
sleep(5)