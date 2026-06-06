from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse
import json
import re

HOST = '127.0.0.1'
PORT = 8080
PROJECT_DIR = Path(__file__).resolve().parent
STATIC_DIR = PROJECT_DIR / 'static'
TRANSLATION_PATTERN = re.compile(r'translate\s+"?(?P<phrase>.+?)"?\s+to\s+(?P<language>[a-zA-Z]+)', re.I)

PHRASEBOOK = {
    'English': {
        'hello': 'Hello',
        'thank you': 'Thank you',
        'where is': 'Where is {place}?',
        'help': 'Help',
        'emergency': 'Emergency',
        'please': 'Please',
        'good morning': 'Good morning',
        'goodbye': 'Goodbye',
    },
    'Hindi': {
        'hello': 'नमस्ते',
        'thank you': 'धन्यवाद',
        'where is': '{place} कहाँ है?',
        'help': 'मदद',
        'emergency': 'आपातकाल',
        'please': 'कृपया',
        'good morning': 'सुप्रभात',
        'goodbye': 'अलविदा',
    },
    'Bengali': {
        'hello': 'নমস্কার',
        'thank you': 'ধন্যবাদ',
        'where is': '{place} কোথায়?',
        'help': 'সাহায্য',
        'emergency': 'জরুরি',
        'please': 'অনুগ্রহ করে',
        'good morning': 'শুভ সকাল',
        'goodbye': 'বিদায়',
    },
    'Gujarati': {
        'hello': 'નમસ્તે',
        'thank you': 'ધન્યવાદ',
        'where is': '{place} ક્યાં છે?',
        'help': 'મદત',
        'emergency': 'આપાતકાલીન',
        'please': 'કૃપા કરીને',
        'good morning': 'સુપ્રભાત',
        'goodbye': 'અલવિદા',
    },
    'Marathi': {
        'hello': 'नमस्कार',
        'thank you': 'धन्यवाद',
        'where is': '{place} कुठे आहे?',
        'help': 'मदत',
        'emergency': 'आपत्कालीन',
        'please': 'कृपया',
        'good morning': 'शुभ प्रभात',
        'goodbye': 'नमस्कार',
    },
    'Punjabi': {
        'hello': 'ਸਤ ਸ੍ਰੀ ਅਕਾਲ',
        'thank you': 'ਧੰਨਵਾਦ',
        'where is': '{place} ਕਿੱਥੇ ਹੈ?',
        'help': 'ਮਦਦ',
        'emergency': 'ਤਤਕਾਲ',
        'please': 'ਕਿਰਪਾ ਕਰਕੇ',
        'good morning': 'ਸ਼ੁਭ ਸਵੇਰ',
        'goodbye': 'ਅਲਵਿਦਾ',
    },
    'Tamil': {
        'hello': 'வணக்கம்',
        'thank you': 'நன்றி',
        'where is': '{place} எங்கு உள்ளது?',
        'help': 'உதவி',
        'emergency': 'அவசரம்',
        'please': 'தயவு செய்து',
        'good morning': 'காலை வணக்கம்',
        'goodbye': 'பிரியாவிடை',
    },
    'Telugu': {
        'hello': 'నమస్కారం',
        'thank you': 'ధన్యవాదాలు',
        'where is': '{place} ఎక్కడ ఉంది?',
        'help': 'సహాయం',
        'emergency': 'అత్యవసర పరిస్థితి',
        'please': 'దయచేసి',
        'good morning': 'శుభోదయం',
        'goodbye': 'వీడ్కోలు',
    },
    'Malayalam': {
        'hello': 'നമസ്കാരം',
        'thank you': 'നന്ദി',
        'where is': '{place} എവിടെയാണ്?',
        'help': 'സഹായം',
        'emergency': 'അപകടം',
        'please': 'ദയവായി',
        'good morning': 'സുപ്രഭാതം',
        'goodbye': 'വിട',
    },
    'Kannada': {
        'hello': 'ನಮಸ್ಕಾರ',
        'thank you': 'ಧನ್ಯವಾದಗಳು',
        'where is': '{place} ಎಲ್ಲಿದೆ?',
        'help': 'ಸಹಾಯ',
        'emergency': 'ತುರ್ತು',
        'please': 'ದಯವಿಟ್ಟು',
        'good morning': 'ಶುಭೋದಯ',
        'goodbye': 'ವಿದಾಯ',
    },
    'French': {
        'hello': 'Bonjour',
        'thank you': 'Merci',
        'where is': 'Où est {place}?',
        'help': 'Aide',
        'emergency': 'Urgence',
        'please': "S'il vous plaît",
        'good morning': 'Bonjour',
        'goodbye': 'Au revoir',
    },
    'Japanese': {
        'hello': 'こんにちは',
        'thank you': 'ありがとうございます',
        'where is': '{place}はどこですか?',
        'help': '助けて',
        'emergency': '緊急',
        'please': 'お願いします',
        'good morning': 'おはようございます',
        'goodbye': 'さようなら',
    },
    'German': {
        'hello': 'Hallo',
        'thank you': 'Danke',
        'where is': 'Wo ist {place}?',
        'help': 'Hilfe',
        'emergency': 'Notfall',
        'please': 'Bitte',
        'good morning': 'Guten Morgen',
        'goodbye': 'Auf Wiedersehen',
    },
}

