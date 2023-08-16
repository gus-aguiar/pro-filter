"""Arquivo que estudantes devem editar"""
# initial commit


def get_path_depth(file_path):
    return file_path.count("/")


def show_deepest_file(context):
    if not context["all_files"]:
        print("No files found")
    else:
        deepest_file = max(context["all_files"], key=get_path_depth)
        print(f"Deepest file: {deepest_file}")


def find_file_by_name(context, search_term, case_sensitive=True):
    if not search_term:
        return []

    found_files = []

    search_term = search_term if case_sensitive else search_term.lower()

    for path in context["all_files"]:
        file_name = path.split("/")[-1]
        file_name = file_name if case_sensitive else file_name.lower()

        if search_term in file_name:
            found_files.append(path)

    return found_files
