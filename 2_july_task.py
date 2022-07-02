import logging

logging.basicConfig(filename="sting_fun.log", level=logging.INFO, format=('%(levelname)s %(name)s %(asctime)s %(message)s'))

class string_functions:

    def extract_string(self, string1):
        self.string1 = string1
        logging.info("We are inside string function")
        try:
            if len(string1) == 0:
                raise ValueError('empty string')
            changed_str = string1[::3]
            logging.info("Extracted string is %s ", changed_str)
            return changed_str
        except ValueError as e:
            logging.exception(e)

    def reverse_str(self,str1):
        try:
            if len(str1) == 0:
                raise ValueError('empty string')
            logging.info("Reversed string is %s ", str1[::-1])

        except ValueError as e:
            logging.exception(e)

    def upper_split(self,str1):
        try:
            if len(str1) == 0:
                raise ValueError('empty string')
            str1 = str1.upper()
            logging.info("String after converting it in upper case then splitting it %s", str1.split())
        except ValueError as e:
            logging.exception(e)

    def lower_case(self,str1):
        try:
            if len(str1) == 0:
                raise ValueError('empty string')
            str1 = str1.lower()
            logging.info("String after converting it in lowercase %s", str1)
        except ValueError as e:
            logging.exception(e)

    def capitalize_string(self,str1):
        try:
            if len(str1) == 0:
                raise ValueError('empty string')
            str1 = str1.capitalize()
            logging.info("String after capitalizing it %s", str1)
        except ValueError as e:
            logging.exception(e)

string_input = "this is My First Python programming class and i am learNING python string and its function"
user_string = string_functions()
user_string.extract_string(string_input)
user_string.reverse_str(string_input)
user_string.upper_split(string_input)
user_string.lower_case(string_input)
user_string.capitalize_string(string_input)

#############################################################################################################################################

class list_function:

    logging.info("We are inside List class")

    def reverse_list(self,li):
        try:
            if len(li) == 0:
                raise ValueError('Empty List')
            logging.info("List after reversing %s", li[::-1])
        except ValueError as e:
            logging.exception(e)

    def access_of_234(self,li):
        try:
            if len(li) == 0:
                raise ValueError('Empty List')
            logging.info("First 234 is available in tuple %s", li[7][0])
            logging.info("Second value is in dictionary %s ", list(li[8].keys())[1])
        except ValueError as e:
            logging.exception(e)

    def access_of_456(self,li):
        try:
            if len(li) == 0:
                raise ValueError('Empty List')
            logging.info("456 is in list %s ", li[5][1])
        except ValueError as e:
            logging.exception(e)

    def extract_list(self,li):
        try:
            if len(li) == 0:
                raise ValueError('Empty List')
            new_li = []
            for i in li:
                if type(i) == list:
                    new_li.append(i)
            logging.info("List that contains only list from original one %s ", new_li)
        except ValueError as e:
            logging.exception(e)

    def extract_sudh(self,li):
        try:
            if len(li) == 0:
                raise ValueError('Empty List')
            logging.info("Extracting of sudh %s", list(li[8].values())[0])
        except ValueError as e:
            logging.exception(e)

    def extract_dict_keys(self,li):
        try:
            if len(li) == 0:
                raise ValueError('Empty List')
            logging.info("Dictionary keys %s ",li[8].keys())
        except ValueError as e:
            logging.exception(e)

    def extract_dict_values(self,li):
        try:
            if len(li) == 0:
                raise ValueError('Empty List')
            logging.info("Dictionary values %s ",li[8].values())
        except ValueError as e:
            logging.exception(e)

l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh", 234:[23,45,656]}]

user_list = list_function()
user_list.reverse_list(l)
user_list.access_of_234(l)
user_list.access_of_456(l)
user_list.extract_list(l)
user_list.extract_sudh(l)
user_list.extract_dict_keys(l)
user_list.extract_dict_values(l)

#########################################################################################################################################

