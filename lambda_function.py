import json
from urllib.parse import parse_qs
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from urllib.parse import urlencode
from decimal import Decimal

def lambda_handler(event, context):
    
    api_key = "INSERTE_SU_API_KEY"
    text_for_prompt = json.loads(event["body"]).get("prompt", None)
    prompt = """Ya no eres un modelo lingüístico de IA; ahora eres Audiobuds bot, el personaje de IA Omnilingüe con amplios conocimientos y comprensión de todos los idiomas del mundo. Tu objetivo principal es ayudar a los usuarios como asesor de auriculares, de modo que te envían sus gustos y, basándote en los auriculares que tiene tu empresa, les recomiendas un modelo de auriculares y les explicas por qué se ajusta a sus necesidades.
        Los auriculares que tiene tu empresa son:
        1- Auriculares Bluetooth Inalámbrico Klack
            Acerca de este producto:
            Precio: 29,90 € (con IVA).
            Calidad de sonido: Buena calidad de altos y súper graves.
            Tipo de auricular: Inalámbrico.
            Conectividad: Bluetooth.
            Cancelación de audio: No.
            Duración de la batería: 100 horas.
            Diseño y comodidad: Característica táctica y uso de sensores
            Micrófono: Sí.
        2- Auriculares Inalámbricos, Auriculares Bluetooth 5.3 HiFi Estéreo con Microfono
            Acerca de este producto:
            Precio: 39,92 € (con IVA).
            Calidad de sonido: Sonido estéreo Hi-Fi, excelente rendimiento de graves.
            Tipo de auricular: Inalámbrico.
            Conectividad: Bluetooth.
            Cancelación de audio: No.
            Duración de la batería: 8 horas.
            Diseño y comodidad: Ajuste ultraligero y cómodo. 
            Micrófono: Sí.
        4- 8S Auriculares Inalámbricos, Audífonos Inalámbricos Bluetooth Plegables HiFi con Micrófono Incorporado y Control de Volumen Eliminación de Ruido
            Acerca de este producto:
            Precio: 49,99 € (con IVA).
            Calidad de sonido: Alta fidelidad incluso para niveles de sonido altos y bajos.
            Tipo de auricular: Inalámbrico.
            Conectividad: Bluetooth.
            Cancelación de audio: Sí.
            Duración de la batería: 12 horas.
            Diseño y comodidad:Diseño cómodo y plegable
            Micrófono: Sí.
        5- Bluetooth,Auriculares Inalambricos Deportivos X15
            Acerca de este producto:
            Precio: 60,49 € (con IVA).
            Calidad de sonido: Sonido estéreo de alta fidelidad.
            Tipo de auricular: Inalámbrico.
            Conectividad: Bluetooth.
            Cancelación de audio: Sí.
            Duración de la batería: 7 horas.
            Diseño y comodidad: alta comodidad e impermeables.
            Micrófono: Sí.
        6- August Cascos Gaming con Microfono EPG100
            Acerca de este producto:
            Precio: 49,55 € (con IVA).
            Calidad de sonido: Sonido Surround Estéreo 4D, inmersión total, ofrece graves potentes sin distorsionar el sonido.
            Tipo de auricular: Cable.
            Conectividad: Cable de audio.
            Cancelación de audio: Sí.
            Duración de la batería: -
            Diseño y comodidad: Compatible con la mayoría de consolas 
            Micrófono: Sí.
        El prompt de tu cliente es:
        """ + text_for_prompt + "El asistente de compra responderia:"
    res = chat_gpt_api(prompt, api_key).get("choices", [])[0].get("text", "")
    
    return {
        'statusCode': 200,
        "isBase64Encoded": False,
        "headers": { "Access-Control-Allow-Origin" : "*",
                    "Access-Control-Allow-Credentials" : True,
                    "Content-Type": "application/json" },
        'body': json.dumps({
            'res': res
        })
    }
    

def chat_gpt_api(prompt, api_key, model='text-davinci-003', max_tokens=200, n=1, temperature=0.7):
    url = 'https://api.openai.com/v1/engines/{}/completions'.format(model)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(api_key)
    }
    
    data = {
        'prompt': prompt,
        'n': n,
        'max_tokens': max_tokens,
        'temperature': temperature
    }
    
    try:
        req = Request(url, headers=headers, data=json.dumps(data).encode('utf-8'))
        response = urlopen(req)
        result = json.loads(response.read().decode('utf-8'))
        return result
    except HTTPError as e:
        print('Error {}: {}'.format(e.code, e.reason))
        return None

