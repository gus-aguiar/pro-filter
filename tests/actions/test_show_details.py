import pytest
from datetime import datetime
from pro_filer.actions.main_actions import show_details  # NOQA


@pytest.fixture
def create_temp_file(tmp_path):
    file_content = "Hello, world!"
    temp_file_path = tmp_path / "temp_file.txt"

    with open(temp_file_path, "w") as temp_file:
        temp_file.write(file_content)

    return temp_file_path


@pytest.fixture
def create_temp_directory(tmp_path):
    temp_dir = tmp_path / "temp_directory"
    temp_dir.mkdir()
    return temp_dir


def test_show_details_file(create_temp_file, capsys):
    context = {"base_path": str(create_temp_file)}
    show_details(context)
    captured = capsys.readouterr()
    assert "File name: temp_file.txt" in captured.out
    assert "File size in bytes:" in captured.out
    assert "File type: file" in captured.out
    assert "File extension: .txt" in captured.out
    assert "Last modified date:" in captured.out


def test_show_details_directory(create_temp_directory, capsys):
    context = {"base_path": str(create_temp_directory)}
    show_details(context)
    captured = capsys.readouterr()
    assert "File name: temp_directory" in captured.out
    assert "File size in bytes:" in captured.out
    assert "File type: directory" in captured.out
    assert "File extension: [no extension]" in captured.out
    assert "Last modified date:" in captured.out


def test_show_details_nonexistent_file(capsys):
    context = {"base_path": "nonexistent_file.txt"}
    show_details(context)
    captured = capsys.readouterr()
    assert "File 'nonexistent_file.txt' does not exist" in captured.out


def test_show_details_date_format(create_temp_file, capsys):
    context = {"base_path": str(create_temp_file)}
    show_details(context)
    captured = capsys.readouterr()
    date_caputerd = captured.out.splitlines()[-1]
    assert date_caputerd == "Last modified date: " + f"{datetime.now().date()}"
