@ECHO OFF
@SET PYTHONIOENCODING=utf-8
@SET PYTHONUTF8=1
@FOR /F "tokens=2 delims=:." %%A in ('chcp') do for %%B in (%%A) do set "_CONDA_OLD_CHCP=%%B"
@chcp 65001 > NUL
@CALL "C:\Users\yezon\miniforge3\condabin\conda.bat" activate "c:\Users\yezon\OneDrive\Documents\Github\social_competiton_elo_rating\.conda"
@IF %ERRORLEVEL% NEQ 0 EXIT /b %ERRORLEVEL%
@c:\Users\yezon\OneDrive\Documents\Github\social_competiton_elo_rating\.conda\python.exe -Wi -m compileall -q -l -i C:\Users\yezon\AppData\Local\Temp\tmp29e0bmx9 -j 0
@IF %ERRORLEVEL% NEQ 0 EXIT /b %ERRORLEVEL%
@chcp %_CONDA_OLD_CHCP%>NUL
