@echo off

title MazdakOS Fun Toolbox Builder

echo.
echo ==========================================
echo     MAZDAKOS FUN TOOLBOX BUILDER
echo ==========================================
echo.

echo [1/6] Closing old Toolbox process...

taskkill /F /IM MazdakOS-Fun-Toolbox.exe >nul 2>&1

echo.
echo [2/6] Cleaning old build...

if exist dist rmdir /s /q dist
if exist build rmdir /s /q build

if exist MazdakOS-Fun-Toolbox.spec (
    del /q MazdakOS-Fun-Toolbox.spec
)

echo.
echo [3/6] Checking PyInstaller...

python -m PyInstaller --version

if errorlevel 1 (
    echo.
    echo ERROR: PyInstaller is not available.
    echo.
    pause
    exit /b 1
)

echo.
echo [4/6] Building application...

python -m PyInstaller ^
    --clean ^
    --noconfirm ^
    --onedir ^
    --windowed ^
    --name "MazdakOS-Fun-Toolbox" ^
    main.py

if errorlevel 1 (
    echo.
    echo ERROR: Build failed.
    echo.
    pause
    exit /b 1
)

echo.
echo [5/6] Copying Toolbox programs...

xcopy "apps" "dist\MazdakOS-Fun-Toolbox\apps" /E /I /Y >nul
xcopy "pranks" "dist\MazdakOS-Fun-Toolbox\pranks" /E /I /Y >nul
xcopy "tools" "dist\MazdakOS-Fun-Toolbox\tools" /E /I /Y >nul

echo.
echo [6/6] Build complete!
echo.

echo ==========================================
echo Output:
echo.
echo dist\MazdakOS-Fun-Toolbox\
echo.
echo     MazdakOS-Fun-Toolbox.exe
echo     apps\
echo     pranks\
echo     tools\
echo     _internal\
echo ==========================================
echo.

pause