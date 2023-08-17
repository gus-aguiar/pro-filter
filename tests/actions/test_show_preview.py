import pytest
from pro_filer.actions.main_actions import show_preview

test_params = [
    (
        {
            "all_files": [
                "src/__init__.py",
                "src/app.py",
                "src/utils/__init__.py",
            ],
            "all_dirs": ["src", "src/utils"],
        },
        "Found 3 files and 2 directories\n"
        "First 5 files: ['src/__init__.py', "
        "'src/app.py', 'src/utils/__init__.py']\n"
        "First 5 directories: ['src', 'src/utils']\n",
    ),
    ({"all_files": [], "all_dirs": []}, "Found 0 files and 0 directories\n"),
    (
        {
            "all_files": [
                "src/__init__.py",
                "src/app.py",
                "src/utils/__init__.py",
                "src/utils/second.py",
                "src/utils/third.py",
                "src/utils/fourth.py",
            ],
            "all_dirs": ["src", "src/utils"],
        },
        "Found 6 files and 2 directories\n"
        "First 5 files: "
        "['src/__init__.py', 'src/app.py', 'src/utils/__init__.py', "
        "'src/utils/second.py', 'src/utils/third.py']\n"
        "First 5 directories: "
        "['src', 'src/utils']\n",
    ),
]


@pytest.mark.parametrize("context, expected_output", test_params)
def test_show_preview(capsys, context, expected_output):
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == expected_output


# aqui haveria a opção de ficar menos verboso, fazendo 3 testes diferentes,
# com a mesma função, mas com diferentes parâmetros.
# Mas como estamos estudando parametrização,
# optei por deixar como está.
