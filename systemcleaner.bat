@echo off
@echo.
@echo.
@echo.
@echo.
@echo.   welcome to guanran928 and nongbaobao's system cleaner (unfinished)
@echo.   1 = remove all cache and logs (safe)
@echo.   2 = remove all cache + recycle bin (unsafe, check whats in ur recycle bin first)
@echo.   3 = exit
@echo.   4 = disable hibernate to free 5 - 10 GB of space
@echo.   5 = enable hibernate
@echo.
@echo.
@echo.
@echo.   p.s. nongbaobao did nothing for this script idk why i added him to credit lol
choice /C 123 /N /M "Enter mode here:"

if '%choice%'=='1' goto 1
if '%choice%'=='3' goto end
if '%choice%'=='4' goto 4
:: yes ik weird logic

del /F /Q %systemdrive%\$Recycle.Bin\*

1:

del /Q %temp%\*
:: remove temp folder

del /Q %appdata%\Tencent\Log\*
:: remove qq logs

del /Q "%userprofile%\AppData\Local\Microsoft\Edge\User Data\Default\Code Cache\js\*"
del /Q "%userprofile%\AppData\Local\Microsoft\Edge\User Data\Default\Code Cache\wasm\*"
del /Q "%userprofile%\AppData\Local\Microsoft\Edge\User Data\ShaderCache\GPUCache\*"
del /Q "%userprofile%\AppData\Local\Microsoft\Edge\User Data\Default\Cache\*"
:: remove edge cache

del /Q "%userprofile%\AppData\Local\Google\Chrome\User Data\Default\Code Cache\js\*"
del /Q "%userprofile%\AppData\Local\Google\Chrome\User Data\Default\Code Cache\wasm\*"
del /Q "%userprofile%\AppData\Local\Google\Chrome\User Data\ShaderCache\GPUCache\*"
del /Q "%userprofile%\AppData\Local\Google\Chrome\User Data\Default\Cache\*"
:: remove chrome cache

del /Q %userprofile%\AppData\Local\Microsoft\Windows\INetCache\IE\*
del /Q %userprofile%\AppData\Local\Microsoft\Windows\WebCache\*
:: remove fucking slowest browser's cache

del /Q %userprofile%\AppData\Roaming\discord\Cache\*
:: remove discord cache

del /Q %appdata%\.minecraft\logs\*
del /Q %appdata%\.minecraft\crash-reports\*
::YES REMOVE MINCRAFT LOG AND CRASH REPORT

del /Q %appdata%\tutor-electron-student\Cache\*
del /Q %appdata%\tutor-electron-student\logs\*
:: YES REMOVE 猿辅导 CACHE & LOGS

:end
@echo Cleanup completed :D, Have a good day!
pause
exit
:: yes we r doing this polite

:4
powercfg /off hibernate
goto end

:5
powercfg /on hibernate
goto end
