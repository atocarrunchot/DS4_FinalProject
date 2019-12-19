import gzip
import shutil
import os


def unzip_gz(path_in, path_out, extension='gz'):
    """
    Unzips total files with the extension given from path_in to path_out.

    :param path_in: the path where files are located in.
    :param path_out: the path where unzipped files will be located.
    :param extension: file extension to be unzipped.
    :return: None
    """
    list_files = [i for i in os.listdir(path_in) if i[-len(extension):] == extension]

    for file_in in list_files:
        print(file_in)
        in_filename = f'{path_in}/{file_in}'
        out_filename = f'{path_out}/{file_in[:-3]}'

        with gzip.open(in_filename, 'rb') as f_in:
            with open(f'{out_filename}', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)


if __name__ == '__main__':
    unzip_gz(path_in='../data/chirps/gz', path_out='../raster')
    pass
