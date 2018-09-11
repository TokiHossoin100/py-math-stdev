#Import statistics module and defining variables
import statistics as st
dataset = []
x = 0

#Loop to enter data
print("To stop entering data, enter anything other than a number.")
while True:		#start while loop
	try:
        temp = float(input("Entry {}: ".format(x)))		#user input to temp
        dataset.append(temp)	#adds temp to end of list
        x += 1		#increments x by 1
    except ValueError:     #catches exception when a non-float is entered (exit loop)
        break

#Calculate and print standard deviation
sd = st.stdev(dataset)
print("s = {}".format(sd))
