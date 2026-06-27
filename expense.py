import pandas as pd
import os
from datetime import datetime as dt
class expense:
    def __init__(self):
        self.csv = self.__readCSV();

    def __filecsv(self,csvfile):
        return os.path.join(os.path.dirname(__file__),csvfile)
    
    def __readCSV(self):
        csvfile="expense.csv"
        file = self.__filecsv(csvfile)
        print(file)
        csv  = pd.read_csv(file,sep=",",names=["date","description","category","prize"]);
        return csv;
    
    def __writeData(self,data:dict):
        result = pd.DataFrame(data)
        
        return result.to_csv(self.__filecsv("expense.csv"),index=False,mode="a",header=0)
    
    
    
    def showAllDataExpenses(self):
        data = self.__readCSV()
        print(f"Loaded {data.shape[0]} expenses" )
        for rows,cols in data[1:].iterrows():
            print(cols["date"]," | ",cols["description"]," | ",cols["category"]," | ",float(cols["prize"]))
            
    def showAllDataTotalExpenses(self):
        data = self.__readCSV()
        print(f"Loaded {data.shape[0]} expenses" )
        totalprizes = 0
        for rows,cols in data[1:].iterrows():
            print(cols["date"]," | ",cols["description"]," | ",cols["category"]," | ",float(cols["prize"]))
            totalprizes += float(cols["prize"])
        print(f"The Total of the prize ---------- {totalprizes}")
                
    def addExpense(self):
        validDate= False
        while not validDate :
            try:
                date = str(input("Enter Date(YYYY-MM-DD):"))
                convertedDate= dt.strptime(date,"%Y-%m-%d")
                validDate = True
            except ValueError as e:
                print(f"----ERROR:not valid input date it must be an in {e}----")
                print(f"Error: {e}")
                answer = int(input("--you want to cotinue or not ? (1--yes 0--no)"))
                if answer == 0:
                    print("----terminating the operation----")
                    return
                else:
                    print("----continuening the process----")
                 
        description = input("Enter Description of the Expense:")
        category = input("Enter Which Category it Belong:")
        
        validprize = False
        while not validprize:
            try:
                prize = int(input("Enter Prize Of How Much Spends:"))
                validprize = True
                continue
            except ValueError as e :
                print(f"----ERROR:not valid input prize it must be an in {e}----")
                answer = int(input("--you want to cotinue or not ? (1--yes 0--no)"))
                if answer == 0:
                    print("----terminating the operation----")
                    return
                else:
                    print("----continuening the process----")
        else:      
            data = {"date":[date],"description":[description],"category":category,"prize":[prize]}
            self.__writeData(data)
            
            print("-------------------------------")
            print("Export Successfully to the CSV")
            
    def summaryCategory(self):
        data = self.__readCSV()
        categoriesTotal={}
        totalprize = 0
        for row,col in data[0:].iterrows():
            category = col["category"]
            totalprize += col["prize"]
            prize = col["prize"]
            
            if category in categoriesTotal:
                categoriesTotal[category] += prize
            else:
                categoriesTotal[category] = prize
        
        print("--------------CATEGORY SUMMARY----------------")
        for key,value in categoriesTotal.items():
            percent = ( value / totalprize ) *100
            print(f"< {key} : {percent:.2f}% >")  
            print(f"SPEND:{value}")
        print(f"---------Total Spend: {totalprize}")
    
    def filterByDate(self):
        data = self.__readCSV()
        data["date"] = pd.to_datetime(data["date"])
        while True:
            
            date = str(input("ENTER DATE(YYYY-MM):"))
            try:
                convertdate = dt.strptime(date,"%Y-%m")
                break
            except ValueError as e:
                print(e)
                ans = int(input("Do you want to terminate the program?(1-yes 0-no)"))
                if ans == 1 :
                    print("terminating the program thanks")
                    return
                
        filterdata = data[data["date"].dt.strftime("%Y-%m") == convertdate.strftime("%Y-%m")]
        print(f"Filter Loaded {filterdata.shape[0]} expenses")
        totalMonthExpense = 0
        print("    Date              |    Description     |    Category    |    Prize    |")

        for row,col in filterdata[0:].iterrows():
            des = col["description"]
            cate = col["category"]
            prize = col["prize"]
            exDate = col["date"]
            totalMonthExpense += prize 
            print(f"---{exDate}---|---{des}---| , |---{cate}---| ,|---{prize }---|")
        print(f"Total : {totalMonthExpense}")
