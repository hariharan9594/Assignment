import pandas as pd

#Input Dataset
threshold = {
"Large": 10,
"XLarge": 20,
"2XLarge": 40,
"4XLarge": 80,
"8XLarge": 160, 
"10XLarge": 320
}
#Reading input data from CSV and Users
input_data = pd.read_csv("data.csv", index_col=0) 
inp = input("Please enter the units and hours: ")
input_unit, input_hour = [int(s) for s in inp.split() if s.isdigit()]
output_data = {}
output_data["output"] = []


#Function to calculate the combination OF threshold units to match target unit
def units_list (input_list, target):    
    units = [0 for i in range (len(input_list))]
    #Loop through units
    for unit in input_list [::-1]:
        i = input_list.index(unit)
        units[i] = 0 
        #looping units until to get smaller value
        while target >= unit:
            target -= unit 
            units[i]+= 1
    return units


#Calculate for New York
ny_input_data = list(input_data["New York"])
out_val=list(threshold. values())
for index, each in enumerate(ny_input_data):
    if each!=each:
        out_val[index]=input_unit+1 
units_out=units_list(out_val, input_unit)
ny_input_data = [0 if x != x else x for x in ny_input_data]
ny_total_cost = [a*b*input_hour for a,b in zip(units_out, ny_input_data)]
machines=[] 
for each, size in zip(units_out, list (threshold.keys())):
    if each!=0:
        machines.append((size, each)) 
#OUTPUT JSON
output_data["output"].append({
"region": "New York",
"total_cost" : "$" + str(sum(ny_total_cost)),
"machines" : machines
})


#Calculate for India
ind_input_data = list(input_data["India"])
out_val=list(threshold.values())
for index, each in enumerate(ind_input_data):
    if each!=each:
        out_val[index]=input_unit+1
units_out=units_list(out_val, input_unit)
ind_input_data = [0 if x != x else x for x in ind_input_data] 
ind_total_cost = [a*b*input_hour for a,b in zip(units_out, ind_input_data) if b is not None] 
machines=[]
for each,size in zip(units_out, list (threshold. keys ())):
    if each!=0:
        machines.append((size, each))
#OUTPUT JSON
output_data["output"].append({
"region": "India",
"total_cost" : "$" + str(sum(ind_total_cost)), 
"machines": machines
})


#Calculate for China
ch_input_data = list(input_data["China"])
out_val=list(threshold. values())
for index, each in enumerate(ch_input_data):
    if each!=each: 
        out_val[index]=input_unit+1
units_out=units_list(out_val, input_unit)
ch_input_data = [0 if x !=x else x for x in ch_input_data] 
ch_total_cost = [a*b*input_hour for a,b in zip(units_out,ch_input_data) if b is not None] 
machines=[]
for each,size in zip(units_out, list (threshold. keys())):
    if each!=0:
        machines.append((size, each))
#OUTPUT JSON
output_data["output"].append({
"region": "China", "total_cost" : "$" + str(sum(ch_total_cost)),
"machines" : machines
})
print(output_data)