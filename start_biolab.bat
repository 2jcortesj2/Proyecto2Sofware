@echo off
echo ========================================
echo   BioLab LIS - Iniciando Sistema
echo ========================================
echo.

REM Obtener la ruta del script
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"

echo [1/2] Iniciando Backend Django...
start "Django Backend" cmd /k "env\Scripts\activate && cd backend && python manage.py runserver"

timeout /t 3 /nobreak >nul

echo [2/2] Iniciando Frontend Vue...
start "Vue Frontend" cmd /k "cd frontend && npm run dev"

echo.
echo ========================================
echo   Sistema iniciado correctamente!
echo ========================================
echo   Backend:  http://127.0.0.1:8000
echo   Frontend: http://localhost:5173
echo ========================================
echo.
echo Presiona cualquier tecla para salir...
pause >nul