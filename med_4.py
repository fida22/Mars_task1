from collections import deque
def muchiko_filter(data):
    # Return nothing if data has less than 3 elements (window too small)
    if len(data)<3:
        return []
    
    # smoothed_data stores the final moving averages
    # window holds the current 3-point window
    smoothed_data=[]
    window=deque(data[:3])

    # Calculate and store the first average
    avg=sum(window)/3
    smoothed_data.append(avg)

    for i in range(3,len(data)):
        # Slide the window: remove the oldest element, add the new one
        window.popleft()
        window.append(data[i])
        # Calculate and store the average of the current window
        avg=sum(window)/3
        smoothed_data.append(avg)

    return smoothed_data

def sanchiko_filter(data):
    # Return nothing if data has less than 3 elements (window too small)
    if len(data)<3:
        return []
    
    # smoothed_data stores the final moving averages
    # window holds the current 3-point window
    smoothed_data=[]
    window=deque(data[:3])

    #s_window stores the sorted elements in the window
    sorted_window=sorted(window)
    smoothed_data.append(sorted_window[1])

    for i in range(3,len(data)):
        # Slide the window: remove the oldest element, add the new one
        window.popleft()
        window.append(data[i])
        # Sort the window and store the median (middle) value
        sorted_window=sorted(window)
        smoothed_data.append(sorted_window[1])

    return smoothed_data

def which_filter(data):
    #finding mean and sd to calculate relative standard deviation
    mean=sum(data)/len(data)
    squared_diff=[ (x-mean)**2 for x in data]
    variance=sum(squared_diff)/len(data)
    sd=variance**0.5

    #calculating rsd
    rsd=sd/mean*100

    #slecting filter accoring to rsd value
    if rsd<=10:
        chosen_filter="Muchiko"
    elif rsd>10 and rsd<=30:
        chosen_filter="Hybrid"
    elif rsd>30:
        #check for z score(checking for spike)
        spike=any(abs(x - mean) > 3 * sd for x in data)
        if spike:
            chosen_filter="Sanchiko"
        else:
            chosen_filter="Muchiko"
    return chosen_filter



if __name__=="__main__":
    #getting data from the text file
    f=open("log.txt")
    data = list(map(int, f.read().split()))
    f.close()

    filter_type=which_filter(data)

    #choosing filter according to filter type
    if filter_type=="Muchiko":
        smoothed_data=muchiko_filter(data)
    elif filter_type=="Sanchiko":
        smoothed_data=sanchiko_filter(data)
    elif filter_type=="Hybrid":
        smoothed_data=muchiko_filter(data)
        smoothed_data=sanchiko_filter(smoothed_data)
    #printing the output
    print("Smoothed Data:", smoothed_data)
    print("Filter Used:", filter_type)



