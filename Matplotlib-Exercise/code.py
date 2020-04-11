# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Code starts here
data=pd.read_csv(path)
#print(data.head())
loan_status=data['Loan_Status'].value_counts()
#print(loan_status)
#plt.figure(figsize=[14,8])
plt.plot(loan_status)
#loan_status.plot(kind='bar')
plt.xlabel('Loan Status')
plt.ylabel('Loan apporval count')
plt.tight_layout()



# --------------
#Code starts here
property_and_loan=data.groupby(['Property_Area','Loan_Status'])
property_and_loan=property_and_loan.size().unstack()
property_and_loan.plot(kind='bar',stacked=False, figsize=(15,10))
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
#plt.title('')
#print(property_and_loan)



# --------------
#Code starts here
education_and_loan=data.groupby(['Education','Loan_Status'])
education_and_loan=education_and_loan.size().unstack()
education_and_loan.plot(kind='bar',stacked=False, figsize=(15,10))
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
#plt.title('')
#print(property_and_loan)


# --------------
#Code starts here
graduate=data[data['Education']=='Graduate']
not_graduate=data[data['Education']=='Not Graduate']

pd.Series(graduate['LoanAmount']).plot(kind='density',label='Graduate')
pd.Series(not_graduate['LoanAmount']).plot(kind='density',label='Not Graduate')

#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(nrows = 3 , ncols = 1)
#plot scatter plot between 'ApplicantIncome' and LoanAmount using ax_1. Set axis title as Applicant Income
x=data['ApplicantIncome']
y=data['LoanAmount']
ax_1.scatter(x,y)
ax_1.set_title('Applicant Income')

#Plot scatter plot between 'CoapplicantIncome' and LoanAmount using ax_2. Set axis title as Coapplicant Income
x=data['CoapplicantIncome']
y=data['LoanAmount']
ax_2.scatter(x,y)
ax_2.set_title('Coapplicant Income')

data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']

#Plot scatter plot between 'TotalIncome' and LoanAmount using ax_3. Set axis title as Total Income
x=data['TotalIncome']
y=data['LoanAmount']
ax_3.scatter(x,y)
ax_3.set_title('Total Income')


