##
from uifunc import *


@FolderSelector
def folder_selector(folder_path: str) -> str:
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
import sys
sys.argv = [sys.argv[0]]

def test_folders():
    folder_selector()


def test_save_folders():
    save_folder_selector()


def test_file():
    file_selector()


def test_files():
    files_selector()


def test_save():
    save_selector()
