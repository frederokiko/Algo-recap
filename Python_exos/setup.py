from cx_Freeze import setup, Executable

setup(
    name="Listdetache",
    version="0.1",
    description="To-Do List Application",
    executables=[Executable("oktodowindows.py")]
)


