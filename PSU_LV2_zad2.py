import numpy as np
import matplotlib.pyplot as plt



data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6,7),delimiter=",", skiprows=1)
print(data)
fig, ax = plt.subplots()
scatter = ax.scatter(data[:, 0], data[:, 3], c='b', s=data[:, 5])

plt.xlabel('hp')
plt.ylabel('mpg')
plt.title('informacije o težini vozila')


handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6)
legend2 = ax.legend(handles, labels, loc="upper right", title="Sizes")


print(min(data[:,0]))
print(max(data[:,0]))
print(sum(data[:,0])/len(data[:,0]))


arr=[]
for i,item in enumerate(data[:,1]):
    if item ==6:
        arr.append(data[i,0])

print(min(arr))        
print(max(arr))        
print(sum(arr)/len(arr))



plt.show()        

