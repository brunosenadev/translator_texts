from language_tool_python import LanguageTool, utils
from re import split

def correct_spelling(text: str) -> list[str]:
    tool = LanguageTool('pt-BR')
    errors_found = tool.check(text)
    corrected_text = utils.correct(text, errors_found)
    return text_processing(corrected_text)

def text_processing(text: str) -> list[str]:
    text_processed = split(r'(?<=\.) ', text)
    return text_processed
