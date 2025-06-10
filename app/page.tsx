'use client';

import { useState, useEffect } from 'react';
import { 
  AVAILABLE_LANGUAGES, 
  LANGUAGES_BY_FAMILY 
} from '../lib/types';

export default function Home() {
  const [prompt, setPrompt] = useState('');
  const [contentType, setContentType] = useState('email');
  const [selectedLanguages, setSelectedLanguages] = useState(['en']);
  const [tone, setTone] = useState('professional');
  const [length, setLength] = useState('medium');
  const [isGenerating, setIsGenerating] = useState(false);
  const [result, setResult] = useState<any>(null);
  const [error, setError] = useState('');
  const [copySuccess, setCopySuccess] = useState<string>('');
  const [apiKey, setApiKey] = useState<string>('');
  const [showApiKeyModal, setShowApiKeyModal] = useState(false);
  const [apiKeyInput, setApiKeyInput] = useState('');

  useEffect(() => {
    // checks if API key exists in localStorage
    const storedApiKey = localStorage.getItem('groq_api_key');
    if (storedApiKey) {
      setApiKey(storedApiKey);
    } else {
      setShowApiKeyModal(true);
    }
  }, []);

  const handleApiKeySubmit = () => {
    if (!apiKeyInput.trim()) {
      alert('Please enter a valid API key');
      return;
    }
    
    // stores API key in localStorage
    localStorage.setItem('groq_api_key', apiKeyInput.trim());
    setApiKey(apiKeyInput.trim());
    setShowApiKeyModal(false);
    setApiKeyInput('');
  };

  const handleChangeApiKey = () => {
    setShowApiKeyModal(true);
    setApiKeyInput(apiKey);
  };

  const handleGenerate = async () => {
    if (!apiKey) {
      setError('Please provide your Groq API key');
      setShowApiKeyModal(true);
      return;
    }

    //checks if anything is missing - redundent but kept just in case of bug in UI state management. 
    if (!prompt.trim()) {
      setError('Please enter a prompt');
      return;
    }

    if (selectedLanguages.length === 0) {
      setError('Please select at least one language');
      return;
    }

    setIsGenerating(true);
    setError('');

    try {
      const response = await fetch('http://localhost:8000/api/generate', {
        method: 'POST',
        headers: { 
          'Content-Type': 'application/json',
          'X-API-Key': apiKey
        },
        body: JSON.stringify({
          prompt,
          contentType,
          targetLanguages: selectedLanguages,
          tone,
          length
        })
      });

      if (!response.ok) {
        const errorData = await response.json();
        if (response.status === 401) {
          setError('Invalid API key. Please check your Groq API key.');
          setShowApiKeyModal(true);
          return;
        }
        throw new Error(errorData.detail || 'Generation failed');
      }

      const data = await response.json();
      setResult(data);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setIsGenerating(false);
    }
  };

  const addLanguage = (langCode: string) => {
    if (!selectedLanguages.includes(langCode)) {
      setSelectedLanguages(prev => [...prev, langCode]);
    }
  };

  const removeLanguage = (langCode: string) => {
    setSelectedLanguages(prev => prev.filter(l => l !== langCode));
  };

  const getLanguageByCode = (code: string) => {
    return AVAILABLE_LANGUAGES.find(lang => lang.code === code);
  };

  const copyToClipboard = async (text: string, identifier: string) => {
    try {
      await navigator.clipboard.writeText(text);
      setCopySuccess(identifier);
      setTimeout(() => setCopySuccess(''), 2000);
    } catch (err) {
      console.error('Failed to copy text: ', err);
    }
  };

  return (
    <div className="min-h-screen bg-white font-montserrat">
      <header className="border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">  
            <div className="flex items-center space-x-6">
              <img 
                src="/assets/groq-labs-logo.png" 
                alt="GroqLabs Logo" 
                className="h-8 w-auto"
              />
              <div className="hidden md:flex items-center space-x-4">
                <span className="text-gray-600">/</span>
                <span className="text-gray-900 font-medium">Project Linguist</span>
                <span className="px-2 py-1 bg-orange-100 text-orange-800 text-xs font-medium rounded">BETA</span>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <button
                onClick={handleChangeApiKey}
                className="text-sm text-gray-600 hover:text-gray-900 flex items-center"
              >
                <svg className="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 7a2 2 0 012 2m0 0a2 2 0 012 2m-2-2h-7m6 3a2 2 0 01-2 2 2 2 0 01-2-2m1.5-3h-7a2 2 0 00-2 2v4a2 2 0 002 2h7a2 2 0 002-2v-4a2 2 0 00-2-2z" />
                </svg>
                API Key
              </button>
              <a href="https://github.com/groq" className="flex items-center text-gray-600 hover:text-gray-900">
                <svg className="w-5 h-5 mr-1" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M10 0C4.477 0 0 4.484 0 10.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0110 4.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.203 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.942.359.31.678.921.678 1.856 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0020 10.017C20 4.484 15.522 0 10 0z" clipRule="evenodd"/>
                </svg>
                GitHub
              </a>
            </div>
          </div>
        </div>
      </header>
      <main className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">
            Multilingual Content Generator
          </h1>
          <p className="text-gray-600">
            Generate content concurrently across 119+ languages with a simple English prompt using <b>Qwen3-32B</b> powered by <b>Groq</b>
          </p>
        </div>
        <div className="bg-white border border-gray-200 rounded-lg p-6 mb-8">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Content Type</label>
              <select
                value={contentType}
                onChange={(e) => setContentType(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-orange-500 focus:border-orange-500"
              >
                <option value="email">Email</option>
                <option value="newsletter">Newsletter</option>
                <option value="article">Article</option>
                <option value="social-post">Social Post</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Tone</label>
              <select
                value={tone}
                onChange={(e) => setTone(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-orange-500 focus:border-orange-500"
              >
                <option value="professional">Professional</option>
                <option value="casual">Casual</option>
                <option value="friendly">Friendly</option>
                <option value="formal">Formal</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Length</label>
              <select
                value={length}
                onChange={(e) => setLength(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-orange-500 focus:border-orange-500"
              >
                <option value="short">Short (150-300 words)</option>
                <option value="medium">Medium (300-600 words)</option>
                <option value="long">Long (600-1200 words)</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Add Language</label>
              <select
                onChange={(e) => e.target.value && addLanguage(e.target.value)}
                value=""
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-orange-500 focus:border-orange-500"
              >
                <option value="">Select a language...</option>
                {Object.entries(LANGUAGES_BY_FAMILY).map(([family, languages]) => (
                  <optgroup key={family} label={family}>
                    {languages.map(lang => (
                      <option 
                        key={lang.code} 
                        value={lang.code}
                        disabled={selectedLanguages.includes(lang.code)}
                      >
                        {lang.name} ({lang.nativeName})
                      </option>
                    ))}
                  </optgroup>
                ))}
              </select>
            </div>
          </div>
          <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-1">Content Prompt</label>
            <textarea
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder="e.g., Write a welcome email for new customers joining Groq"
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-orange-500 focus:border-orange-500 h-24 resize-none"
            />
          </div>
          {selectedLanguages.length > 0 && (
            <div className="mb-4">
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Selected Languages ({selectedLanguages.length})
              </label>
              <div className="flex flex-wrap gap-2">
                {selectedLanguages.map(langCode => {
                  const lang = getLanguageByCode(langCode);
                  return (
                    <span
                      key={langCode}
                      className="inline-flex items-center px-2 py-1 rounded-md text-sm bg-gray-100 text-gray-800"
                    >
                      {lang?.name || langCode}
                      <button
                        onClick={() => removeLanguage(langCode)}
                        className="ml-1 text-gray-600 hover:text-gray-800"
                      >
                        ×
                      </button>
                    </span>
                  );
                })}
              </div>
            </div>
          )}
          <button
            onClick={handleGenerate}
            disabled={isGenerating || !prompt.trim() || selectedLanguages.length === 0}
            className={`w-full py-2 px-4 rounded-md font-medium ${
              isGenerating || !prompt.trim() || selectedLanguages.length === 0
                ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
                : 'bg-orange-600 text-white hover:bg-orange-700'
            }`}
          >
            {isGenerating ? 'Generating...' : 'Generate Multilingual Content'}
          </button>
          {error && (
            <div className="mt-4 p-3 bg-red-50 border border-red-200 text-red-700 rounded-md text-sm">
              {error}
            </div>
          )}
        </div>
        {isGenerating && (
          <div className="text-center py-12">
            <div className="inline-flex items-center space-x-1 mb-4">
              <div className="w-2 h-2 bg-orange-500 rounded-full animate-pulse"></div>
              <div className="w-2 h-2 bg-orange-500 rounded-full animate-pulse" style={{animationDelay: '0.2s'}}></div>
              <div className="w-2 h-2 bg-orange-500 rounded-full animate-pulse" style={{animationDelay: '0.4s'}}></div>
            </div>
            <p className="text-gray-600">Generating content in {selectedLanguages.length} languages...</p>
          </div>
        )}
        {result && !isGenerating && (
          <div className="space-y-6">
            <div className="text-center text-sm text-gray-500">
              Generated in {result.processingTime}ms
              {result.totalTokensUsed && (
                <> • {Math.round((result.totalTokensUsed / (result.processingTime / 1000))).toLocaleString()} tokens/sec</>
              )}
            </div>
            <div className="border border-gray-200 rounded-lg overflow-hidden">
              <div className="bg-gray-50 px-4 py-3 border-b border-gray-200 flex justify-between items-center">
                <h3 className="font-medium text-gray-900">
                  Original Content ({getLanguageByCode(result.originalContent.language)?.name || result.originalContent.language})
                </h3>
                <button
                  onClick={() => copyToClipboard(result.originalContent.content, 'original')}
                  className="inline-flex items-center px-3 py-1 text-xs font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-orange-500 focus:ring-offset-2"
                >
                  {copySuccess === 'original' ? (
                   <>
                     <svg className="w-5 h-5 mr-1 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                       <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                     </svg>
                   </>
                 ) : (
                   <>
                     <svg className="w-5 h-5 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                       <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                     </svg>
                   </>
                 )}
                </button>
              </div>
              <div className="p-4">
                <div className="whitespace-pre-line text-gray-800 mb-3">
                  {result.originalContent.content}
                </div>
                <div className="flex items-center text-xs text-gray-500 space-x-4">
                  <span>{result.originalContent.metadata?.wordCount} words</span>
                  <span>{result.originalContent.metadata?.estimatedReadingTime} min read</span>
                  <span>{result.originalContent.metadata?.characterCount} characters</span>
                </div>
              </div>
            </div>
            {result.translations?.map((translation: any, index: number) => {
              const lang = getLanguageByCode(translation.language);
              return (
                <div key={index} className="border border-gray-200 rounded-lg overflow-hidden">
                  <div className="bg-gray-50 px-4 py-3 border-b border-gray-200 flex justify-between items-center">
                    <h3 className="font-medium text-gray-900">
                      Translation {index + 1} ({lang?.name || translation.language})
                      {lang?.nativeName && lang.nativeName !== lang.name && (
                        <span className="text-gray-600 font-normal ml-1">
                          - {lang.nativeName}
                        </span>
                      )}
                    </h3>
                    <button
                      onClick={() => copyToClipboard(translation.content, `translation-${index}`)}
                      className="inline-flex items-center px-3 py-1 text-xs font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-orange-500 focus:ring-offset-2"
                    >
                      {copySuccess === `translation-${index}` ? (
                       <>
                         <svg className="w-5 h-5 mr-1 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                           <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                         </svg>
                       </>
                     ) : (
                       <>
                         <svg className="w-5 h-5 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                           <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                         </svg>
                       </>
                     )}
                    </button>
                  </div>
                  <div className="p-4">
                    <div className="whitespace-pre-line text-gray-800 mb-3">
                      {translation.content}
                    </div>
                    <div className="flex items-center text-xs text-gray-500 space-x-4">
                      <span>{translation.metadata?.wordCount} words</span>
                      <span>{translation.metadata?.estimatedReadingTime} min read</span>
                      <span>{translation.metadata?.characterCount} characters</span>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        )}
        {!result && !isGenerating && (
          <div className="text-center py-12 text-gray-500">
            <p>Configure your content above and click generate</p>
            <p className="text-sm mt-1">Choose from {AVAILABLE_LANGUAGES.length}+ languages & dialects!</p>
          </div>
        )}
      </main>

      {/* API Key Modal */}
      {showApiKeyModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white rounded-lg p-6 w-full max-w-md mx-4">
            <div className="flex items-center mb-4">
              <svg className="w-6 h-6 text-orange-600 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 7a2 2 0 012 2m0 0a2 2 0 012 2m-2-2h-7m6 3a2 2 0 01-2 2 2 2 0 01-2-2m1.5-3h-7a2 2 0 00-2 2v4a2 2 0 002 2h7a2 2 0 002-2v-4a2 2 0 00-2-2z" />
              </svg>
              <h3 className="text-lg font-semibold text-gray-900">Groq API Key Required</h3>
            </div>
            
            <p className="text-gray-600 mb-4">
              To use this service, you need to provide your own Groq API key. 
              <a 
                href="https://console.groq.com/keys" 
                target="_blank" 
                rel="noopener noreferrer" 
                className="text-orange-600 hover:text-orange-700 underline ml-1"
              >
                Get your free API key here
              </a>
            </p>
            
            <div className="mb-4">
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Groq API Key
              </label>
              <input
                type="password"
                value={apiKeyInput}
                onChange={(e) => setApiKeyInput(e.target.value)}
                placeholder="Insert Here"
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500"
                onKeyPress={(e) => e.key === 'Enter' && handleApiKeySubmit()}
              />
            </div>
            
            <div className="bg-yellow-50 border border-yellow-200 rounded-md p-3 mb-4">
              <div className="flex">
                <svg className="w-4 h-4 text-yellow-600 mt-0.5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.864-.833-2.5 0L4.268 8.5c-.77.833.192 2.5 1.732 2.5z" />
                </svg>
                <div>
                  <p className="text-sm text-yellow-800">
                    <strong>Privacy:</strong> Your API key is stored locally in your browser and sent directly to Groq. We never see or store your API key.
                  </p>
                </div>
              </div>
            </div>
            
            <div className="flex space-x-3">
              <button
                onClick={handleApiKeySubmit}
                className="flex-1 bg-orange-600 text-white px-4 py-2 rounded-md hover:bg-orange-700 focus:outline-none focus:ring-2 focus:ring-orange-500 focus:ring-offset-2"
              >
                Save API Key
              </button>
              {apiKey && (
                <button
                  onClick={() => setShowApiKeyModal(false)}
                  className="px-4 py-2 text-gray-600 hover:text-gray-800 focus:outline-none"
                >
                  Cancel
                </button>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
