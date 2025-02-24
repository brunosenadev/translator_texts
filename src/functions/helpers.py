from language_tool_python import LanguageTool, utils
from re import split
from bs4 import BeautifulSoup

def correct_spelling(text: str) -> list[str]:
    tool = LanguageTool('pt-BR')
    errors_found = tool.check(text)
    corrected_text = utils.correct(text, errors_found)
    return text_processing(corrected_text)

def text_processing(text: str) -> list[str]:
    text_processed = split(r'(?<=\.) ', text)
    return text_processed

def paragraph_processing(list_str: list[str]):
    text_paragraph_processing = "\n".join(list_str)
    return text_paragraph_processing

def clean_richtext(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    
    for p in soup.find_all("p"):
        p.insert_before("\n") 
        p.unwrap() 

    for br in soup.find_all("br"):
        br.replace_with("\n")
    
    text = soup.get_text(separator=" ")
    text = "\n".join(line.strip() for line in text.split("\n") if line.strip())
    return text