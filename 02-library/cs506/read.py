def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    with open(csv_file_path, 'r') as file:
        stuff = []
        lines = file.readlines()
        for line in lines:
            r = []
            for item in line.split(','):
                try:
                    r.append(float(item.strip()))
                except:
                    r.append(item.strip().replace('"', ''))
            stuff.append(r)
        return stuff