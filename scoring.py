import difflib
import re

def clean_text(text):
    """Remove punctuation and convert to lowercase for fair comparison."""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

def calculate_pronunciation_score(target, spoken):
    """
    Calculate pronunciation score using difflib SequenceMatcher.
    Returns a score between 0 and 100.
    """
    target_clean = clean_text(target)
    spoken_clean = clean_text(spoken)
    
    if not target_clean or not spoken_clean:
        return 0

    matcher = difflib.SequenceMatcher(None, target_clean, spoken_clean)
    score = matcher.ratio() * 100
    return round(score)
