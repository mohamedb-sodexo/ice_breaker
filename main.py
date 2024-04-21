from langchain.agents import tool
from langchainhub import pull
from dotenv import load_dotenv
load_dotenv()

@tool("")
def get_text_length(text: str) -> int:
    """
    returns the length of a text by characters

    :param text: _description_
    :return: _description_
    """
    return len(text)

if __name__ == "__main__":
    print("toto")
    tools = [get_text_length]
    
    template="""
    
    """