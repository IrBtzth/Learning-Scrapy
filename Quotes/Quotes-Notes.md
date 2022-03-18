
# Quotes Notes
This note will show the notes I have taken for the module 2 of the course "Curso Scrapy" dictated in https://platzi.com/cursos/scrapy/.

:shipit:

To open the scrapy terminal use the command

```bash
scrapy shell 'http://quotes.toscrape.com/page/1' 
```
:seedling: Useful for verifying that xpath expressions are working 



```python
top = getattr(self,'top', None)
        if top:
            top = int(top)
            topTags = topTags[:top]
```
El codigo anterior funciona de la siguiente forma, si existe dentro de la ejecución de parse() un atributo de nombre top se guardara en la variable top. Si no se envía el atributo en la ejecución se guardara None en top. 


    1. To understand callback: A callback function is a function passed into another function as an argument, 
    which is then invoked inside the outer function to complete some kind of routine or action.
    
    2.To understand cb_kwargs: https://stackoverflow.com/questions/30695803/what-does-cb-in-cb-kwargs-stand-for
    """
