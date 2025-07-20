"""
language_detector.py
---------------------

This module detects the language of the input text.

Author: Maria Mahmood
Date: July 2025
"""

from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# For consistent results
DetectorFactory.seed = 42

SUPPORTED_LANGUAGES = {
    "en": "English",
    "ur": "Urdu",
    "hi": "Hindi",
    "fr": "French",
    "es": "Spanish",
    "ar": "Arabic",
    "de": "German",
    "zh-cn": "Chinese (Simplified)",
}

def detect_language(text):
    """
    Detects the language of the input text.

    Parameters:
        text (str): The text to detect the language of.

    Returns:
        str: ISO 639-1 code of the language ('en', 'ur', etc.) or 'unsupported'.
    """
    try:
        lang_code = detect(text)
        return lang_code if lang_code in SUPPORTED_LANGUAGES else "unsupported"
    except LangDetectException:
        return "unsupported"
