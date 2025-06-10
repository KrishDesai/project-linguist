import re
import math
from typing import Dict, List
from .types import GeneratedContent, ContentMetadata


def remove_markdown_formatting(content: str) -> str:
    """Remove markdown formatting symbols from content"""
    # eemove bold formatting **text** or __text__
    content = re.sub(r'\*\*(.*?)\*\*', r'\1', content)
    content = re.sub(r'__(.*?)__', r'\1', content)
    
    # remove italic formatting *text* or _text_
    content = re.sub(r'\*(.*?)\*', r'\1', content)
    content = re.sub(r'_(.*?)_', r'\1', content)
    
    # remove heading markers ## or ###
    content = re.sub(r'^#{1,6}\s*', '', content, flags=re.MULTILINE)
    
    # remove link formatting [text](url)
    content = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', content)
    
    # remove code formatting `code`
    content = re.sub(r'`([^`]+)`', r'\1', content)
    
    # remove strikethrough ~~text~~
    content = re.sub(r'~~(.*?)~~', r'\1', content)
    
    return content


def clean_content(content: str) -> str:
    """Clean and normalize content while preserving line breaks"""
    # remove any remaining HTML tags if present
    content = re.sub(r'<[^>]+>', '', content)
    
    # remove markdown formatting
    content = remove_markdown_formatting(content)
    
    # remove excessive spaces on the same line (multiple spaces become one)
    # but preserve line breaks and paragraph breaks
    content = re.sub(r'[ \t]+', ' ', content)
    
    # clean up excessive line breaks (more than 2 consecutive newlines become 2)
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # remove trailing spaces at the end of lines
    content = re.sub(r'[ \t]+\n', '\n', content)
    
    return content.strip()


def calculate_metadata(content: str) -> ContentMetadata:
    """Calculate metadata for content"""
    # clean content for accurate counting
    clean_text = clean_content(content)
    
    # character count
    char_count = len(clean_text)
    
    # word count (split by whitespace and filter empty strings)
    word_count = len([word for word in clean_text.split() if word.strip()])
    
    # estimated reading time (average 200 words per minute)
    reading_time = max(1, math.ceil(word_count / 200))
    
    return ContentMetadata(
        wordCount=word_count,
        characterCount=char_count,
        estimatedReadingTime=reading_time
    )


def create_generated_content(language: str, content: str) -> GeneratedContent:
    """Create a GeneratedContent object with metadata"""
    # remove markdown formatting and preserve line breaks
    clean_content_for_display = remove_markdown_formatting(content.strip())
    
    # use cleaned content for metadata calculation
    cleaned_for_metadata = clean_content(content)
    metadata = calculate_metadata(cleaned_for_metadata)
    
    return GeneratedContent(
        language=language,
        content=clean_content_for_display,
        metadata=metadata
    )


def remove_thinking_blocks(content: str) -> str:
    """Remove reasoning/thinking blocks from generated content"""
    # remove everything between <think> and </think> tags (case insensitive, multiline)
    cleaned_content = re.sub(r'<think>.*?</think>', '', content, flags=re.IGNORECASE | re.DOTALL)
    
    # also handle variations like <thinking> tags
    cleaned_content = re.sub(r'<thinking>.*?</thinking>', '', cleaned_content, flags=re.IGNORECASE | re.DOTALL)
    
    # remove content that starts with <think> even without closing tag
    cleaned_content = re.sub(r'<think>.*', '', cleaned_content, flags=re.IGNORECASE | re.DOTALL)
    
    # split into lines and filter out reasoning lines
    lines = cleaned_content.split('\n')
    filtered_lines = []
    
    skip_patterns = [
        # explicit thinking indicators
        'think', 'thinking', 'reasoning',
        # common reasoning starters
        'okay, i', 'let me', 'first,', 'next,', 'now,', 'then,', 'also,', 'moving',
        'translating', 'i need to', 'i should', 'i will', 'i\'ll',
        # translation process indicators
        'starting with', 'going through', 'working on', 'checking', 'ensuring',
        'double-check', 'make sure', 'verify', 'review',
        # reasoning about choices
        'could be', 'would be', 'might be', 'sounds better', 'is better',
        'for instance', 'for example', 'such as', 'like this',
        # incomplete or instructional content
        'subject:', 'body:', 'remember:', 'note:', 'important:',
        'in french', 'in english', 'translation', 'translate',
        # meta-commentary
        'the original', 'the content', 'the text', 'the email',
        'this becomes', 'this translates', 'this should be',
        # version/adjustment commentary
        'final version', 'this version', 'adjusted version', 'updated version',
        'meets all requirements', 'meets the requirements', 'with plain text',
        'plain text adjustments', 'adjust the', 'adjustments as needed',
        'as needed', 'placeholders as needed', 'address/phone placeholders',
        # formatting instructions
        'proper line breaks', 'concise paragraphs', 'bullet points',
        'no markdown', 'without markdown', 'plain text only',
        'formatted version', 'formatted content', 'formatting applied',
        # completion indicators
        'here is the', 'here\'s the', 'below is the', 'above is the',
        'content is ready', 'content ready', 'generation complete'
    ]
    
    for line in lines:
        stripped_line = line.strip().lower()
        
        # skip empty lines
        if not stripped_line:
            filtered_lines.append(line)
            continue
            
        # skip lines that match reasoning patterns
        should_skip = False
        for pattern in skip_patterns:
            if pattern in stripped_line:
                should_skip = True
                break
        
        # skip lines that are clearly instructions or meta-commentary
        if (stripped_line.startswith('"') and ('–' in stripped_line or 'or ' in stripped_line or 'becomes' in stripped_line)):
            should_skip = True
        
        # skip lines that end with colons and contain instructional words
        if stripped_line.endswith(':') and any(word in stripped_line for word in ['version', 'adjustments', 'requirements', 'format']):
            should_skip = True
        
        # skip very short lines that are likely headers or fragments
        if len(stripped_line) <= 2 and stripped_line not in ['hi', 'in']:
            should_skip = True
            
        if not should_skip:
            filtered_lines.append(line)
    
    cleaned_content = '\n'.join(filtered_lines)
    
    # remove any remaining translation artifacts
    artifact_patterns = [
        r'"[^"]*"[ ]*[–-][ ]*"[^"]*"',  # "english" – "french" patterns
        r'"[^"]*"[ ]*or[ ]*"[^"]*"',    # "option1" or "option2" patterns
        r'becomes[ ]*"[^"]*"',          # becomes "translation" patterns
        # new patterns for version commentary
        r'.*version.*:.*',              # lines with "version" and colon
        r'.*requirements.*:.*',         # lines with "requirements" and colon
        r'.*adjustments.*:.*',          # lines with "adjustments" and colon
    ]
    
    for pattern in artifact_patterns:
        cleaned_content = re.sub(pattern, '', cleaned_content, flags=re.IGNORECASE | re.MULTILINE)
    
    # clean up extra whitespace and return
    cleaned_content = re.sub(r'\n{3,}', '\n\n', cleaned_content)
    return cleaned_content.strip() 