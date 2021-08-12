# Webscrapper do site do Tribunal de Justiça de São Paulo

Feito como teste para o Centro de Regulação e Democracia do Insper

## Built with:

- Selenium
- BeautifulSoup
- Pandas
- Tkinter

<p align="center">
  <img src="data:image/png;base64,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" width="350" title="Interface do programa">
</p>