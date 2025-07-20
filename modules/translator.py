"""
translator.py
-------------
Translates text between supported languages using MarianMT from Hugging Face.

Author: Maria Mahmood
Date: July 2025
"""

from transformers import MarianMTModel, MarianTokenizer

SUPPORTED_LANGUAGES = {
    "en": "English",
    "ur": "Urdu",
    "hi": "Hindi",
    "fr": "French",
    "es": "Spanish",
    "ar": "Arabic",
    "de": "German",
    "zh-cn": "Chinese (Simplified)"
}

def get_model_name(src_lang, tgt_lang):
    # Hugging Face uses 'zh' for Chinese
    src = "zh" if src_lang == "zh-cn" else src_lang
    tgt = "zh" if tgt_lang == "zh-cn" else tgt_lang
    return f"Helsinki-NLP/opus-mt-{src}-{tgt}"

def load_translation_pipeline(src_lang, tgt_lang):
    model_name = get_model_name(src_lang, tgt_lang)
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return model, tokenizer

def translate(text, src_lang="auto", tgt_lang="en"):
    if src_lang == tgt_lang:
        return text

    try:
        model, tokenizer = load_translation_pipeline(src_lang, tgt_lang)
        tokens = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        translated = model.generate(**tokens)
        return tokenizer.decode(translated[0], skip_special_tokens=True)
    except Exception as e:
        print(f"[ERROR] Translation from {src_lang} to {tgt_lang} failed: {e}")
        return "[Translation Failed]"
