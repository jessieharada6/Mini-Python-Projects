# age:int
# name:str
# height: float
# is_human:bool

# specify data type
# Type hints:  return data type with arrow
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive= False
    return can_drive

if police_check(18):
    print("you may pass")
else:
    print("fine")