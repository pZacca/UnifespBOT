import tweepy  # Need to install
import datetime as dt

'''
For any suggestions or contact, mail me at pedrozaccaria@gmail.com
https://github.com/pZacca/Python_pZacca/tree/master/Conjunto
https://twitter.com/UnifespBot
'''
# Credentials and Token info
auth = tweepy.OAuth1UserHandler(
   "Chave API", "Chave API Secreta",
   "Token de Acesso", "Token de Acesso Secreto"
)
api = tweepy.API(auth)
# Dates and date calculation (delta)
inicio_veteranos = dt.date(2022, 4, 6)
inicio_calouros = dt.date(2022, 4, 11)
hoje = dt.date.today()
delta_veteranos = inicio_veteranos - hoje
delta_calouros = inicio_calouros - hoje
# Tweet structure
msg = '🚨 CONTAGEM REGRESSIVA PRAS AULAS 🚨\n'

if delta_veteranos.days > 1:
    msg += f'VETERANOS: {delta_veteranos.days} Dias\n'
elif delta_veteranos.days == 1:
    msg += f'VETERANOS: Começam amanhã 😳\n'
else:
    msg += 'VETERANOS: AS AULAS COMEÇARAM! 🥳\n'

if delta_calouros.days > 1:
    msg += f'CALOUROS: {delta_calouros.days} Dias'
elif delta_calouros.days == 1:
    msg += f'CALOUROS: Começam amanhã 😳'
else:
    msg = '🚨 AS AULAS DA UNIFESP COMEÇARAM PARA VETERANOS E CALOUROS! 🚨\n' \
          'Boa sorte a todos, obrigado por terem acompanhado o Bot!\n' \
          'Por enquanto o Bot será desativado :(\n' \
          'Ideias e sugestões do que fazer agora são bem-vindas.'

# Tweet publishing
api.update_status(status=msg)
