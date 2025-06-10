from typing import List, Dict, Optional, Literal
from pydantic import BaseModel
from enum import Enum


class ContentType(str, Enum):
    EMAIL = "email"
    NEWSLETTER = "newsletter"
    SOCIAL_POST = "social-post"
    ARTICLE = "article"


class Tone(str, Enum):
    PROFESSIONAL = "professional"
    CASUAL = "casual"
    FRIENDLY = "friendly"
    FORMAL = "formal"


class Length(str, Enum):
    SHORT = "short"
    MEDIUM = "medium"
    LONG = "long"


class Language(BaseModel):
    code: str
    name: str
    nativeName: str
    family: str


# All available languages (119+ languages)
AVAILABLE_LANGUAGES = [
    # Indo-European Languages
    Language(code='en', name='English', nativeName='English', family='Indo-European'),
    Language(code='fr', name='French', nativeName='Français', family='Indo-European'),
    Language(code='pt', name='Portuguese', nativeName='Português', family='Indo-European'),
    Language(code='de', name='German', nativeName='Deutsch', family='Indo-European'),
    Language(code='ro', name='Romanian', nativeName='Română', family='Indo-European'),
    Language(code='sv', name='Swedish', nativeName='Svenska', family='Indo-European'),
    Language(code='da', name='Danish', nativeName='Dansk', family='Indo-European'),
    Language(code='bg', name='Bulgarian', nativeName='Български', family='Indo-European'),
    Language(code='ru', name='Russian', nativeName='Русский', family='Indo-European'),
    Language(code='cs', name='Czech', nativeName='Čeština', family='Indo-European'),
    Language(code='el', name='Greek', nativeName='Ελληνικά', family='Indo-European'),
    Language(code='uk', name='Ukrainian', nativeName='Українська', family='Indo-European'),
    Language(code='es', name='Spanish', nativeName='Español', family='Indo-European'),
    Language(code='nl', name='Dutch', nativeName='Nederlands', family='Indo-European'),
    Language(code='sk', name='Slovak', nativeName='Slovenčina', family='Indo-European'),
    Language(code='hr', name='Croatian', nativeName='Hrvatski', family='Indo-European'),
    Language(code='pl', name='Polish', nativeName='Polski', family='Indo-European'),
    Language(code='lt', name='Lithuanian', nativeName='Lietuvių', family='Indo-European'),
    Language(code='nb', name='Norwegian Bokmål', nativeName='Norsk Bokmål', family='Indo-European'),
    Language(code='nn', name='Norwegian Nynorsk', nativeName='Norsk Nynorsk', family='Indo-European'),
    Language(code='fa', name='Persian', nativeName='فارسی', family='Indo-European'),
    Language(code='sl', name='Slovenian', nativeName='Slovenščina', family='Indo-European'),
    Language(code='gu', name='Gujarati', nativeName='ગુજરાતી', family='Indo-European'),
    Language(code='lv', name='Latvian', nativeName='Latviešu', family='Indo-European'),
    Language(code='it', name='Italian', nativeName='Italiano', family='Indo-European'),
    Language(code='oc', name='Occitan', nativeName='Occitan', family='Indo-European'),
    Language(code='ne', name='Nepali', nativeName='नेपाली', family='Indo-European'),
    Language(code='mr', name='Marathi', nativeName='मराठी', family='Indo-European'),
    Language(code='be', name='Belarusian', nativeName='Беларуская', family='Indo-European'),
    Language(code='sr', name='Serbian', nativeName='Српски', family='Indo-European'),
    Language(code='lb', name='Luxembourgish', nativeName='Lëtzebuergesch', family='Indo-European'),
    Language(code='vec', name='Venetian', nativeName='Vèneto', family='Indo-European'),
    Language(code='as', name='Assamese', nativeName='অসমীয়া', family='Indo-European'),
    Language(code='cy', name='Welsh', nativeName='Cymraeg', family='Indo-European'),
    Language(code='szl', name='Silesian', nativeName='Ślōnski', family='Indo-European'),
    Language(code='ast', name='Asturian', nativeName='Asturianu', family='Indo-European'),
    Language(code='hne', name='Chhattisgarhi', nativeName='छत्तीसगढ़ी', family='Indo-European'),
    Language(code='awa', name='Awadhi', nativeName='अवधी', family='Indo-European'),
    Language(code='mai', name='Maithili', nativeName='मैथिली', family='Indo-European'),
    Language(code='bho', name='Bhojpuri', nativeName='भोजपुरी', family='Indo-European'),
    Language(code='sd', name='Sindhi', nativeName='سنڌي', family='Indo-European'),
    Language(code='ga', name='Irish', nativeName='Gaeilge', family='Indo-European'),
    Language(code='fo', name='Faroese', nativeName='Føroyskt', family='Indo-European'),
    Language(code='hi', name='Hindi', nativeName='हिन्दी', family='Indo-European'),
    Language(code='pa', name='Punjabi', nativeName='ਪੰਜਾਬੀ', family='Indo-European'),
    Language(code='bn', name='Bengali', nativeName='বাংলা', family='Indo-European'),
    Language(code='or', name='Oriya', nativeName='ଓଡ଼ିଆ', family='Indo-European'),
    Language(code='tg', name='Tajik', nativeName='Тоҷикӣ', family='Indo-European'),
    Language(code='yi', name='Eastern Yiddish', nativeName='ייִדיש', family='Indo-European'),
    Language(code='lmo', name='Lombard', nativeName='Lumbaart', family='Indo-European'),
    Language(code='lij', name='Ligurian', nativeName='Ligure', family='Indo-European'),
    Language(code='scn', name='Sicilian', nativeName='Sicilianu', family='Indo-European'),
    Language(code='fur', name='Friulian', nativeName='Furlan', family='Indo-European'),
    Language(code='sc', name='Sardinian', nativeName='Sardu', family='Indo-European'),
    Language(code='gl', name='Galician', nativeName='Galego', family='Indo-European'),
    Language(code='ca', name='Catalan', nativeName='Català', family='Indo-European'),
    Language(code='is', name='Icelandic', nativeName='Íslenska', family='Indo-European'),
    Language(code='sq', name='Albanian', nativeName='Shqip', family='Indo-European'),
    Language(code='li', name='Limburgish', nativeName='Limburgs', family='Indo-European'),
    Language(code='prs', name='Dari', nativeName='دری', family='Indo-European'),
    Language(code='af', name='Afrikaans', nativeName='Afrikaans', family='Indo-European'),
    Language(code='mk', name='Macedonian', nativeName='Македонски', family='Indo-European'),
    Language(code='si', name='Sinhala', nativeName='සිංහල', family='Indo-European'),
    Language(code='ur', name='Urdu', nativeName='اردو', family='Indo-European'),
    Language(code='mag', name='Magahi', nativeName='मगही', family='Indo-European'),
    Language(code='bs', name='Bosnian', nativeName='Bosanski', family='Indo-European'),
    Language(code='hy', name='Armenian', nativeName='Հայերեն', family='Indo-European'),

    # Sino-Tibetan Languages
    Language(code='zh', name='Chinese (Simplified)', nativeName='简体中文', family='Sino-Tibetan'),
    Language(code='zh-TW', name='Chinese (Traditional)', nativeName='繁體中文', family='Sino-Tibetan'),
    Language(code='yue', name='Cantonese', nativeName='粵語', family='Sino-Tibetan'),
    Language(code='my', name='Burmese', nativeName='မြန်မာ', family='Sino-Tibetan'),

    # Afro-Asiatic Languages
    Language(code='ar', name='Arabic (Standard)', nativeName='العربية', family='Afro-Asiatic'),
    Language(code='ar-SA', name='Arabic (Najdi)', nativeName='العربية النجدية', family='Afro-Asiatic'),
    Language(code='ar-LB', name='Arabic (Levantine)', nativeName='العربية الشامية', family='Afro-Asiatic'),
    Language(code='ar-EG', name='Arabic (Egyptian)', nativeName='العربية المصرية', family='Afro-Asiatic'),
    Language(code='ar-MA', name='Arabic (Moroccan)', nativeName='العربية المغربية', family='Afro-Asiatic'),
    Language(code='ar-IQ', name='Arabic (Mesopotamian)', nativeName='العربية العراقية', family='Afro-Asiatic'),
    Language(code='ar-YE', name='Arabic (Ta\'izzi-Adeni)', nativeName='العربية اليمنية', family='Afro-Asiatic'),
    Language(code='ar-TN', name='Arabic (Tunisian)', nativeName='العربية التونسية', family='Afro-Asiatic'),
    Language(code='he', name='Hebrew', nativeName='עברית', family='Afro-Asiatic'),
    Language(code='mt', name='Maltese', nativeName='Malti', family='Afro-Asiatic'),

    # Austronesian Languages
    Language(code='id', name='Indonesian', nativeName='Bahasa Indonesia', family='Austronesian'),
    Language(code='ms', name='Malay', nativeName='Bahasa Melayu', family='Austronesian'),
    Language(code='tl', name='Tagalog', nativeName='Tagalog', family='Austronesian'),
    Language(code='ceb', name='Cebuano', nativeName='Cebuano', family='Austronesian'),
    Language(code='jv', name='Javanese', nativeName='Basa Jawa', family='Austronesian'),
    Language(code='su', name='Sundanese', nativeName='Basa Sunda', family='Austronesian'),
    Language(code='min', name='Minangkabau', nativeName='Baso Minangkabau', family='Austronesian'),
    Language(code='ban', name='Balinese', nativeName='Basa Bali', family='Austronesian'),
    Language(code='bjn', name='Banjar', nativeName='Bahasa Banjar', family='Austronesian'),
    Language(code='pag', name='Pangasinan', nativeName='Salitan Pangasinan', family='Austronesian'),
    Language(code='ilo', name='Iloko', nativeName='Pagsasao nga Ilokano', family='Austronesian'),
    Language(code='war', name='Waray', nativeName='Winaray', family='Austronesian'),

    # Dravidian Languages
    Language(code='ta', name='Tamil', nativeName='தமிழ்', family='Dravidian'),
    Language(code='te', name='Telugu', nativeName='తెలుగు', family='Dravidian'),
    Language(code='kn', name='Kannada', nativeName='ಕನ್ನಡ', family='Dravidian'),
    Language(code='ml', name='Malayalam', nativeName='മലയാळം', family='Dravidian'),

    # Turkic Languages
    Language(code='tr', name='Turkish', nativeName='Türkçe', family='Turkic'),
    Language(code='az', name='Azerbaijani', nativeName='Azərbaycan', family='Turkic'),
    Language(code='uz', name='Uzbek', nativeName='Oʻzbek', family='Turkic'),
    Language(code='kk', name='Kazakh', nativeName='Қазақша', family='Turkic'),
    Language(code='ba', name='Bashkir', nativeName='Башҡорт', family='Turkic'),
    Language(code='tt', name='Tatar', nativeName='Татар', family='Turkic'),

    # Tai-Kadai Languages
    Language(code='th', name='Thai', nativeName='ไทย', family='Tai-Kadai'),
    Language(code='lo', name='Lao', nativeName='ລາວ', family='Tai-Kadai'),

    # Uralic Languages
    Language(code='fi', name='Finnish', nativeName='Suomi', family='Uralic'),
    Language(code='et', name='Estonian', nativeName='Eesti', family='Uralic'),
    Language(code='hu', name='Hungarian', nativeName='Magyar', family='Uralic'),

    # Austroasiatic Languages
    Language(code='vi', name='Vietnamese', nativeName='Tiếng Việt', family='Austroasiatic'),
    Language(code='km', name='Khmer', nativeName='ខ្មែរ', family='Austroasiatic'),

    # Other Languages
    Language(code='ja', name='Japanese', nativeName='日本語', family='Japonic'),
    Language(code='ko', name='Korean', nativeName='한국어', family='Koreanic'),
    Language(code='ka', name='Georgian', nativeName='ქართული', family='Kartvelian'),
    Language(code='eu', name='Basque', nativeName='Euskera', family='Language Isolate'),
    Language(code='ht', name='Haitian', nativeName='Kreyòl Ayisyen', family='Creole'),
    Language(code='pap', name='Papiamento', nativeName='Papiamentu', family='Creole'),
    Language(code='kea', name='Kabuverdianu', nativeName='Kriolu', family='Creole'),
    Language(code='tpi', name='Tok Pisin', nativeName='Tok Pisin', family='Creole'),
    Language(code='sw', name='Swahili', nativeName='Kiswahili', family='Niger-Congo'),
]

