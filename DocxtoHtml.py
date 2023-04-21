import mammoth as mth

caminho  = r"DIGITE AQUI O DIRETÓRIO"

with open (caminho, "rb") as docx_file:
    result = mth.convert_to_html(docx_file)
    text = result.value
    with open("output.html", 'w', encoding='utf-8') as htmlfile:
        htmlfile.write(text)