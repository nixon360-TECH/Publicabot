# Instalación en la PC de Nixon (Windows) — paso a paso

Todo es gratis. Hazlo en orden y marca cada paso. Si algo falla, copia el error en Dispatch o en Claude Code.

## 1. Base
1. **Claude Desktop** (incluye Claude Code y Dispatch): https://claude.com/download
2. **Git for Windows**: https://git-scm.com/download/win
3. **Node.js LTS** (para Remotion): https://nodejs.org
4. **FFmpeg** (respaldo y QA). En PowerShell: `winget install Gyan.FFmpeg`

## 2. Repo
```powershell
git clone https://github.com/nixon360-TECH/Publicabot C:\NBS\publicabot
cd C:\NBS\publicabot
copy .env.example .env    # luego edita MEDIA_ROOT con la ruta real del disco
```

## 3. ArtCraft apps (desde sus Releases en GitHub o con el ArtCraft Launcher)
- FilmCraft: https://github.com/storytold/filmcraft/releases (instalador MSI)
- Opcionales para después: LightCraft, PhotoCraft, EffectCraft (mismo procedimiento)

Registrar FilmCraft en Claude Code (PowerShell, ruta por defecto del MSI):
```powershell
claude mcp add filmcraft -- "$env:LOCALAPPDATA\Programs\ArtCraft\FilmCraft\filmcraft-cli.exe" mcp
```
Comprobar que quedó registrado: `claude mcp list`

## 4. Remotion (capa de subtítulos y diseño) — solo si Nixon aprueba VIDEO_STACK
```powershell
cd C:\NBS\publicabot
npx create-video@latest --yes --blank templates\remotion
cd templates\remotion
npx remotion skills add      # instala las skills oficiales de Remotion para Claude Code
```

## 5. Primera prueba
Abre Claude Code en `C:\NBS\publicabot` y escribe:
> Ejecuta N360-001: audita esta PC (specs, MEDIA_ROOT, FFmpeg, FilmCraft MCP) y actualiza CURRENT_STATE.

## 6. Dispatch
En la app de escritorio: menú lateral → Dispatch → Get started. Vincúlalo con la app de Claude en el celular y da acceso a `C:\NBS\publicabot` y a la carpeta de MEDIA_ROOT.
