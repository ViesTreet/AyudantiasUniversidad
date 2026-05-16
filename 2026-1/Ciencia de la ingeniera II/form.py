import requests
import pandas as pd
import random
import time
from bs4 import BeautifulSoup

# ================= CONFIGURACIÓN =================
CSV_FILENAME = 'Encuesta-Proyecto-USM-_Respuestas_.csv'
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfsQX3etghfflwnvbAbdLmHXeCIVdGQDrHDUQazOAGJ6F52UQ"
CANTIDAD_A_ENVIAR = 50  # Cuántas respuestas falsas quieres agregar
# =================================================

def cargar_datos_base():
    try:
        df = pd.read_csv(CSV_FILENAME, encoding='utf-8-sig', sep=',')
        df = df.fillna('')  # Limpiar valores nulos
        return df
    except Exception as e:
        print(f"❌ Error leyendo el CSV: {e}")
        return None

def enviar_respuesta(session, df):
    # 1. Seleccionar una respuesta al azar del CSV para mantener porcentajes
    fila = df.sample(n=1).iloc[0]

    # 2. GET request para obtener las Cookies y el token FBZX dinámico
    print("Obteniendo sesión y tokens...")
    headers_get = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
    }
    res_get = session.get(f"{FORM_URL}/viewform", headers=headers_get)
    soup = BeautifulSoup(res_get.text, 'html.parser')
    fbzx_input = soup.find('input', {'name': 'fbzx'})

    if not fbzx_input:
        print("❌ No se pudo extraer el token fbzx. Google puede haber bloqueado la IP temporalmente.")
        return False

    fbzx_token = fbzx_input['value']

    # 3. Mapear los datos de la fila a los IDs del formulario
    # Índices de columna basados en el CSV proporcionado
    payload = {
        # Página 1 (Datos básicos)
        "entry.1668422516": fila.iloc[1],   # 1.1 Edad
        "entry.1396812382": fila.iloc[2],   # 1.2 Género
        "entry.1383407662": fila.iloc[3],   # 1.3 Rol principal
        "entry.925890645": fila.iloc[4],    # 1.4 Años experiencia
        "entry.921166642": fila.iloc[5],    # 1.5 Personas en cuadrilla
        "entry.407700716": fila.iloc[6],    # 1.6 Comuna

        # Página 2 (Educación y manejo)
        "entry.718735920": fila.iloc[7],    # 2.1 Nivel educativo
        "entry.816936009": fila.iloc[8],    # 2.2 Manejo apps
        "entry.296820602": fila.iloc[9],    # 2.3 Tipo contrato
        "entry.1652705685": fila.iloc[10],  # 2.4 Tiempo en empresa
        "entry.1796977190": fila.iloc[11],  # 2.5 Permiten WhatsApp

        # Página 3 (Dispositivos y conectividad)
        "entry.1949338639": fila.iloc[12],  # 3.1 Dispositivo principal
        "entry.954805787": fila.iloc[13],   # 3.2 Conectividad
        "entry.1937541358": fila.iloc[14],  # 3.3 Frecuencia uso apps
        "entry.1504304917": fila.iloc[15],  # 3.4 Puede enviar foto

        # Página 4 (Problemas en obra)
        "entry.1711344162": fila.iloc[19],  # 4.3 Tiempo perdido esperando
        "entry.1828751822": fila.iloc[20],  # 4.4 Claridad estado solicitud
        "entry.1228197241": fila.iloc[21],  # 4.5 Frecuencia materiales incorrectos
        "entry.1494056156": fila.iloc[22],  # 4.6 Claridad materiales urgentes
        "entry.1438714850": fila.iloc[23],  # 4.7 Frecuencia rehacer solicitudes
        "entry.1703612607": fila.iloc[24],  # 4.8 Orden llegada materiales
        "entry.926096833": fila.iloc[25],   # 4.9 Dónde ocurren más problemas

        # Página 5 (Utilidad del sistema)
        "entry.1536989645": fila.iloc[26],  # 5.1 Utilidad lista prioridad
        "entry.2027537068": fila.iloc[27],  # 5.2 Utilidad ver estado
        "entry.903607668": fila.iloc[28],   # 5.3 Utilidad confirmación entrega
        "entry.2008359880": fila.iloc[31],  # 5.6 Usaría sistema
        "entry.578449968": fila.iloc[32],   # 5.7 Preferiría sobre papel
        "entry.1173854916": fila.iloc[33],  # 5.8 Dificultad uso digital
        "entry.955921105": fila.iloc[34],   # 5.9 Dispuesto a participar piloto

        # Metadatos del form
        "fvv": "1",
        "pageHistory": "0,1,2,3,4,5",
        "fbzx": fbzx_token,
        "submissionTimestamp": str(int(time.time() * 1000))  # Timestamp actual
    }

    # Convertir payload a lista de tuplas para permitir claves duplicadas (múltiples entradas)
    datos_post = list(payload.items())

    # Procesar preguntas de opción múltiple (checkboxes) que pueden tener varias respuestas separadas por coma
    # 3.5 Problemas técnicos (col 16)
    tecnicos = str(fila.iloc[16])
    if tecnicos:
        for opcion in tecnicos.split(','):
            datos_post.append(("entry.939680223", opcion.strip()))

    # 4.1 Factores impacto retrasos (col 17) - máximo 2
    factores = str(fila.iloc[17])
    if factores:
        for opcion in factores.split(',')[:2]:
            datos_post.append(("entry.1773528744", opcion.strip()))

    # 4.2 Qué ocurre cuando material no llega (col 18) - máximo 2
    ocurre = str(fila.iloc[18])
    if ocurre:
        for opcion in ocurre.split(',')[:2]:
            datos_post.append(("entry.1086763967", opcion.strip()))

    # 5.4 Problema más importante resolver (col 29) - máximo 2
    problema = str(fila.iloc[29])
    if problema:
        for opcion in problema.split(',')[:2]:
            datos_post.append(("entry.2137179734", opcion.strip()))

    # 5.5 Lo más valioso del sistema (col 30) - máximo 2 (aunque normalmente es uno)
    valioso = str(fila.iloc[30])
    if valioso:
        for opcion in valioso.split(',')[:2]:
            datos_post.append(("entry.1990634278", opcion.strip()))

    # 4. Enviar el POST Final
    headers_post = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": f"{FORM_URL}/formResponse",
        "Origin": "https://docs.google.com",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    res_post = session.post(f"{FORM_URL}/formResponse", data=datos_post, headers=headers_post)

    if res_post.status_code == 200:
        print(f"✅ ¡Respuesta enviada con éxito! (Status: {res_post.status_code})")
        return True
    else:
        print(f"❌ Error al enviar. Status: {res_post.status_code} - Razón: {res_post.reason}")
        return False

def main():
    print("Iniciando escalado de respuestas...")
    df = cargar_datos_base()
    if df is None:
        return

    exitos = 0
    session = requests.Session()

    for i in range(CANTIDAD_A_ENVIAR):
        print(f"\n--- Intentando envío {i+1} de {CANTIDAD_A_ENVIAR} ---")
        if enviar_respuesta(session, df):
            exitos += 1

            # Espera aleatoria para simular comportamiento humano
            delay = random.uniform(12.5, 45.3)
            print(f"Esperando {delay:.2f} segundos para evadir el anti-bot...")
            time.sleep(delay)

            # Refrescar sesión cada 5 envíos
            if exitos % 5 == 0:
                print("Refrescando sesión de red...")
                session = requests.Session()
        else:
            print("Deteniendo el script para evitar bloqueo de IP.")
            break

    print(f"\n🏁 Proceso finalizado. Se enviaron {exitos} respuestas de forma exitosa.")

if __name__ == "__main__":
    main()