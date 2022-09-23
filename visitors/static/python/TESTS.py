import pickle,os,random

'''
CLASS TEST CREATE TEST WITH QUESTIONS AND ANSWERS AND CALCULATE THE STUDENT'S GRADE
'''
class Test:
    #CONSTRACTOR
    def __init__(self):
        p = input("type file path for test : ")
        if not(os.path.exists(p)):
            p = "test.txt"
            print('wrong path for file . file choosed to be in : "{0}".'.format(p))
        self._path = p
        self.create_test()

    def get_Path(self):
        #RETURN PATH FOR TEST FILE
        return _path
    

    def __eq__(self,test2):
        #CHACK WHENEVER 2 TESTS HAVE SIMILAR QUESTION AND ANSWER
        file_test_self = open(self._path,"rb")
        dic_test_self = pickle.load(file_test)
        file_test_test2 = open(test2.getPath(),"rb")
        dic_test_test2 = pickle.load(file_test)
        count=0
        for i in dic_test.keys():
            if (dic_test_self[i][0]==dic_test_test2[i][0]) and (dic_test_self[i][1]==dic_test_test2[i][1]):
                return True
        return False

    def __str__(self):
        #RETURN FOR PRINT PATH FOR TEST FILE
        return self._path
        
    
    def create_test(self):
        #CREATE TEST WITH QUESTIONS AND ANSWERS FOR THE FIRST TIME
        try:
            dic={}
            f_out_test =  open(self._path,'wb') 
            for i in range(1,11):
                num1 = random.randint(1,10)
                num2 = random.randint(1,10)
                o = random.randint(1,4)
                if o == 1:
                    operator = r'+'
                    result = num1+num2
                elif o == 2:
                    operator = r'-'
                    result=num1-num2
                elif o == 3:
                    operator = r'*'
                    result=num1*num2
                else:
                    operator = '\\'
                    result=num1//num2
                dic[i] = [f"{num1}{operator}{num2}"+"=",result]
            pickle.dump(dic,f_out_test)
            f_out_test.close()
            self.print_test()
        except:
            print("error accured . try again.")

    def print_test(self):
        #PRINT TEST TO THE SCREEN AND RECEIVE ANSWERS FROM STUDENT
        s=" "
        try:
            file_test = open(self._path,"rb")
            file_student_answers = open("student_answers.txt",'w')
            dic_test = pickle.load(file_test)
            for i in dic_test.keys():
                result = input(dic_test[i][0])
                s = ","+result 
                file_student_answers.write(s)
            file_student_answers.close()
            file_test.close()
        except:
            print("something wrong with the file . try again.")
        finally:
            input("finish test: ")
            self.calc_grade()
    


    def calc_grade(self):
        #CLACULATE AND PPRINT STUDENT GRADE
        grade = 0
        try:
            file_student_answers = open("student_answers.txt","r")
            file_test = open(self._path,"rb")
            dic_test = pickle.load(file_test)
            l_student_answers = file_student_answers.read().split(",")
            for i in dic_test.keys():
                try:
                    if int(l_student_answers[i]) == dic_test[i][1]:
                        grade+=1
                except:
                    pass
            file_test.close()
            file_student_answers.close()
        except:
            print("something wrong with the file . try again.")
        finally:
            print("student grade is: {0}".format(grade))     



def call_tests():

    while True:
        option = input("Create test . for exit type EXIT: ")

        if option == 'EXIT':
            input("test end ...")
            break
        else:
            Test()
