# how does a dictionary work 
variable_name = {"Variable_key":"Variable_value",
                 "Variable2":"Value2"}
# you need the key to get the value 
print(variable_name["Variable_key"])

#add a new intry
variable_name["variable3"]= "value 3"
#this make a new entry in the dictionary 


#nested list in dictionaries 
travel_log = {
    "France":["Paris","Lille","Dijon"],
    "Germany":["Stuttgart","Berlin"]
}

print(travel_log["France"][1])
#this prints Lille 

nested_list = ["A","B",["C","D"]]
print(nested_list[2][1])
# C and D are the 3rd item in the first list not a squared list rows are x and collums are y 

print(travel_log["Germany"]["cities_visited"][2])