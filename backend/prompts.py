from typing import Dict, Tuple
from .types import ContentType, Tone, Length

def generate_prompt(
    content_type: ContentType,
    user_prompt: str,
    tone: Tone = Tone.PROFESSIONAL,
    length: Length = Length.MEDIUM
) -> Tuple[str, str]:
    """
    Generate system and user prompts based on content type and parameters
    Returns: (system_prompt, user_prompt)
    """
    
    length_guidelines = {
        Length.SHORT: "150-300 words",
        Length.MEDIUM: "300-600 words", 
        Length.LONG: "600-1200 words"
    }
    
    tone_descriptions = {
        Tone.PROFESSIONAL: "professional, clear, and business-appropriate",
        Tone.CASUAL: "relaxed, conversational, and approachable",
        Tone.FRIENDLY: "warm, welcoming, and personable",
        Tone.FORMAL: "formal, respectful, and traditional"
    }

    content_guidelines = {
        ContentType.EMAIL: {
            "structure": "Subject line, greeting, introduction paragraph, main content with bullet points if needed, call-to-action, and professional closing",
            "best_practices": "Use proper email formatting with line breaks between sections, short paragraphs, bullet points on separate lines. Add more content to the email if word count is less than requested. DO NOT CREATE SUPER LONG SIGNATURE. ",
            "format_example": """Subject: Welcome to Our Platform

                Hi [Customer Name],

                Welcome to our community! We're excited to have you join us.

                As a new member, here's what you can expect:

                - Access to exclusive features and content
                - Dedicated customer support team
                - Regular updates and improvements
                - Community forums and resources

                To get started, simply log into your account and explore the dashboard.

                If you have any questions, don't hesitate to reach out to our support team.

                Best regards,
                The Team"""
        },
        ContentType.NEWSLETTER: {
            "structure": "Compelling headline, introduction, main sections with subheadings, conclusion with call-to-action",
            "best_practices": "Use clear sections with subheadings, bullet points for key information, proper spacing between sections",
            "format_example": """Newsletter: Monthly Tech Updates

Welcome to This Month's Edition

Hello subscribers! Here are the latest updates from our platform.

New Features

This month we've introduced several exciting features:

- Enhanced dashboard with better analytics
- New collaboration tools for teams
- Improved mobile experience
- Advanced security features

Upcoming Events

Mark your calendars for these upcoming events:

- Webinar: Platform Best Practices (March 15)
- User Conference: TechCon 2024 (April 10-12)
- Training Session: Advanced Features (March 25)

Community Spotlight

This month we're highlighting amazing work from our community members.

Stay tuned for more updates next month!

Best regards,
The Newsletter Team"""
        },
        ContentType.ARTICLE: {
            "structure": "Compelling headline, introduction, body with clear sections and subheadings, conclusion with key takeaways",
            "best_practices": "Use subheadings for readability, include examples, provide actionable insights, proper paragraph breaks",
            "format_example": """The Future of AI in Business Operations

Introduction

Artificial Intelligence is revolutionizing how businesses operate across industries.

Current Applications

AI is currently being used in several key areas:

- Customer service automation
- Predictive analytics and forecasting
- Supply chain optimization
- Quality control and monitoring

Benefits for Organizations

Companies implementing AI solutions report significant improvements:

1. Increased Efficiency: Automation reduces manual work by up to 40%
2. Better Decision Making: Data-driven insights improve accuracy
3. Cost Reduction: Streamlined processes lower operational costs

Implementation Strategies

To successfully adopt AI in your organization:

- Start with pilot projects in specific departments
- Invest in employee training and development
- Choose the right technology partners
- Measure and track performance metrics

Conclusion

AI adoption is no longer optional for competitive businesses. Organizations that embrace these technologies now will have significant advantages in the future.

The key is to start small, learn quickly, and scale successful implementations."""
        },
        ContentType.SOCIAL_POST: {
            "structure": "Engaging hook, main message, call-to-action with relevant hashtags",
            "best_practices": "Use line breaks for readability, include emojis appropriately, hashtags on separate lines",
            "format_example": """🚀 Exciting news! We just launched our new AI-powered platform!

After months of development, we're thrilled to share this game-changing tool with our community.

✨ Key features:
- Intelligent automation
- Real-time analytics
- Seamless integrations
- User-friendly interface

Ready to transform your workflow? 

Get started today with our free trial! Link in bio 👆

#AI #ProductLaunch #Innovation #TechNews #Productivity #Automation"""
        }
    }

    guidelines = content_guidelines[content_type]
    target_length = length_guidelines[length]
    tone_desc = tone_descriptions[tone]

    system_prompt = f"""You are an expert content writer specializing in {content_type.value} creation.

Your task is to create high-quality {content_type.value} content that is {tone_desc} in tone.

Content Requirements:
- Type: {content_type.value.title()}
- Tone: {tone_desc}
- Length: {target_length}
- Structure: {guidelines['structure']}
- Best Practices: {guidelines['best_practices']}

CRITICAL FORMATTING REQUIREMENTS:
1. Use proper line breaks (\\n\\n) between paragraphs and sections
2. Keep paragraphs short (2-4 sentences max)
3. Use bullet points on separate lines with dashes (-) or asterisks (*)
4. Include proper spacing between all sections
5. DO NOT create one long paragraph - break up the content naturally
6. Format exactly like the example below
7. DO NOT use markdown formatting (no **, *, ##, or other symbols)
8. Write in PLAIN TEXT only - no bold, italic, or markdown symbols

FORBIDDEN FORMATTING:
- Do NOT use **bold text**
- Do NOT use *italic text*
- Do NOT use ## headings
- Do NOT use ### subheadings
- Do NOT use [links](url)
- Use plain text for all emphasis

FORMAT EXAMPLE:
{guidelines['format_example']}

IMPORTANT: Output ONLY the requested content in PLAIN TEXT. Do NOT include any reasoning, thinking process, commentary, explanations, or phrases like "Here's the content" or "I'll create...". Do NOT explain what you're doing. Start directly with the content and follow the exact formatting style shown in the example."""

    enhanced_user_prompt = f"""Create a {content_type.value} with the following specifications:

Content Request: {user_prompt}

Requirements:
- Tone: {tone_desc}
- Target length: {target_length}
- Format: {content_type.value}

FORMATTING INSTRUCTIONS:
- Use proper paragraph breaks (double line breaks)
- Include appropriate headings/subject lines
- Use bullet points on separate lines when listing items
- Keep paragraphs concise and readable
- Follow the exact formatting style from the example

Remember: Output ONLY the {content_type.value} content with proper formatting. No explanations or commentary."""

    return system_prompt, enhanced_user_prompt
