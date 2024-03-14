:: Check if the folder "folder1" exists
if exist new_folder (
    ::if exist then create new folder
    mkdir if_folder
) else (
    ::if no
    mkdir new-projects
)

:: check if 'if_folder' exists

if exist if_folder (
    ::if exists
    mkdir hyperionDev
) else (
    :: if no
    mkdir new-projects
)