class all_function:
    logging.info("We are inside class where we perform operation on all types of data structure")

    def extract_list(self,li):
        try:
            if len(li) == 0:
                raise ValueError('Empty List')
            new_li = []
            for i in li:
                if type(i)==list:
                    new_li.append(i)
            logging.info("All the list element from original %s",new_li)
        except ValueError as e:
            logging.exception(e)

    def extract_dict(self, li):
        try:
            if len(li) == 0:
                raise ValueError('Empty List')
            for i in li:
                if type(i) == dict:
                    logging.info("All the dictionary element from original %s",i)
        except ValueError as e:
            logging.exception(e)

    def extract_tuple(self, li):
        try:
            if len(li) == 0:
                raise ValueError('Empty List')
            for i in li:
                if type(i) == tuple:
                    logging.info("All the tuple element from original %s",i)
        except ValueError as e:
            logging.exception(e)

    def extract_numeric(self, li):
        try:
            if len(li) == 0:
                raise ValueError('Empty List')
            l1=[]
            for i in li:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
                if type(i)==dict:
                    for k in i.items():
                        for m in k:
                            if type(m)==int:
                                l1.append(m)
            logging.info("All the numeric values in list %s",l1)

        except ValueError as e:
            logging.exception(e)

    def sum_of_numeric(self, li):
        try:
            if len(li) == 0:
                raise ValueError('Empty List')
            l1 = []
            for i in li:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for m in k:
                            if type(m) == int:
                                l1.append(m)
            logging.info("Sum of all numeric elements %s ", sum(l1))
        except ValueError as e:
            logging.exception(e)

    def odd_elements(self, li):
        try:
            if len(li) == 0:
                raise ValueError('Empty List')
            l1 = []
            for i in li:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for m in k:
                            if type(m) == int:
                                l1.append(m)
            odd_li=[]
            for i in l1:
                if i%2==1:
                    odd_li.append(i)
            logging.info("All odd number in list %s",odd_li)
        except ValueError as e:
            logging.exception(e)

    def extract_ineuron(self,li):
        try:
            if len(li) == 0:
                raise ValueError('Empty List')
            logging.info("extracting ineuron   %s   %s", list(li[4].values())[1], li[5][0])
        except ValueError as e:
            logging.exception(e)

    def count1(self,li):
        try:
            if len(li) == 0:
                raise ValueError('Empty List')
            l1 = []
            for i in li:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int or type(i) == str:
                            l1.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for m in k:
                            if type(m) == int or type(i) == str:
                                l1.append(m)
            for i in set(l1):
                print(i,l1.count(i))

        except ValueError as e:
            logging.exception(e)

    def number_keys(self,li):
        try:
            if len(li) == 0:
                raise ValueError('Empty List')
            for i in li:
                if type(i)==dict:
                    num1=len(list(i.keys()))
            logging.info("Number os keys %s", num1)
        except ValueError as e:
            logging.exception(e)

    def string_data(self,li):
        try:
            if len(li) == 0:
                raise ValueError('Empty List')
            l1 = []
            for i in li:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                         if type(i) == str:
                            l1.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for m in k:
                            if type(i) == str:
                                l1.append(m)
            logging.info("All string data %s",l1)

        except ValueError as e:
            logging.exception(e)

    def isalphanumeric(self,li):
        try:
            if len(li) == 0:
                raise ValueError('Empty List')
            l1 = []
            for i in li:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int or type(i) == str:
                            l1.append(j)
                if  type(i) == dict:
                    for k in i.items():
                        for m in k:
                            if type(m) == int or type(i) == str:
                                l1.append(m)
            l1_alpha=[]
            for i in l1:
                if type(i)==str:
                    if i.isalpha():
                        l1_alpha.append(i)
            logging.info("Alphnum list %s",l1_alpha)

        except ValueError as e:
            logging.exception(e)


    def multiply(self, li):
        try:
            if len(li) == 0:
                raise ValueError('Empty List')
            for i in li:
                m=1
                if type(i) == list or type(i)==tuple or type(i)==set:
                    for j in i:
                        if type(j)==int:
                            m=m*j
                    print(m)
                if type(i)==dict:
                    for k in i.items():
                        for n in k:
                            if type(n)==int:
                                m=m*n
                    print(m)

        except ValueError as e:
            logging.exception(e)







l =[[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]),{'k1' : "sudh" , 'k2' :"ineuron", 'k3' : "kumar", 3:6, 7:8}, ["ineuron", "data science"]]

user_all = all_function()
user_all.extract_list(l)
user_all.extract_dict(l)
user_all.extract_tuple(l)
user_all.extract_numeric(l)
user_all.sum_of_numeric(l)
user_all.odd_elements(l)
user_all.extract_ineuron(l)
user_all.count1(l)
user_all.number_keys(l)
user_all.string_data(l)
user_all.isalphanumeric(l)
user_all.multiply(l)


