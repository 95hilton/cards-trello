#importação de módulo para fazer requisição e interpretar o json
import requests
import json
file = open('result_trello.txt','w')

########################################conta cartões na lista FILA###################################
urlFila = "https://api.trello.com/1/lists/5cb317ea95fa3658f92275b3/cards"

queryFila = {
                   'key': '8382afbb5d5cc2e3a068dd326fa89f92',
                   'token': '791fde721ccb53158d6c8a10a9199651e18cb7c659972f3beefb247cb4ef5425'
                                               }

responseFila = requests.request(
                   "GET",
                    urlFila,
                    params=queryFila
                                                                   )

#converte resposta em JSON
dataFila = json.loads(responseFila.text)
tamanhoFila=len(dataFila)
print("Qtd cartões em FILA:", tamanhoFila)
file.write("Qtd cartões em FILA: "+ str(tamanhoFila)+"\n")
#print(type(dataFila))
#print(dataFila)



########################################conta cartões na lista AG ATIVAÇAO###################################
urlAgAtivacao = "https://api.trello.com/1/lists/5fbffc4d0117b488fa59e9c6/cards"

queryAgAtivacao = {
                           'key': '8382afbb5d5cc2e3a068dd326fa89f92',
                                              'token': '791fde721ccb53158d6c8a10a9199651e18cb7c659972f3beefb247cb4ef5425'
                                                                                             }

responseAgAtivacao = requests.request(
                           "GET",
                                               urlAgAtivacao,
                                                                   params=queryAgAtivacao
                                                                                                                                      )

#converte resposta em JSON
dataAgAtivacao = json.loads(responseAgAtivacao.text)
tamanhoAgAtivacao=len(dataAgAtivacao)
print("Qtd cartões em Aguardando Ativação: ", tamanhoAgAtivacao)
file.write("Qtd cartões em Aguardando Ativação: "+ str(tamanhoAgAtivacao)+"\n")
#print(type(dataFila))
#print(dataFila)

########################################conta cartões na lista reserva IP###################################
urlReservaIP = "https://api.trello.com/1/lists/5cb317ea95fa3658f92275b4/cards"

queryReservaIP = {
              'key': '8382afbb5d5cc2e3a068dd326fa89f92',
              'token': '791fde721ccb53158d6c8a10a9199651e18cb7c659972f3beefb247cb4ef5425'
              }

responseReservaIP = requests.request(
           "GET",
              urlReservaIP,
                 params=queryReservaIP
                 )

#converte resposta em JSON
dataReservaIP = json.loads(responseReservaIP.text)

tamanhoReservaIP=len(dataReservaIP)
print("Qtd cartões Reserva IP:", tamanhoReservaIP)
file.write("Qtd cartões Reserva IP: "+ str(tamanhoReservaIP)+"\n")
#print(type(dataReservaIP))
#print(dataReservaIP)

########################################conta cartões na lista configurar VLAN###################################
urlConfigurarVLAN = "https://api.trello.com/1/lists/5cb317ea95fa3658f92275b5/cards"

queryConfigurarVLAN = {
                      'key': '8382afbb5d5cc2e3a068dd326fa89f92',
                                    'token': '791fde721ccb53158d6c8a10a9199651e18cb7c659972f3beefb247cb4ef5425'
                                                  }

responseConfigurarVLAN = requests.request(
                   "GET",
                                 urlConfigurarVLAN,
                                                  params=queryConfigurarVLAN
                                                                   )

#converte resposta em JSON
dataConfigurarVLAN = json.loads(responseConfigurarVLAN.text)

tamanhoConfigurarVLAN=len(dataConfigurarVLAN)
print("Qtd cartões Configurar VLAN:", tamanhoConfigurarVLAN)
file.write("Qtd cartões Configurar VLAN: "+ str(tamanhoConfigurarVLAN)+"\n")
#print(type(dataReservaIP))
#print(dataReservaIP)

########################################conta cartões na lista PABX Virtual###################################
urlPABXVirtual= "https://api.trello.com/1/lists/5f9b27fb6b097138a2f6933f/cards"

queryPABXVirtual = {
                             'key': '8382afbb5d5cc2e3a068dd326fa89f92',
                                                                 'token': '791fde721ccb53158d6c8a10a9199651e18cb7c659972f3beefb247cb4ef5425'
                                                                                                                 }

responsePABXVirtual = requests.request(
                          "GET",
                                                            urlPABXVirtual,
                                                                                                              params=queryPABXVirtual
                                                                                                                                                                                 )

#converte resposta em JSON
dataPABXVirtual = json.loads(responsePABXVirtual.text)

tamanhoPABXVirtual=len(dataPABXVirtual)
print("Qtd cartões PABX Virtual:", tamanhoPABXVirtual)
file.write("Qtd cartões PABX Virtual: "+ str(tamanhoPABXVirtual)+"\n")
#print(type(dataReservaIP))
#print(dataReservaIP)

########################################conta cartões na lista Aguardando Instalação ###################################
urlAguardandoInstalacao= "https://api.trello.com/1/lists/5cb31864557e110b1920d4e1/cards"

