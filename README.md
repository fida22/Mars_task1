#  MaRS Software Task #1

This repository contains my solutions to the Light, Medium, and Hard Dose problems

---

##  Learning Experience

Throughout this task, I:

- Learned to install ubuntu by dual booting 
- Got to know how to use Git and Github
- Learned about bashscripting which is a new concept for me
- Understood new concepts of Filters, 3D and 4D rotation systems,Path finding with Matrix
- worked with python libraries such as collections
- Had fun time doing all the other Problems 

---

## Equations, Concepts & Theorems

### **Medium_1**:

  - Euclidean distance between two points: \(\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}\)

##

### **Medium_2**
  - **Morse Code**:


     ![Morse Code Chart](https://github.com/fida22/Mars_task1/blob/9f95107b63ba39e49381d643d9f49e272361df65/photos_for_readme/morse%20code.jpg)


##

    

### **Medium 4**:

  - Standard deviation formula:


      $$
    \text{Standard Deviation} = \sqrt{ \frac{1}{N} \sum_{i=1}^{N} (x_i - \text{mean})^2 }
      $$


    - where
      - \( N \) is the total number of data points  
      - \( x_i \) is each individual data point  
      - \( \text{mean} = \frac{1}{N} \sum_{i=1}^{N} x_i \)
     

        
  - Relative Standard Deviation:




    
     ![Morse Code Chart](https://github.com/fida22/Mars_task1/blob/738887aed8fe0cf3b9906e2689b03c5e6c3a6cef/photos_for_readme/rsd%20formula.png)



      
  - Choosing filter based on RSD






      ![rsd vs filter](https://github.com/fida22/Mars_task1/blob/9f95107b63ba39e49381d643d9f49e272361df65/photos_for_readme/RSD%20VS%20FILTER.png)





    

  - Z - Score to find Outlier





      ![rsd vs filter](https://github.com/fida22/Mars_task1/blob/9f95107b63ba39e49381d643d9f49e272361df65/photos_for_readme/RSD%20VS%20FILTER.png)



##
    
### **Medium_5**
  
  - Formula to convert Euler to quaternions





    
      ![rsd vs filter](https://github.com/fida22/Mars_task1/blob/d5a7bfe86de85ba81f608b48784bcb273de14a7b/photos_for_readme/euler%20to%20quaternion%20formula.png)







---


## 📼 Approach & Thought Process


### ***Bash scripting***
  ***Learnings***:
  
  ![rsd vs filter](https://github.com/fida22/Mars_task1/blob/d63f3bffb14dfb77fabedc09bc1d5755b2b12550/photos_for_readme/bashscirpting%20learning.jpg)
  


### 1) ***Medium_1***
  - ***Interpretation of Given Data*** :
     
    - `x, y, z` coordinates are given as input.
    - `z` coordinate is taken as the **height**.
    - `y` represents **forward and backward** movement.
    - `x` represents **left and right** movement.

  - ***Reasoning*** :

    - The `y` coordinate may contain **error** because the **camera is mounted at the front**, but the rover should rotate **when its center** reaches the marker.
      
  - ***Final Output*** :
    
    - Therefore, we **adjust the y coordinate** by an **offset value of 55**.

    we can find the distance between camera and marker using euclidean distance formula


##
### 2) ***Medium_2***
  - ***Interpretation of Given Data*** :
     
    - Morse code is stored in a dictonary named morse_dict
    - The message is split into words using split function giving 7 spaces as paramater to split
    - The words are again split into letters using the split function giving 3 spaces as parameter to split
    

  - ***Reasoning*** :

    - Traveresed thorugh each letter
    - checked weather if the morse code of the letter is found in dictonary keys
    - if yes returned the english equivalend
    - and added it to the result string
      
  - ***Final Output*** :
    
    - returned the result string

    note: Main function was not included since the question was to write a funciton

##

### 3) ***Medium_3***
  - ***Interpretation of Given Data*** :
     
    - The given input message was converted to upper case

  - ***Reasoning*** :

    - Traversed through each letter
    - took its ascii value
    - reduced the ascii value by its position value
    - converted it back to charecter
      
  - ***Final Output*** :
    
    - The result was stored in a list , so converted it back to string

##

### 4) ***Medium_4***
  - ***Interpretation of Given Data*** :

    - A set of data was given in log.txt
    - extracted the data using file handling in python and stored it in list name data
    - `y` represents **forward and backward** movement.
    - `x` represents **left and right** movement.

  - ***Reasoning*** :

    - Included Three function One for Sanchiko filter , Other for Muchiko filter and other to determine which filter to use
    - Muchiko filter
      - using sliding window technique and deque from collections module computed average using a window size of 3 and added the results to smoothed data list
    - Sanchiko filter
      - using sliding window technique and deque created the window sorted it into ascending oreder and found the median and added the results to smoothed data list
    - Which filter to use
      - Calculated the RSD value
      - if its between 1 to 10 use Muchiko
      - if its between 10 to 30 use Hybrid
      - if it greater than 30 check for z score
      - if spike is found use Sanchiko
      - else use Muchiko  
      
  - ***Final Output*** :
    
    - Smoothed data and Filter used is returned
   

##

### 5) ***Medium_5***
  - ***Interpretation of Given Data*** :
     
    - Assuming the input is in degree converted it into radians
   
  - ***Reasoning*** :

    - Calculated the half angles and computed the quternions using the formula
      
  - ***Final Output*** :
    
    - The quaternion cordinates were returned
      
##

### 1) ***Hard_1***
  - ***Interpretation of Given Data*** :
     
    - obstacle cordinates where taken from sample.txt file using python file handling functions
    - each row is considered as one obstacle
    - stored the obstacle cordinates in a list
      
  - ***Reasoning*** :

    - To create the map The largest value is found from the obstacle cordinate and
    - created a map double the size of it because brick is in the center and it can move in both the directions
    - intialised the map with 1 
    - The net movement in the vertical direction will be North - South
    - The net movement in the horizontal direction will be East -west
    - The middle cordinates will be [n,n]
    - the exact cordinate of obstacle will be
      - row: n - (north-south)
      - column: n + (east-west)
    - equated that cordinate to zero
      
  - ***Final Output*** :
    
    - The map is printed
      ![rsd vs filter](https://github.com/fida22/Mars_task1/blob/d63f3bffb14dfb77fabedc09bc1d5755b2b12550/photos_for_readme/map.jpg)


---



## 📚 Resources Used

 - https://www.youtube.com/watch?v=mXyN1aJYefc&ab_channel=Robtech
 - https://www.codedex.io/git-github
 - https://www.w3schools.com/
 - https://betterstack.com/
 - https://stackoverflow.com/
 - https://devhints.io/bash

