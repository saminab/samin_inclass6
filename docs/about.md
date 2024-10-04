# Mkdocs Project

## Creating MKdocs

To Create a website using MKdocs we use mkdocs new my-project. You can follow the instructions in the following [MkDocs-website](https://www.mkdocs.org/getting-started/#adding-pages).

## Preview your Documents

Make sure you are in a same directory as the *mkdocs.yml* file, then start the server by running mkdocs serve.

    $ mkdocs serve
	INFO    -  Building documentation...
	INFO    -  Cleaning site directory
	INFO    -  Documentation built in 0.22 seconds
	INFO    -  [15:50:43] Watching paths for changes: 'docs', 'mkdocs.yml'
	INFO    -  [15:50:43] Serving on http://127.0.0.1:8000/

## Open the Website

Open up the link in your browser.[Mkdocs-website](http://127.0.0.1:8000/about/)

## Edit the theme and site name 

open **docs/index.md** document, change the initial heading to **MkLorum**, and save the changes.
Now try to edit configuration file **mkdocs.ymk**. Change the **site_name** setting to MKLorum and save the file.
	
site_name: MKLorum
	