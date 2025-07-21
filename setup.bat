@echo off
chcp 65001 >nul
echo Скачиваем Python portable...
curl -L -o python-portable.zip https://github.com/indygreg/python-build-standalone/releases/download/20240505/cpython-3.11.9+20240505-x86_64-pc-windows-msvc-shared-install_only.tar.gz

echo Распаковываем...
tar -xf python-portable.zip
move python-install py-portable
del python-portable.zip

echo Устанавливаем pip...
py-portable\python.exe -m ensurepip

echo Устанавливаем transliterate...
py-portable\python.exe -m pip install transliterate

echo Создаем data папку...
mkdir data

echo Скачиваем rename_translit.py...
curl -L -o rename_translit.py https://raw.githubusercontent.com/da0ab/rename-translit/main/rename_translit.py

echo Создаем run.bat...
echo @echo off > run.bat
echo chcp 65001 ^>nul >> run.bat
echo cd /d %%~dp0 >> run.bat
echo py-portable\python.exe rename_translit.py data >> run.bat
echo pause >> run.bat

echo Готово! Положите файлы в папку data и запустите run.bat
pause
