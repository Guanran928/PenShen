@echo off
@echo.
@echo.
@echo.
@echo.
@echo.   welcome to lunar client launcher! by Guanran928!
@echo.   1 = 1.7
@echo.   2 = 1.8
@echo.   3 = exit
@echo.
@echo.
@echo.
@echo.
@echo.
choice /C 123 /N /M "Enter version here:"

if '%choice%'=='1' goto 1.7
if '%choice%'=='2' goto 1.8
if '%choice%'=='3' exit

start javaw.exe --add-modules jdk.naming.dns --add-exports jdk.naming.dns/com.sun.jndi.dns=java.naming -Djna.boot.library.path="%USERPROFILE%\.lunarclient\offline\1.7\natives" --add-opens java.base/java.io=ALL-UNNAMED -Xmx4G -Djava.library.path="%USERPROFILE%\.lunarclient\offline\1.7\natives" -cp "%USERPROFILE%\.lunarclient\offline\1.7\lunar-assets-prod-1-optifine.jar";"%USERPROFILE%\.lunarclient\offline\1.7\lunar-assets-prod-2-optifine.jar";"%USERPROFILE%\.lunarclient\offline\1.7\lunar-assets-prod-3-optifine.jar";"%USERPROFILE%\.lunarclient\offline\1.7\lunar-libs.jar";"%USERPROFILE%\.lunarclient\offline\1.7\lunar-prod-optifine.jar";"%USERPROFILE%\.lunarclient\offline\1.7\OptiFine.jar";"%USERPROFILE%\.lunarclient\offline\1.7\vpatcher-prod.jar" com.moonsworth.lunar.patcher.LunarMain --version 1.7 --accessToken 0 --assetIndex 1.7 --userProperties {} --gameDir "%APPDATA%\.minecraft" --texturesDir "%USERPROFILE%\.lunarclient\textures" --width 854 --height 480 & exit


:1.7
start javaw.exe --add-modules jdk.naming.dns --add-exports jdk.naming.dns/com.sun.jndi.dns=java.naming -Djna.boot.library.path="%USERPROFILE%\.lunarclient\offline\1.8\natives" --add-opens java.base/java.io=ALL-UNNAMED -Xmx4G -Djava.library.path="%USERPROFILE%\.lunarclient\offline\1.8\natives" -cp "%USERPROFILE%\.lunarclient\offline\1.8\lunar-assets-prod-1-optifine.jar";"%USERPROFILE%\.lunarclient\offline\1.8\lunar-assets-prod-2-optifine.jar";"%USERPROFILE%\.lunarclient\offline\1.8\lunar-assets-prod-3-optifine.jar";"%USERPROFILE%\.lunarclient\offline\1.8\lunar-libs.jar";"%USERPROFILE%\.lunarclient\offline\1.8\lunar-prod-optifine.jar";"%USERPROFILE%\.lunarclient\offline\1.8\OptiFine.jar";"%USERPROFILE%\.lunarclient\offline\1.8\vpatcher-prod.jar" com.moonsworth.lunar.patcher.LunarMain --version 1.8 --accessToken 0 --assetIndex 1.8 --userProperties {} --gameDir "%APPDATA%\.minecraft" --texturesDir "%USERPROFILE%\.lunarclient\textures" --width 854 --height 480 & exit
::Command made by Aetopia and Lemons#2555, Edited By Guanran928