export type ContentType = 'email' | 'newsletter' | 'social-post' | 'article';


export interface Language {
  code: string;
  name: string;
  nativeName: string;
  family: string;
}


export const AVAILABLE_LANGUAGES: Language[] = [
  // Indo-European Languages
  { code: 'en', name: 'English', nativeName: 'English', family: 'Indo-European' },
  { code: 'fr', name: 'French', nativeName: 'Français', family: 'Indo-European' },
  { code: 'pt', name: 'Portuguese', nativeName: 'Português', family: 'Indo-European' },
  { code: 'de', name: 'German', nativeName: 'Deutsch', family: 'Indo-European' },
  { code: 'ro', name: 'Romanian', nativeName: 'Română', family: 'Indo-European' },
  { code: 'sv', name: 'Swedish', nativeName: 'Svenska', family: 'Indo-European' },
  { code: 'da', name: 'Danish', nativeName: 'Dansk', family: 'Indo-European' },
  { code: 'bg', name: 'Bulgarian', nativeName: 'Български', family: 'Indo-European' },
  { code: 'ru', name: 'Russian', nativeName: 'Русский', family: 'Indo-European' },
  { code: 'cs', name: 'Czech', nativeName: 'Čeština', family: 'Indo-European' },
  { code: 'el', name: 'Greek', nativeName: 'Ελληνικά', family: 'Indo-European' },
  { code: 'uk', name: 'Ukrainian', nativeName: 'Українська', family: 'Indo-European' },
  { code: 'es', name: 'Spanish', nativeName: 'Español', family: 'Indo-European' },
  { code: 'nl', name: 'Dutch', nativeName: 'Nederlands', family: 'Indo-European' },
  { code: 'sk', name: 'Slovak', nativeName: 'Slovenčina', family: 'Indo-European' },
  { code: 'hr', name: 'Croatian', nativeName: 'Hrvatski', family: 'Indo-European' },
  { code: 'pl', name: 'Polish', nativeName: 'Polski', family: 'Indo-European' },
  { code: 'lt', name: 'Lithuanian', nativeName: 'Lietuvių', family: 'Indo-European' },
  { code: 'nb', name: 'Norwegian Bokmål', nativeName: 'Norsk Bokmål', family: 'Indo-European' },
  { code: 'nn', name: 'Norwegian Nynorsk', nativeName: 'Norsk Nynorsk', family: 'Indo-European' },
  { code: 'fa', name: 'Persian', nativeName: 'فارسی', family: 'Indo-European' },
  { code: 'sl', name: 'Slovenian', nativeName: 'Slovenščina', family: 'Indo-European' },
  { code: 'gu', name: 'Gujarati', nativeName: 'ગુજરાતી', family: 'Indo-European' },
  { code: 'lv', name: 'Latvian', nativeName: 'Latviešu', family: 'Indo-European' },
  { code: 'it', name: 'Italian', nativeName: 'Italiano', family: 'Indo-European' },
  { code: 'oc', name: 'Occitan', nativeName: 'Occitan', family: 'Indo-European' },
  { code: 'ne', name: 'Nepali', nativeName: 'नेपाली', family: 'Indo-European' },
  { code: 'mr', name: 'Marathi', nativeName: 'मराठी', family: 'Indo-European' },
  { code: 'be', name: 'Belarusian', nativeName: 'Беларуская', family: 'Indo-European' },
  { code: 'sr', name: 'Serbian', nativeName: 'Српски', family: 'Indo-European' },
  { code: 'lb', name: 'Luxembourgish', nativeName: 'Lëtzebuergesch', family: 'Indo-European' },
  { code: 'vec', name: 'Venetian', nativeName: 'Vèneto', family: 'Indo-European' },
  { code: 'as', name: 'Assamese', nativeName: 'অসমীয়া', family: 'Indo-European' },
  { code: 'cy', name: 'Welsh', nativeName: 'Cymraeg', family: 'Indo-European' },
  { code: 'szl', name: 'Silesian', nativeName: 'Ślōnski', family: 'Indo-European' },
  { code: 'ast', name: 'Asturian', nativeName: 'Asturianu', family: 'Indo-European' },
  { code: 'hne', name: 'Chhattisgarhi', nativeName: 'छत्तीसगढ़ी', family: 'Indo-European' },
  { code: 'awa', name: 'Awadhi', nativeName: 'अवधी', family: 'Indo-European' },
  { code: 'mai', name: 'Maithili', nativeName: 'मैथिली', family: 'Indo-European' },
  { code: 'bho', name: 'Bhojpuri', nativeName: 'भोजपुरी', family: 'Indo-European' },
  { code: 'sd', name: 'Sindhi', nativeName: 'سنڌي', family: 'Indo-European' },
  { code: 'ga', name: 'Irish', nativeName: 'Gaeilge', family: 'Indo-European' },
  { code: 'fo', name: 'Faroese', nativeName: 'Føroyskt', family: 'Indo-European' },
  { code: 'hi', name: 'Hindi', nativeName: 'हिन्दी', family: 'Indo-European' },
  { code: 'pa', name: 'Punjabi', nativeName: 'ਪੰਜਾਬੀ', family: 'Indo-European' },
  { code: 'bn', name: 'Bengali', nativeName: 'বাংলা', family: 'Indo-European' },
  { code: 'or', name: 'Oriya', nativeName: 'ଓଡ଼ିଆ', family: 'Indo-European' },
  { code: 'tg', name: 'Tajik', nativeName: 'Тоҷикӣ', family: 'Indo-European' },
  { code: 'yi', name: 'Eastern Yiddish', nativeName: 'ייִדיש', family: 'Indo-European' },
  { code: 'lmo', name: 'Lombard', nativeName: 'Lumbaart', family: 'Indo-European' },
  { code: 'lij', name: 'Ligurian', nativeName: 'Ligure', family: 'Indo-European' },
  { code: 'scn', name: 'Sicilian', nativeName: 'Sicilianu', family: 'Indo-European' },
  { code: 'fur', name: 'Friulian', nativeName: 'Furlan', family: 'Indo-European' },
  { code: 'sc', name: 'Sardinian', nativeName: 'Sardu', family: 'Indo-European' },
  { code: 'gl', name: 'Galician', nativeName: 'Galego', family: 'Indo-European' },
  { code: 'ca', name: 'Catalan', nativeName: 'Català', family: 'Indo-European' },
  { code: 'is', name: 'Icelandic', nativeName: 'Íslenska', family: 'Indo-European' },
  { code: 'sq', name: 'Albanian', nativeName: 'Shqip', family: 'Indo-European' },
  { code: 'li', name: 'Limburgish', nativeName: 'Limburgs', family: 'Indo-European' },
  { code: 'prs', name: 'Dari', nativeName: 'دری', family: 'Indo-European' },
  { code: 'af', name: 'Afrikaans', nativeName: 'Afrikaans', family: 'Indo-European' },
  { code: 'mk', name: 'Macedonian', nativeName: 'Македонски', family: 'Indo-European' },
  { code: 'si', name: 'Sinhala', nativeName: 'සිංහල', family: 'Indo-European' },
  { code: 'ur', name: 'Urdu', nativeName: 'اردو', family: 'Indo-European' },
  { code: 'mag', name: 'Magahi', nativeName: 'मगही', family: 'Indo-European' },
  { code: 'bs', name: 'Bosnian', nativeName: 'Bosanski', family: 'Indo-European' },
  { code: 'hy', name: 'Armenian', nativeName: 'Հայերեն', family: 'Indo-European' },

  // Sino-Tibetan Languages
  { code: 'zh', name: 'Chinese (Simplified)', nativeName: '简体中文', family: 'Sino-Tibetan' },
  { code: 'zh-TW', name: 'Chinese (Traditional)', nativeName: '繁體中文', family: 'Sino-Tibetan' },
  { code: 'yue', name: 'Cantonese', nativeName: '粵語', family: 'Sino-Tibetan' },
  { code: 'my', name: 'Burmese', nativeName: 'မြန်မာ', family: 'Sino-Tibetan' },

  // Afro-Asiatic Languages
  { code: 'ar', name: 'Arabic (Standard)', nativeName: 'العربية', family: 'Afro-Asiatic' },
  { code: 'ar-SA', name: 'Arabic (Najdi)', nativeName: 'العربية النجدية', family: 'Afro-Asiatic' },
  { code: 'ar-LB', name: 'Arabic (Levantine)', nativeName: 'العربية الشامية', family: 'Afro-Asiatic' },
  { code: 'ar-EG', name: 'Arabic (Egyptian)', nativeName: 'العربية المصرية', family: 'Afro-Asiatic' },
  { code: 'ar-MA', name: 'Arabic (Moroccan)', nativeName: 'العربية المغربية', family: 'Afro-Asiatic' },
  { code: 'ar-IQ', name: 'Arabic (Mesopotamian)', nativeName: 'العربية العراقية', family: 'Afro-Asiatic' },
  { code: 'ar-YE', name: 'Arabic (Ta\'izzi-Adeni)', nativeName: 'العربية اليمنية', family: 'Afro-Asiatic' },
  { code: 'ar-TN', name: 'Arabic (Tunisian)', nativeName: 'العربية التونسية', family: 'Afro-Asiatic' },
  { code: 'he', name: 'Hebrew', nativeName: 'עברית', family: 'Afro-Asiatic' },
  { code: 'mt', name: 'Maltese', nativeName: 'Malti', family: 'Afro-Asiatic' },

  // Austronesian Languages
  { code: 'id', name: 'Indonesian', nativeName: 'Bahasa Indonesia', family: 'Austronesian' },
  { code: 'ms', name: 'Malay', nativeName: 'Bahasa Melayu', family: 'Austronesian' },
  { code: 'tl', name: 'Tagalog', nativeName: 'Tagalog', family: 'Austronesian' },
  { code: 'ceb', name: 'Cebuano', nativeName: 'Cebuano', family: 'Austronesian' },
  { code: 'jv', name: 'Javanese', nativeName: 'Basa Jawa', family: 'Austronesian' },
  { code: 'su', name: 'Sundanese', nativeName: 'Basa Sunda', family: 'Austronesian' },
  { code: 'min', name: 'Minangkabau', nativeName: 'Baso Minangkabau', family: 'Austronesian' },
  { code: 'ban', name: 'Balinese', nativeName: 'Basa Bali', family: 'Austronesian' },
  { code: 'bjn', name: 'Banjar', nativeName: 'Bahasa Banjar', family: 'Austronesian' },
  { code: 'pag', name: 'Pangasinan', nativeName: 'Salitan Pangasinan', family: 'Austronesian' },
  { code: 'ilo', name: 'Iloko', nativeName: 'Pagsasao nga Ilokano', family: 'Austronesian' },
  { code: 'war', name: 'Waray', nativeName: 'Winaray', family: 'Austronesian' },

  // Dravidian Languages
  { code: 'ta', name: 'Tamil', nativeName: 'தமிழ்', family: 'Dravidian' },
  { code: 'te', name: 'Telugu', nativeName: 'తెలుగు', family: 'Dravidian' },
  { code: 'kn', name: 'Kannada', nativeName: 'ಕನ್ನಡ', family: 'Dravidian' },
  { code: 'ml', name: 'Malayalam', nativeName: 'മലയാളം', family: 'Dravidian' },

  // Turkic Languages
  { code: 'tr', name: 'Turkish', nativeName: 'Türkçe', family: 'Turkic' },
  { code: 'az', name: 'Azerbaijani', nativeName: 'Azərbaycan', family: 'Turkic' },
  { code: 'uz', name: 'Uzbek', nativeName: 'Oʻzbek', family: 'Turkic' },
  { code: 'kk', name: 'Kazakh', nativeName: 'Қазақша', family: 'Turkic' },
  { code: 'ba', name: 'Bashkir', nativeName: 'Башҡорт', family: 'Turkic' },
  { code: 'tt', name: 'Tatar', nativeName: 'Татар', family: 'Turkic' },

  // Tai-Kadai Languages
  { code: 'th', name: 'Thai', nativeName: 'ไทย', family: 'Tai-Kadai' },
  { code: 'lo', name: 'Lao', nativeName: 'ລາວ', family: 'Tai-Kadai' },

  // Uralic Languages
  { code: 'fi', name: 'Finnish', nativeName: 'Suomi', family: 'Uralic' },
  { code: 'et', name: 'Estonian', nativeName: 'Eesti', family: 'Uralic' },
  { code: 'hu', name: 'Hungarian', nativeName: 'Magyar', family: 'Uralic' },

  // Austroasiatic Languages
  { code: 'vi', name: 'Vietnamese', nativeName: 'Tiếng Việt', family: 'Austroasiatic' },
  { code: 'km', name: 'Khmer', nativeName: 'ខ្មែរ', family: 'Austroasiatic' },

  // Other Languages
  { code: 'ja', name: 'Japanese', nativeName: '日本語', family: 'Japonic' },
  { code: 'ko', name: 'Korean', nativeName: '한국어', family: 'Koreanic' },
  { code: 'ka', name: 'Georgian', nativeName: 'ქართული', family: 'Kartvelian' },
  { code: 'eu', name: 'Basque', nativeName: 'Euskera', family: 'Language Isolate' },
  { code: 'ht', name: 'Haitian', nativeName: 'Kreyòl Ayisyen', family: 'Creole' },
  { code: 'pap', name: 'Papiamento', nativeName: 'Papiamentu', family: 'Creole' },
  { code: 'kea', name: 'Kabuverdianu', nativeName: 'Kriolu', family: 'Creole' },
  { code: 'tpi', name: 'Tok Pisin', nativeName: 'Tok Pisin', family: 'Creole' },
  { code: 'sw', name: 'Swahili', nativeName: 'Kiswahili', family: 'Niger-Congo' },
];


export const LANGUAGES_BY_FAMILY = AVAILABLE_LANGUAGES.reduce((acc, lang) => {
  if (!acc[lang.family]) {
    acc[lang.family] = [];
  }
  acc[lang.family].push(lang);
  return acc;
}, {} as Record<string, Language[]>);


export interface GenerationRequest {
  prompt: string;
  contentType: ContentType;
  targetLanguages: string[];
  sourceLanguage?: string;
  tone?: 'professional' | 'casual' | 'friendly' | 'formal';
  length?: 'short' | 'medium' | 'long';
}


export interface GeneratedContent {
  language: string;
  content: string;
  metadata?: {
    wordCount: number;
    characterCount: number;
    estimatedReadingTime: number;
  };
}


export interface GenerationResponse {
  originalContent: GeneratedContent;
  translations: GeneratedContent[];
  totalTokensUsed?: number;
  processingTime: number;
}

export interface GroqConfig {
  apiKey: string;
  model: string;
  maxTokens?: number;
  temperature?: number;
}

export interface AIAgentError {
  type: 'API_ERROR' | 'VALIDATION_ERROR' | 'RATE_LIMIT' | 'UNKNOWN';
  message: string;
  details?: any;
} 