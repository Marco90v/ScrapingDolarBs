# ScrapingDolarBs

Script realizado para usar en la `Polybar y Rofi en Linux`

Para usar, ejecuta el script, `Python3 dolar.py` se realizara una peticion a la Web: `https://monitordolarvenezuela.com/`.  
Se extraeran los datos del precio del dolar, tanto para el `Banco Central de Venezuela`, `En Paralelo` y `Binance P2P`.  
Los datos son almacenados en un archivo `JSON` para ser usados cada vez que se necesite mostar, los datos son actualizados cada 15 minutos.  
El archivo es almacenado en la misma ruta del script, en este caso es: `~/.config/polybar/hack/scripts/`

Para mostrar el resultado, pase el parametro `show`, ejemplo `Python3 dolar.py show`

## Modulo en Polybar
```ini
[module/dolar]  
type = custom/script  
exec = ~/.config/polybar/hack/scripts/dolar.py  
interval = 60*15  
click-left = ~/.config/polybar/hack/scripts/dolar.py show | rofi -dmenu -theme ~/.config/polybar/hack/scripts/rofi/dolar.rasi -p "Precio del Dolar"  
content = "%output%"
```

## Formato del JSON
```JSON 
[
    {
        "title": "BCV",
        "amount": "Bs = 16,566"
    },
    {
        "title": "Paralelo",
        "amount": "Bs = 17,45"
    },
    {
        "title": "Binance P2P",
        "amount": "Bs = 17,400"
    }
]
```

## Vista Previa

![Preview](https://github.com/Marco90v/ScrapingDolarBs/blob/main/dolar_polybar_rofi.png)
