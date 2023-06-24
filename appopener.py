"""
    with open("command.csv","w", encoding="utf-8") as file:
    file.write(hindi + "\n")

datas = pd.read_csv("command.csv")
print(datas)

translator = Translator()
translations = {}
for column in datas.columns:
    unique = datas[column].unique()
    for element in unique:
        translations[element] = translator.translate(element).text
for i in translations.items():
    print(i)

datas.replace(translations, inplace=True)
print(datas)
    """