# Create languages by family mapping
LANGUAGES_BY_FAMILY: Dict[str, List[Language]] = {}
for lang in AVAILABLE_LANGUAGES:
    if lang.family not in LANGUAGES_BY_FAMILY:
        LANGUAGES_BY_FAMILY[lang.family] = []
    LANGUAGES_BY_FAMILY[lang.family].append(lang)


class GenerationRequest(BaseModel):
    prompt: str
    contentType: ContentType
    targetLanguages: List[str]
    sourceLanguage: Optional[str] = "en"
    tone: Optional[Tone] = Tone.PROFESSIONAL
    length: Optional[Length] = Length.MEDIUM


class ContentMetadata(BaseModel):
    wordCount: int
    characterCount: int
    estimatedReadingTime: int


class GeneratedContent(BaseModel):
    language: str
    content: str
    metadata: Optional[ContentMetadata] = None


class GenerationResponse(BaseModel):
    originalContent: GeneratedContent
    translations: List[GeneratedContent]
    totalTokensUsed: Optional[int] = None
    processingTime: int


class GroqConfig(BaseModel):
    apiKey: str
    model: str 
    maxTokens: Optional[int]
    temperature: Optional[float]


class AIAgentError(Exception):
    def __init__(self, error_type: str, message: str, details: Optional[dict] = None):
        self.type = error_type
        self.message = message
        self.details = details or {}
        super().__init__(self.message)


def get_language_by_code(code: str) -> Optional[Language]:
    """Get language by code"""
    for lang in AVAILABLE_LANGUAGES:
        if lang.code == code:
            return lang
    return None


def validate_language_codes(codes: List[str]) -> Dict[str, List[str]]:
    """Validate language codes and return valid/invalid lists"""
    valid = []
    invalid = []
    
    for code in codes:
        if get_language_by_code(code):
            valid.append(code)
        else:
            invalid.append(code)
    
    return {"valid": valid, "invalid": invalid} 