queryAguardandoInstalacao = {
                                     'key': '8382afbb5d5cc2e3a068dd326fa89f92',
                                                                                                      'token': '791fde721ccb53158d6c8a10a9199651e18cb7c659972f3beefb247cb4ef5425'
                                                                                                                                                                                                                       }

responseAguardandoInstalacao = requests.request(
                                  "GET",
                                                                                              urlAguardandoInstalacao,
                                                                                                                                                                                                            params=queryAguardandoInstalacao
                                                                                                                                                                                                                                                                                                                                                                                             )

#converte resposta em JSON
dataAguardandoInstalacao = json.loads(responseAguardandoInstalacao.text)

tamanhoAguardandoInstalacao=len(dataAguardandoInstalacao)
print("Qtd cartões Aguardando Instalação:", tamanhoAguardandoInstalacao)
file.write("Qtd cartões Aguardando Instalação: "+ str(tamanhoAguardandoInstalacao)+"\n")
#print(type(dataReservaIP))
#print(dataReservaIP)


########################################conta cartões na lista Solicitar Portabilidade ###################################
urlSolicitarPortabilidade= "https://api.trello.com/1/lists/5cb3186f7cb47f2fc9bbf039/cards"

querySolicitarPortabilidade = {
                                     'key': '8382afbb5d5cc2e3a068dd326fa89f92',
                                                                                                      'token': '791fde721ccb53158d6c8a10a9199651e18cb7c659972f3beefb247cb4ef5425'
                                                                                                                                                                                                                       }

responseSolicitarPortabilidade = requests.request(
                                  "GET",
                                                                                              urlSolicitarPortabilidade,
                                                                                                                                                                                                            params=querySolicitarPortabilidade
                                                                                                                                                                                                                                                                                                                                                                                             )

#converte resposta em JSON
dataSolicitarPortabilidade = json.loads(responseSolicitarPortabilidade.text)

tamanhoSolicitarPortabilidade=len(dataSolicitarPortabilidade)
print("Qtd cartões Solicitar Portabilidade:", tamanhoSolicitarPortabilidade)
file.write("Qtd cartões Solicitar Portabilidade: "+ str(tamanhoSolicitarPortabilidade)+"\n")
#print(type(dataReservaIP))
#print(dataReservaIP)


########################################conta cartões na lista Concluídos ###################################
urlConcluidos= "https://api.trello.com/1/lists/5cb318726982a70a5b3b1bae/cards"

queryConcluidos = {
                                     'key': '8382afbb5d5cc2e3a068dd326fa89f92',
                                                                                                      'token': '791fde721ccb53158d6c8a10a9199651e18cb7c659972f3beefb247cb4ef5425'
                                                                                                                                                                                                                       }

responseConcluidos = requests.request(
                                  "GET",
                                                                                              urlConcluidos,
                                                                                                                                                                                                            params=queryConcluidos
                                                                                                                                                                                                                                                                                                                                                                                             )

#converte resposta em JSON
dataConcluidos = json.loads(responseConcluidos.text)

tamanhoConcluidos=len(dataConcluidos)
print("Qtd cartões Concluídos:", tamanhoConcluidos)
file.write("Qtd cartões Concluídos: "+ str(tamanhoConcluidos)+"\n")
#print(type(dataReservaIP))
#print(dataReservaIP)

########################################conta cartões na lista Standby ###################################
urlStandby= "https://api.trello.com/1/lists/5e8b3d0bf036195154119f01/cards"

queryStandby = {
                                     'key': '8382afbb5d5cc2e3a068dd326fa89f92',
                                                                                                      'token': '791fde721ccb53158d6c8a10a9199651e18cb7c659972f3beefb247cb4ef5425'
                                                                                                                                                                                                                       }

responseStandby = requests.request(
                                  "GET",
                                                                                              urlStandby,
                                                                                                                                                                                                            params=queryStandby
                                                                                                                                                                                                                                                                                                                                                                                             )

#converte resposta em JSON
dataStandby = json.loads(responseStandby.text)

tamanhoStandby=len(dataStandby)
print("Qtd cartões Standby:", tamanhoStandby)
file.write("Qtd cartões Standby: "+ str(tamanhoStandby)+"\n")
#print(type(dataReservaIP))
#print(dataReservaIP)


######################################### TODOS OS CARTOES DO QUADRO #################################

#conta cartões do quadro
urlTotal = "https://api.trello.com/1/boards/TrEzbfJS/cards"

queryTotal = {
                   'key': '8382afbb5d5cc2e3a068dd326fa89f92',
                                 'token': '791fde721ccb53158d6c8a10a9199651e18cb7c659972f3beefb247cb4ef5425'
                                               }

responseTotal = requests.request(
                   "GET",
                                 urlTotal,
                                                  params=queryTotal
                                                                   )

#converte resposta em JSON
dataTotal= json.loads(responseTotal.text)

tamanhoTotal=len(dataTotal)
print("Total de cartões:", tamanhoTotal)
file.write("Total de cartões: "+ str(tamanhoTotal)+"\n")
#print(type(dataTotal))
#print(dataTotal)

