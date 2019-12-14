def PHRASE_RESULTS(phrase):
    xpath = f"//div[@id='links']//*[contains(text(), '{phrase}')]"
    print(xpath)

PHRASE_RESULTS("Hello World")