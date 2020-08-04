
# TODO - create exception? use existing?
    # if there is no exception class that fits the requirement

def is_file_corrupted(filename: str) -> bool:
    """
    a corrupted file is a file that ends with '_corrupted'
    :param filename: name of the file to check
    :return: True if file is corrupted, else False
    """
    pass

def add_files_to_db(): # TODO - document better
    """
    Go over a list of filenames, and add the non corrupted files to the database
    :return:
    """
    # get the JSON from the request
    # https://stackoverflow.com/questions/20001229/how-to-get-posted-json-in-flask
    # parse the JSON and get the list of files
    # for each file in the files:
    # if file is not corrupted, add it to the database
    pass

