# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data=np.genfromtxt(path,delimiter=",",skip_header=1)
print(data)
census=np.concatenate((data,new_record))
print(census.shape)
print(census)


# --------------
#Code starts here
import numpy as np

age = census[:,0]
max_age= np.amax(age)
print(max_age)

min_age= np.amin(age)
print(min_age)

age_mean= np.mean(age)
print(age_mean)

age_std= np.std(age)
print(age_std)


# --------------
#Code starts here
import numpy as np
#Code starts here
##race=census[:,2]
##print(race)
race_0=census[census[:,2]==0]
##print(race_0)
race_1=census[census[:,2]==1]
##print(race_1
race_2=census[census[:,2]==2]
##print(race_2)
race_3=census[census[:,2]==3]
##print(race_3)
race_4=census[census[:,2]==4]
##print(race_4)
len_0=len(race_0)
print(len_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
print(len_1)
print(len_2)
print(len_3)
print(len_4)
minority=np.array([len_0,len_1,len_2,len_3,len_4])
minority_race=minority.argmin()
print(minority_race)


# --------------
#Code starts here
import numpy as np
senior_citizens=census[census[:,0]>60]
##print(senior_citizens)
working_hours_sum=np.sum(senior_citizens[:,6])
print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
print(senior_citizens_len)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
##print(high)
##print(low)
avg_pay_high=np.mean(high[:,7])
avg_pay_low=np.mean(low[:,7])
print(avg_pay_high)
print(avg_pay_low)


