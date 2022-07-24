file_path = 'righe.txt'

with open(file_path, 'r') as f:
    linelist = f.readlines()
    num_of_row = len(linelist)
    if num_of_row > 0:
        num_column = len(linelist[0].split(','))

        matrix = []
        for x in range(num_column):
            row = []
            for i in range(num_column):
                row.append('0')
            matrix.append(row)
        print(matrix)

        sum = ['0' for i in range(num_column)]
        print(sum)

        for i in range(num_column):
            for line in linelist:
                line_splitted = line.replace('\n', '').split(',')
                sum[i] = str(int(sum[i]) + int(line_splitted[i]))
        print(sum)
                
        for x in range(num_column):
            matrix[x][x] = str(sum[x])
        print(matrix)

        with open('file_dove_scrivere.txt', 'w') as wf:
            for i in range(len(matrix)):
                wf.write(' '.join(matrix[i]))
                wf.write('\n')