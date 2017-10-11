##
from uifunc import *
sys.argv = [sys.argv[0]]


@FolderSelector
def folder_selector(folder_path: str) -> str:
    return folder_path


@FoldersSelector
def folders_selector(folder_path: List[str]) -> List[str]:
    return folder_path


@SaveFolderSelector
def save_folder_selector(folder_path: str) -> str:
    return folder_path


@FileSelector(['.txt'])
def file_selector(file_path: str) -> str:
    return file_path


@FilesSelector(['.txt'])
def files_selector(file_paths: List[str]) -> List[str]:
    return file_paths


@SaveSelector(['.txt'])
def save_selector(file_path: str) -> str:
    return file_path


##
def test_folder():
    folder_selector()


def test_folders():
    folders_selector()


def test_save_folders():
    save_folder_selector()


def test_file():
    file_selector()


def test_files():
    files_selector()


def test_save():
    save_selector()
##