KNOWLEDGE = {
    'navigation': [
        'The main bathing area at Mahakumbh is arranged along the riverbank. Follow the signboards for the main gate and use the shuttle service from Gate 3 to reach the festival grounds.',
        'Public transport is available from Haridwar station, Rishikesh, and Dehradun. Auto-rickshaws and authorized taxis are best for short connections inside the city.',
    ],
    'events': [
        'Event highlights include the Shahi Snan (royal bath), cultural programs, spiritual discussions, and daily aarti at sunrise and sunset.',
        'Key ritual timings: Morning aarti at 6:00 AM, evening aarti at 7:00 PM and special seminars from 10:00 AM to 1:00 PM.',
    ],
    'accommodation': [
        'Pilgrim accommodation is available in arranged tents, dharamshalas, and authorised guest houses near the river. Book early for official camp zones A, B, and C to stay close to the main site.',
        'For budget stays, check the government pilgrim camps and authorised guest houses near Harki Puri and Har Ki Pauri.',
    ],
    'services': [
        'Local services include first-aid centres, lost-and-found counters, information booths, food stalls, and charging stations across the festival area.',
        'Look for the blue information helpdesks marked with the pilgrim support logo for directions, medical assistance, and transport advice.',
    ],
    'women_help': [
        'For women-specific assistance, call 1091, the women’s helpline at the Mahakumbh site.',
    ],
    'emergency': [
        'Emergency support: call 100 for police, 102 for ambulance, and 108 for disaster rescue. Locate the nearest first-aid centre or ask a volunteer for immediate assistance.',
        'If you are lost, stay near an information kiosk or speak with an authorised volunteer wearing a yellow badge.',
    ],
    'faq': [
        'Q: How do I find the nearest water station? A: Follow the blue water signs or ask a nearby volunteer. Water stations are available every 500 metres.',
        'Q: Can I charge my phone? A: Yes, there are charging tents and power kiosks in the main camp zones. Use authorised charging stalls only.',
        'Q: What should I carry? A: Carry your ID, water bottle, comfortable footwear, sunscreen, and a portable charger.',
    ],
}

COMMON_PATTERNS = {
    'women_help': ['women helpline', 'women help', '1091', 'ladies helpline', 'women emergency'],
    'emergency': ['emergency', 'ambulance', 'police', 'urgent'],
    'events': ['event', 'schedule', 'program', 'aarti', 'snan', 'time', 'timing'],
    'accommodation': ['stay', 'hotel', 'accommodation', 'camp', 'sleep', 'room'],
    'navigation': ['where', 'direction', 'how to reach', 'route', 'gate'],
    'services': ['service', 'medical', 'charger', 'food', 'lost'],
    'translate': ['translate', 'say', 'how to say', 'phrase', 'language'],
    'faq': ['faq', 'question', 'answer', 'common', 'know'],
}

AVAILABLE_LANGUAGES = [
    'English', 'Hindi', 'Bengali', 'Gujarati', 'Marathi', 'Punjabi', 'Tamil',
    'Telugu', 'Malayalam', 'Kannada', 'French', 'Japanese', 'German'
]


def parse_translation_request(query: str) -> tuple[str, str] | None:
    match = TRANSLATION_PATTERN.search(query)
    if not match:
        return None
    phrase = match.group('phrase').strip().lower()
    target = match.group('language').strip().title()
    return phrase, target


def build_translation(query: str, target_language: str) -> str:
    parsed = parse_translation_request(query)
    if parsed is not None:
        phrase, raw_target = parsed
        if raw_target not in AVAILABLE_LANGUAGES:
            return f'Sorry, translation into {raw_target} is not available yet.'
        target_language = raw_target
    else:
        phrase = query.lower().strip()

    if target_language not in PHRASEBOOK:
        return f'Sorry, translation into {target_language} is not available yet.'

    if 'where is' in phrase:
        place = phrase.split('where is')[-1].strip(' ?') or 'place'
        template = PHRASEBOOK[target_language].get('where is')
        return template.format(place=place)

    for key in ['hello', 'thank you', 'please', 'good morning', 'goodbye', 'help', 'emergency']:
        if key in phrase:
            return PHRASEBOOK[target_language][key]

    return (
        'I can translate a few useful phrases. Try: "hello", "thank you", "please", "where is the medical camp", or "good morning".'
    )


def choose_answer(message: str, language: str) -> str:
    text = message.lower().strip()
    if not text:
        return 'Please type a question or choose one of the example prompts to continue.'

    for topic, keywords in COMMON_PATTERNS.items():
        if any(k in text for k in keywords):
            if topic == 'translate':
                return build_translation(text, language)
            if topic in KNOWLEDGE:
                answer = KNOWLEDGE[topic][0]
                if len(KNOWLEDGE[topic]) > 1:
                    return f"{answer}\n\nAlso: {KNOWLEDGE[topic][1]}"
                return answer

    return (
        'Sorry, I did not understand that question. '
        'Please ask about navigation, event timings, emergency support, accommodation, local services, or translation. '
        'For example: "Where is the main gate?", "Translate thank you to Hindi", or "What are the event timings?"'
    )


def normalize_language(code: str) -> str:
    if not code:
        return 'English'
    normalized = code.strip().title()
    return normalized if normalized in AVAILABLE_LANGUAGES else 'English'


class PilgrimAssistantHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(STATIC_DIR), **kwargs)

    def do_GET(self):
        if self.path in ('/', '/index.html'):
            self.path = '/index.html'
        return super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path == '/api/chat':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length).decode('utf-8')
            try:
                data = json.loads(body)
            except json.JSONDecodeError:
                self.send_response(400)
                self.end_headers()
                return

            message = data.get('message', '')
            language = normalize_language(data.get('language', 'English'))
            answer = choose_answer(message, language)
            response = {
                'reply': answer,
                'language': language,
                'request': message,
            }
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()


def run_server(host=HOST, port=PORT):
    server_address = (host, port)
    httpd = ThreadingHTTPServer(server_address, PilgrimAssistantHandler)
    print(f'Pilgrim Assistant running at http://{host}:{port}')
    print('Open the URL in your browser and type a question or ask for a translation.')
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()
