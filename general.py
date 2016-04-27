import os


# For each website we crawl, the program will generate an individual folder to store the result
def create_result_dir(directory):
    if not os.path.exists(directory):
        print("Creating project directory " + directory)
        os.makedirs(directory)


# Create link queues and already crawled files
def create_data_files(project_name, home_url):
    queue = project_name + '/!queue.txt'
    crawled = project_name + '/!crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, home_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Create a new file
def write_file(path, data):
    file = open(path, 'w')
    file.write(data)
    file.close()


# Add data to an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')  # Add data to the end of file, then add a new line


# Clear the contents of a file
def delete_file_contents(path):
    with open(path, 'w'):
        pass  # pass keyword = 'do nothing'; this function essentially make a new file with the same name.


# Read a file and scan all the lines and convert them into set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))  # so the '\n' character won't corrupt the result

    return results


# Iterate through a set, each item will be a new line in the file
def set_to_file(set_items, file):
    delete_file_contents(file)
    for set_items in sorted(set_items):
        append_to_file(file, set_items)