# Ivy_Homes_Assignment
So this repository serves as the codebase for the assignment given by Ivy Homes for the SWE Intern role at IIT Kharagpur and this is the submission of Subhransu Sahu (22MI10059).
When I tested out the rate limit and the time required to reset the rate limit , i got the following info

V1 - 100 requests , 16 seconds reset time

V2 - 50 requests, so first time i checked i got 37 seconds but later when i ran the main code to find out names , it gave 429 error on some queries so I reran the code and got to know that 39 is the sweet spot for the reset time of V2

V3 - 80 requests, 27 seconds 


So now coming to the main part , initially i thought that if I give the input of only one character like {a,b,c,d......1,2,3} like this , then I can get all the names since as the name suggests its autocomplete but no it was not like that-

There were different responses for inputs like {aa,ab,a1,ba,1a,1d,1v....} and they most of them were not included when I gave single character as input , and they were unique names and the some of the observations I made are -

1) #,&,+ are the characters which gave results with names while others didnt
2) None of the name started with capital alphabets
3) for V1 the valid characters that gave results are - " abcdefghijklmnopqrstuvwxyz#&+"  while that of V2 and V3 are " abcdefghijklmnopqrstuvwxyz0123456789#&+" i.e V1 didnt allow numbers , thats why i have included two files one for V1 and other for both V2 and V3 , you just have to enter the version in the second code while it is constant in first code(V1).
4) only two character combinations yielded results like {ab,bb,bc,gc} and not three letter or more inputs like {aaa,avn,dndnd.........}
5) Some names were repeated so to find unique names i stored all the results in set while for all names i saved it in a list
   
So after running the files v1_test.py the details are-
Total requests - 930
Unique Names - 6720
All Names including duplicates - 9260

After running v2&v3_test.py for v2 - 
Total requests - 1640
Unique Names - 7873
All Names including duplicates - 12001

After running v2&v3_test.py for v3 - 
Total requests - 1640
Unique Names - 7156
All Names including duplicates - 11785





