# ScrapingDolarBs
Scraping Web del precio del Dolar en Bolívares, script para usar en polybar, extrae y muestra resultado

Script realizado para usar en la `Polybar y Rofi en Linux`

Para usar, ejecuta el script, `Python3 dolar.py` se realizara una peticion a la Web: `https://monitordolarvenezuela.com/`.  
Se extraeran los datos del precio del dolar, tanto para el `Banco Central de Venezuela`, `En Paralelo` y `Binance P2P`.  
Los datos son almacenados en un archivo `JSON` para ser usados cada vez que se necesite mostar, los datos son actualizados cada 15 minutos.  
El archivo es almacenado en la misma ruta del script, en este caso es: `~/.config/polybar/hack/scripts/`

Para mostrar el resultado, pase el parametro `show`, ejemplo `Python3 dolar.py show`

## Modulo en Polybar

[module/dolar]  
type = custom/script  
exec = ~/.config/polybar/hack/scripts/dolar.py  
interval = 60*15  
click-left = ~/.config/polybar/hack/scripts/dolar.py show | rofi -dmenu -theme ~/.config/polybar/hack/scripts/rofi/dolar.rasi -p "Precio del Dolar"  
content = "%output%"
