# Сайт проекта Неодим БСЗ

Вики сайт проекта Неодим БСЗ.

## Локальный запуск сайта документации

Репозиторий использует **MkDocs** + **Material for MkDocs**.

### Требования

- Python 3.8 или новее
- pip (обычно идёт вместе с Python)
- git (чтобы клонировать репозиторий)

### Вариант 1. Установка через виртуальное окружение (рекомендуется)

#### Windows

1. Откройте **PowerShell** или **Командную строку** (cmd) от имени администратора

2. Клонируйте репозиторий (если ещё не сделали):
   ```bash
   git clone https://github.com/inscrut/neodim-bsz.git
   cd neodim-bsz
   ```

3. Создайте и активируйте виртуальное окружение:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
   или в cmd:
   ```cmd
   python -m venv .venv
   .venv\Scripts\activate.bat
   ```

4. Установите зависимости:
   ```bash
   python.exe -m pip install --upgrade pip
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. Запустите локальный сервер разработки:
   ```bash
   mkdocs serve -a 0.0.0.0:3000 --livereload
   ```

6. Откройте в браузере:
   - на этом же компьютере → http://127.0.0.1:3000
   - или http://localhost:3000

**Важно для Windows**: если сайт не открывается с другого устройства → разрешите входящие соединения в Windows Firewall для порта 3000 (или временно отключите firewall для теста).

#### Linux (Ubuntu / Debian / Fedora и др.)

1. Установите git и python (если ещё не стоят):
   ```bash
   sudo apt update
   sudo apt install -y git python3 python3-venv python3-pip    # Ubuntu/Debian
   # или
   sudo dnf install -y git python3 python3-pip                 # Fedora
   ```

2. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/inscrut/neodim-bsz.git
   cd neodim-bsz
   ```

3. Создайте и активируйте виртуальное окружение:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Установите зависимости:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. Запустите сервер:
   ```bash
   mkdocs serve -a 0.0.0.0:3000
   ```

6. Откройте в браузере:
   - http://localhost:3000 (на этой же машине)
   - http://<ваш-ip>:3000 (с другого устройства)

### Полезные команды

```bash
mkdocs serve                 # обычный запуск (только localhost)
mkdocs serve -a 0.0.0.0:3000 # доступ со всех интерфейсов
mkdocs build                 # собрать статический сайт в папку site/
mkdocs build --clean         # пересобрать с нуля
```
