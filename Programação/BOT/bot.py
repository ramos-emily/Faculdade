import requests
import datetime
import random
import unicodedata
from telegram.ext import ApplicationBuilder, MessageHandler, filters

def limpar(texto):
    texto = texto.lower()
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

def get_pokemon_info(identifier):
    url = f"https://pokeapi.co/api/v2/pokemon/{identifier}"
    r = requests.get(url)
    if r.status_code != 200:
        return None
    data = r.json()
    nome = data["name"]
    tipos = ", ".join([t["type"]["name"] for t in data["types"]])
    altura = data["height"]
    peso = data["weight"]
    img = data["sprites"]["other"]["official-artwork"]["front_default"]
    return nome, data["id"], tipos, altura, peso, img

def get_pokemon_name_in_message(msg):
    palavras = msg.split()
    for p in palavras:
        url = f"https://pokeapi.co/api/v2/pokemon/{p}"
        r = requests.get(url)
        if r.status_code == 200:
            return p
    return None

def get_evolution_chain(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}"
    r = requests.get(url)
    if r.status_code != 200:
        return None
    evo_url = r.json()["evolution_chain"]["url"]
    chain = requests.get(evo_url).json()["chain"]
    result = []
    atual = chain
    while True:
        result.append(atual["species"]["name"])
        if len(atual["evolves_to"]) == 0:
            break
        atual = atual["evolves_to"][0]
    return result

async def responder(update, context):
    msg_raw = update.message.text
    msg = limpar(msg_raw)

    if "pokemon do dia" in msg:
        hoje = datetime.date.today()
        random.seed(hoje.toordinal())
        n = random.randint(1, 1025)
        info = get_pokemon_info(n)
        if not info:
            await update.message.reply_text("Erro ao buscar Pokémon.")
            return
        nome, pid, tipos, altura, peso, img = info
        texto = f"Pokémon do dia:\nNome: {nome}\nID: {pid}\nTipos: {tipos}\nAltura: {altura}\nPeso: {peso}"
        await update.message.reply_photo(photo=img, caption=texto)
        return

    if "pokemon numero" in msg or "numero do pokemon" in msg:
        nums = [int(s) for s in msg.split() if s.isdigit()]
        if not nums:
            await update.message.reply_text("Não encontrei o número na frase.")
            return
        info = get_pokemon_info(nums[0])
        if not info:
            await update.message.reply_text("Pokémon não encontrado.")
            return
        nome, pid, tipos, altura, peso, img = info
        texto = f"Nome: {nome}\nID: {pid}\nTipos: {tipos}\nAltura: {altura}\nPeso: {peso}"
        await update.message.reply_photo(photo=img, caption=texto)
        return

    if "evolucao" in msg or "evolucao de" in msg or "evolucao do" in msg or "evolucao da" in msg:
        nome = get_pokemon_name_in_message(msg)
        if not nome:
            await update.message.reply_text("Não consegui identificar o Pokémon na frase.")
            return
        cadeia = get_evolution_chain(nome)
        if not cadeia:
            await update.message.reply_text("Não encontrei a linha evolutiva.")
            return
        texto = " → ".join(cadeia)
        await update.message.reply_text(f"Evolução: {texto}")
        return

    await update.message.reply_text(
        "Exemplos:\n"
        "- Qual o Pokémon do dia?\n"
        "- Qual o Pokémon número 25?\n"
        "- Qual a evolução do Bulbasaur?"
    )

TOKEN = "8192056590:AAHBV-5Dnz63F9BL0BeugFbZaeVInwuvtHY"

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
app.run_polling()
