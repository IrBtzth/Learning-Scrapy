

# Quotes Notes
This note will show the notes I have taken for the module 2 of the course "Curso Scrapy" dictated in https://platzi.com/cursos/scrapy/.


# <span style="color:purple">Scrapy Shell<span/>
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
# Running Scrapy


*<span style="color:purple">Scrapy is an asynchronous framework. Asynchronous programming is when an operation is performed on the database, but the software is able to do other things during this process. Then, when the response arrives, your software can process it.</span>*

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

The spiders are run with

```
scrapy crawl quotes
```
where quotes is the value of the variable name in quotes.py 

# quotes.py by Dissection

```python
top = getattr(self,'top', None)
        if top:
            top = int(top)
            topTags = topTags[:top]
```
The above code works as follows, if there is within the execution of parse() an attribute named "top" it will be stored in the variable top. If the attribute is not sent in the execution, None will be stored in top. 

**To understand callback:** *"A callback function is a function passed into another function as an argument, which is then invoked inside the outer function to complete some kind of routine or action."* by https://developer.mozilla.org/en-US/docs/Glossary/Callback_function

```javascript
function greeting(name) {
  alert('Hello ' + name);
}

function processUserInput(callback) {
  var name = prompt('Please enter your name.');
  callback(name);
}

processUserInput(greeting);
```

**To understand cb_kwargs:** *"cb_kwargs is not a python reserved keyword or builtin function, so it can mean anything depending on context.*

*The typical use is as a dictionary of keyword, value pairs that is meant to be passed to a callback function at some time, for example:*
```python
cb_kwargs = {'timeout':22, 'verbose':False}
```
*Then some function callback might later be called as*
```python
callback(**cb_kwargs)
```
*which for this particular dictionary would be equivalent to calling it as:*
```python
callback(timeout=22, verbose=False)
```
 https://stackoverflow.com/questions/30695803/what-does-cb-in-cb-kwargs-stand-for

