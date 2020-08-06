def is_file_corrupted(filename: str) -> bool:
    """
    a corrupted file is a file that ends with '_corrupted'
    :param filename: name of the file to check
    :return: True if file is corrupted, else False
    """
    if filename.endswith("_corrupted"):
        return True
    return False
