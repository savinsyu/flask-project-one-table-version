#!/bin/bash
ECHO "Убиваем все процессы python"
./kill_python.ps1
ECHO "Заново запускаем приложение"
./start_app.sh