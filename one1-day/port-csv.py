import csv



with open('one.csv') as csv_file:
    csv_reader = csv.reader(csv_file , delimiter=',')
    line_count = 0 
    for row in csv_reader:
        if line_count == 0:
            print(f'           {"   ".join(row)}')
            line_count+=1
        else:
            print(f'\t{row[0]}-01-01  {row[1]} {row[2]}')
            line_count+=1








#with open('table4.csv','r') as csv_file:
#    csv_reader = csv.DictReader(csv_file)

#    with open('new_names.csv', 'w') as new_file:
#        fieldnames = ['first_name','last_name']

#        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames ,delimiter='\t')

#        csv_writer.writeheader()

#        for line in csv_reader:
#            del line['email']
#            csv_writer.writerow(line)
