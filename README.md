# tft-scraper
Scripts en Python para leer los TFT (Trabajo de Fin de Título) de la web de la Escuela de Ingeniería Informática de la Universidad de Las Palmas de Gran Canaria (https://www.eii.ulpgc.es/es/informacionacademica/tft/ofertatft). 

## Requisitos:
Versión de Python >= 3.11

## Instalación:
```
git clone https://github.com/Alejandro-M-Cruz/tft-scraper
cd web-scraper
pip install -r requirements.txt
```

## Uso:
Los siguientes comandos leen los TFT de la web de la EII y almacenan los TFT que contienen el texto "python" en el fichero python.md.
```
python scrape_tfts.py
python search_tfts.py -q python -f python.md
```
