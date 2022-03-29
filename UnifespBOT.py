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
inicio_calouros = dt.date(2022, 4, 11)
inicio_veteranos = dt.date(2022, 4, 6)
hoje = dt.date.today()
delta_calouros = inicio_calouros - hoje
delta_veteranos = inicio_veteranos - hoje

# Tweet structure
if delta_veteranos.days > 1:
    msg = f'Faltam {delta_veteranos.days} dias para o início das aulas dos veteranos e '
elif delta_veteranos.days == 1:
    msg = f'Falta um dia para o início das aulas dos veteranos e '
else:
    msg = 'As aulas dos veteranos começaram e '

if delta_calouros.days > 1:
    msg += f'faltam {delta_calouros.days} dias para o início das aulas dos calouros.'
elif delta_calouros.days == 1:
    msg += f'falta um dia para o início das aulas dos calouros.'
else:
    msg += 'as aulas dos calouros começaram!'

# Tweet publishing
api.update_status(status=msg)
