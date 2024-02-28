# -*- coding:utf-8-*-
import os
import logging
import shutil


logging.basicConfig(level=logging.INFO, format='%(asctime)s  %(levelname)s  %(message)s')
compressed_file_suffix = (".tar", ".tar.gz", ".tar.bz2")


def dataset_cutter(sourcedata, split_number, basename='', delimiter='\n', locate_dir=None):
    if os.path.isdir(sourcedata):
        return split_dir(sourcedata, split_number, basename, locate_dir)
    elif sourcedata.endswith(compressed_file_suffix):
        return split_compressed_file(sourcedata, split_number, locate_dir, basename)
    else:
        return split_file(sourcedata, split_number, basename, delimiter, locate_dir)


def split_file(sourcefile, split_number, basename='', delimiter='\n', locate_dir=None):
    """
    split file
    :param sourcefile:string
    :param split_number:int
    :param basename: string
    :param delimiter: string
    :param dir_name: string
    :return: list, split_files
    """
    if not basename:
        base_name = os.path.basename(sourcefile)
    else:
        base_name = basename
    if not locate_dir:
        locate_dir = sourcefile.rsplit('/', 1)[0]
    split_files = [os.path.join(locate_dir, str(i) + '_' + base_name) for i in range(1, split_number+1)]
    writer_list = [open(i, 'wb') for i in split_files]

    with open(sourcefile, 'rb') as reader:
        header_remain_file_end = (".csv")
        if sourcefile.endswith(header_remain_file_end):
            headline = reader.readline()
            for w in writer_list:
                w.write(headline)

        if delimiter == '\n' or not delimiter:
            for w in writer_list:
                j = 0
                for line in reader:
                    writer_list[j].write(line)
                    j += 1
                    if j == split_number:
                        j = 0
        else:
            delimiter = delimiter.encode()
            for w in writer_list:
                pattern = 2
                first_line = reader.readline()
                if first_line.strip() == delimiter:
                    pattern = 1

                j = 0
                writer_list[j].write(first_line)
                if pattern == 2:
                    for line in reader:
                        writer_list[j].write(line)
                        if line.strip() != delimiter:
                            continue
                        j += 1
                        if j == split_number:
                            j = 0
                else:
                    for line in reader:
                        if line.strip() != delimiter:
                            writer_list[j].write(line)
                            continue
                        else:
                            j += 1
                            if j == split_number:
                                j = 0
                            writer_list[j].write(line)
                            continue
    for f in writer_list:
        f.close()
    will_rm = []
    for f in split_files:
        try:
            if not os.path.getsize(f):
                will_rm.append(f)
                continue
        except FileNotFoundError:
            will_rm.append(f)
            continue
    if will_rm:
        for f in will_rm:
            split_files.remove(f)
    return split_files


def split_dir(sourcedir, split_number, basename='', locate_dir=None, mode="copy"):
    """
    split file
    :param sourcedata:string
    :param split_number:int
    :param basename: string
    :param locate_dir: string
    :param mode: string, copy or move
    :return: list
    """
    if os.path.isfile(sourcedir):
        return []
    if not basename:
        base_name = os.path.basename(sourcedir)
    else:
        base_name = basename
    if not locate_dir:
        locate_dir = sourcedir.rsplit('/', 1)[0]
    split_dirs = [os.path.join(locate_dir, str(i) + '_' + base_name) for i in range(1, split_number+1)]
    for d in split_dirs:
        os.mkdir(d)
    cursor = 0
    for i in sorted(os.listdir(sourcedir)):
        i_path = os.path.join(sourcedir, i)
        destination = os.path.join(split_dirs[cursor], os.path.basename(i_path))
        if mode == "move":
            shutil.move(i_path, destination)
        else:
            if os.path.isfile(i_path):
                shutil.copy(i_path, destination)
            else:
                shutil.copytree(i_path, destination, symlinks=True)
        cursor += 1
        if cursor == split_number:
            cursor = 0
    will_rm = []
    for d in split_dirs:
        try:
            if not os.listdir(d):
                will_rm.append(d)
                continue
        except:
            continue
    if will_rm:
        for d in will_rm:
            split_dirs.remove(d)
    return split_dirs


def split_compressed_file(compressed_file, split_number, locate_dir, basename=''):
    """
    split a compressed file
    :param compressed_file:string
    :param split_number:int
    :param basename: string
    :param locate_dir: string
    :return: list
    """
    if not os.path.isfile(compressed_file):
        return []
    if os.listdir(locate_dir):
        return []
    commands = {
        "tar": "tar xf {} -C {}",
        "tar.gz": "tar zxf {} -C {}",
        "tar.bz2": "tar jxf {} -C {}",
        }
    file_suffix = "tar" + compressed_file.rsplit(".tar", 1)[-1]
    if file_suffix not in commands:
        return []
    if not basename:
        basename = os.path.basename(compressed_file).split(".", 1)[0]
    extract_result = os.system(commands[file_suffix].format(compressed_file, locate_dir))
    if int(extract_result) != 0:
        print("dataset {} split failed with code {}".format(os.path.basename(compressed_file), extract_result))
        return []
    split_source_dir = os.path.join(locate_dir, os.listdir(locate_dir)[0])
    split_dirs = split_dir(split_source_dir, split_number, basename, locate_dir, mode="move")
    shutil.rmtree(split_source_dir)
    return split_dirs


if __name__ == '__main__':
    sourcedata = ""
    split_number = 50
    delimiter = '\n'
    locate_dir = None
    dataset_cutter(sourcedata=sourcedata, split_number=split_number, delimiter=delimiter, locate_dir=locate_dir)
