import mammoth as mth

class wordToHtml():

    @property
    def diretorio(self):
        return{'caminho': r"DIGITE AQUI O DIRETÓRIO"
        }
        
    def main(self):
        with open (self.diretorio['caminho'], "rb") as docx_file:
            result = mth.convert_to_html(docx_file)
            text = result.value
            with open("output.html", 'w', encoding='utf-8') as htmlfile:
                htmlfile.write(text)
                
if __name__ == "__main__":
    service=wordToHtml()
    service.main()