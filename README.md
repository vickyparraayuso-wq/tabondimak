# Katia Vidal — bot de Discord

Este bot envía, a intervalos aleatorios, exactamente uno de estos mensajes:

- `dejadme en paz joeee!!`
- `Parad ya!!!`
- `no os metáis conmigo!!`

## 1. Instalar

Necesitas Python 3.10 o superior.

```bash
pip install -U discord.py
```

## 2. Crear la aplicación/bot

En Discord Developer Portal:

1. Crea una nueva Application.
2. Entra en **Bot** y pulsa **Add Bot**.
3. En **Bot > Profile**, establece el nombre visible como `Katia Vidal`.
4. Sube `avatar.jpeg` como avatar.
5. Copia el token del bot. **No lo publiques ni lo compartas.**
6. En **OAuth2 > URL Generator**, selecciona `bot` y dale permiso para **View Channel** y **Send Messages**.
7. Invítalo a tu servidor.

El bot debe presentarse como un bot y no como una persona real si la imagen/nombre pertenecen a una persona real.

## 3. Obtener el ID del canal

Activa el **Developer Mode** de Discord y copia el ID del canal donde quieres que escriba.

## 4. Configurar el token y el canal

### Windows PowerShell

```powershell
$env:DISCORD_TOKEN="TU_TOKEN"
$env:DISCORD_CHANNEL_ID="123456789012345678"
python bot.py
```

### macOS/Linux

```bash
export DISCORD_TOKEN="TU_TOKEN"
export DISCORD_CHANNEL_ID="123456789012345678"
python bot.py
```

## 5. Frecuencia

Por defecto espera entre **15 y 60 minutos** antes de cada mensaje.

Puedes cambiar estas líneas de `bot.py`:

```python
MIN_DELAY = 15 * 60
MAX_DELAY = 60 * 60
```

Por ejemplo, para que escriba entre 1 y 5 minutos:

```python
MIN_DELAY = 60
MAX_DELAY = 5 * 60
```
