import pytest
from unittest.mock import Mock, patch
from pro_filer.actions.main_actions import show_disk_usage  # NOQA


@pytest.fixture
def create_temp_file_one(tmp_path):
    file_content = "Hello, world!"
    temp_file_path = tmp_path / "temp_file_one.txt"

    with open(temp_file_path, "w") as temp_file:
        temp_file.write(file_content)

    return temp_file_path


@pytest.fixture
def create_temp_file_two(tmp_path):
    file_content = "Hello, universe!"
    temp_file_path = tmp_path / "temp_file_two.txt"

    with open(temp_file_path, "w") as temp_file:
        temp_file.write(file_content)

    return temp_file_path


def test_show_disk_usage(create_temp_file_one, create_temp_file_two, capsys):
    context = {
        "all_files": [
            str(create_temp_file_one),
            str(create_temp_file_two),
        ]
    }
    mock_get_printable_file_path = Mock(
        return_value="path/do/the/file/file.txt"
    )
    with patch(
        "pro_filer.actions.main_actions._get_printable_file_path",
        mock_get_printable_file_path,
    ):
        show_disk_usage(context)
    captured = capsys.readouterr()
    print(captured.out)
