# Code to show how we can read data from a CSV

import csv
import pandas

# importd pandas so that we can see the CSV output in a readable format


class test_CRUD(object):
    def test_update_1(self):
        # Read a file
        with open('/Users/datashan/Desktop/Test Automation/Py3xLearning/Ex_26072024/testdata.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row[0], row[1])

    def test_update_2(self):
        df = pandas.read_csv('/Users/datashan/Desktop/Test Automation/Py3xLearning/Ex_26072024/testdata.csv')
        print(df)


crud = test_CRUD()
crud.test_update_1()
crud.test_update_2()
