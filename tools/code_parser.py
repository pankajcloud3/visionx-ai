def read_code_file(file_path):
    """
    Read source code from file.
    """

    try:
        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()

    except Exception as e:
        return f"Error reading file: {e}"