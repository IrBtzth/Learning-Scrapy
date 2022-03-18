

# Quotes Notes
This note will show the notes I have taken for the module 2 of the course "Curso Scrapy" dictated in https://platzi.com/cursos/scrapy/.

:shipit:

# Scrapy Shell
To open the scrapy terminal use the command

```bash
scrapy shell 'http://quotes.toscrape.com/page/1' 
```
:seedling: Useful for verifying that xpath expressions are working 

```bash
>>> response.xpath('//h1/a/text()').get()
'Quotes to Scrape'
```
:seedling: The getall() method fetches us the list

```bash
>>> response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
['“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”', ...]
```
:seedling: You can know the methods of the terminal with

```bash
>>> dir(request)
```
# Creating the project

After having created the repository, the .gitignore file and the virtual environment, (pip must be updated) we install the dependencies pip3 install scrapy autopep8 
```
 pip3 install scrapy autopep8 
 ```
:seedling: Initialize scrapy project

```
 scrapy startproject quotes_scraper
 ```
Files to know

- ***scrapy.cfg:*** Contains information for deply

- ***pipelines.py:*** allows us to modify our data from the moment they enter our spiders until they reach the end.
- ***middlewares.py*** allows to work with signals and use events as in nodejs
- ***items.py:*** we have a complex way to play and transform the response data to save it in a standard way.
- **nit.py:** indicates that this folder is a python module, and is an empty file.

- **spiders:** where the scripts should be created, e.g. quotes.py

- **setings:** general settings

```
 
 ```







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
