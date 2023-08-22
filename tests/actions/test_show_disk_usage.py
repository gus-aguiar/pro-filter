from pro_filer.actions.main_actions import show_disk_usage  # NOQA
import pytest
from unittest.mock import patch


@pytest.fixture
def create_temp_file_one(tmp_path):
    file_content = "Hello, world!"
    temp_file_path = tmp_path / "temp_file_one.txt"

    with open(str(temp_file_path), "w") as temp_file:
        # estou usando str(temp_file_path) porque se não for string o open não
        # funciona e originalmente o temp_file_path é um objeto
        # Path e não uma string.
        temp_file.write(file_content)

    return temp_file_path


@pytest.fixture
def create_temp_file_two(tmp_path):
    file_content = "Hello, universe!"
    temp_file_path = tmp_path / "temp_file_two.txt"

    with open(str(temp_file_path), "w") as temp_file:
        temp_file.write(file_content)

    return temp_file_path


def test_show_disk_usage(create_temp_file_one, create_temp_file_two, capsys):
    context = {
        "all_files": [
            str(create_temp_file_one),
            str(create_temp_file_two),
        ]
    }

    show_disk_usage(context)
    captured = capsys.readouterr()
    date_captuerd = captured.out.splitlines()
    assert len(date_captuerd) == 3
    assert "temp_file_one.txt" in date_captuerd[1]
    assert "temp_file_two.txt" in date_captuerd[0]
    assert "Total size:" in date_captuerd[2]


def test_show_disk_usage_no_files(capsys):
    context = {"all_files": []}

    show_disk_usage(context)
    captured = capsys.readouterr()
    assert captured.out == "Total size: 0\n"


def test_show_disk_usage_wrong_size_calculation(
    create_temp_file_one, create_temp_file_two, capsys
):
    context = {
        "all_files": [
            str(create_temp_file_one),
            str(create_temp_file_two),
        ]
    }
    with patch(
        "pro_filer.actions.main_actions.os.path.getsize", return_value=10
    ):
        show_disk_usage(context)
    captured = capsys.readouterr()
    captured_lines = captured.out.splitlines()

    assert captured_lines[-1] == "Total size: 20"


def test_show_disk_usage_with_inexistent_file(
    create_temp_file_one, create_temp_file_two, capsys
):
    context = {
        "all_files": [
            str(create_temp_file_one),
            str(create_temp_file_two),
            "inexistent_file.txt",
        ]
    }
    with pytest.raises(FileNotFoundError):
        show_disk_usage(context)


def test_show_disk_usage_order_of_sizes(
    create_temp_file_one, create_temp_file_two, capsys
):
    context = {
        "all_files": [
            str(create_temp_file_one),
            str(create_temp_file_two),
        ]
    }
    show_disk_usage(context)
    captured = capsys.readouterr()
    captured_lines = captured.out.splitlines()
    percentage1 = captured_lines[0].split()[-1].strip("()%")
    percentage2 = captured_lines[1].split()[-1].strip("()%")
    assert percentage1 > percentage2


# Exemplo de mock :
# mock_get_printable_file_path = Mock(
#     return_value="path/do/the/file/file.txt"
# )
# with patch(
#     "pro_filer.actions.main_actions._get_printable_file_path",
#     mock_get_printable_file_path,
# ):
