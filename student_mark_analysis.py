import pandas as pd
data = {
    "Name" : ["Salman", "Rahul", "kutub", "Aman", "Supriya"],
    "Maths" : [90, 85, 78, 92, 88],
    "Science" : [80, 85, 75, 95, 89],
    "English" : [78, 88, 82, 91, 84]
    
}

df = pd.DataFrame(data)
print(df)

df["Total"] = df["Maths"]+df["Science"]+df["English"]
print(df)

df["percentage"] = ((df["Total"]/300)*100).astype(int)
print(df)

def grade_calc(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "Fail"
    
df["Grade"] = df["percentage"].apply(grade_calc)
print(df)


topper = df.loc[df["percentage"].idxmax()]
print("Topper Details:")
print(topper)

print("Maths Average:" , df["Maths"].mean())
print("Science Average:" , df["Science"].mean())
print("English Average:" , df["English"].mean())

high_scorers = df[df["percentage"] > 85]
print("Students above 85%:")
print(high_scorers)