'''
A module for calculating the Ruffier test result.

Ideally, the sum of pulse rate measured in three attempts (before the physical exertion,
immediately after it, and after a short rest) should not exceed 200 beats per minute.
We suggest children measure their pulse for 15 seconds and convert to beats per minute
by multiplying by 4:
   S = 4 * (P1 + P2 + P3)
The further this result is from the ideal 200 beats, the worse.
Traditionally, tables are given for a value divided by 10.

Ruffier Index  
   IR = (S - 200) / 10
is estimated by the table according to one's age:
       7-8             9-10                11-12               13-14               15+ (for teenagers only!)
exl.    6.4 and less    4.9 and less        3.4 and less         1.9 and less        0.4 and less
good    6.5 - 11.9      5 - 10.4            3.5 - 8.9            2 - 7.4             0.5 - 5.9
sat.    12 - 16.9       10.5 - 15.4         9 - 13.9             7.5 - 12.4          6 - 10.9
weak    17 - 20.9       15.5 - 19.4         14 - 17.9            12.5 - 16.4         11 - 14.9
unsat.  21 and more     19.5 and more       18 and more          16.5 and more       15 and more

For all ages, the difference between the unsatisfactory and weak results is 4,
the difference between the weak and satisfactory results is 5,
and the difference between the good and satisfactory results is 5.5.

Therefore, let's code the ruffier_result(r_index, level) function that receives
the calculated Ruffier index and the "unsatisfactory" level for the age,
and returns the result.
'''

# result text strings:
txt_index = "Your Ruffier Index: "
txt_workheart = "Cardiac performance: "
txt_nodata = "No data for this age"

txt_res = []
txt_res.append("low.\nUrgently consult the doctor!")
txt_res.append("satisfactory.\nConsult the doctor!")
txt_res.append("average.\nIt may be worth an additional doctor's consultation.")
txt_res.append("above average")
txt_res.append("high")


def ruffier_index(P1, P2, P3):
    """returns the index value by three pulse indicators for reconciliation with the table"""
    return (4 * (P1 + P2 + P3) - 200) / 10


def neud_level(age):
    """options with an age less than 7 and age of adults should be processed separately;
    here we select only the “unsatisfactory” level inside the table:
    for children aged 7, “unsatisfactory” is index 21; then it decreases by 1.5
    every 2 years until reaching 15 for children aged 15–16."""
    norm_age = (min(age, 15) - 7) // 2
    result = 21 - norm_age * 1.5
    return result
    

def ruffier_result(r_index, level):
    """the function receives the Ruffier index and interprets it,
    returning the fitness level (0 to 4)
    the higher the level, the better the result."""
    if r_index >= level:
        return 0
    level = level - 4
    if r_index >= level:
        return 1
    level = level - 5
    if r_index >= level:
        return 2
    level = level - 5.5
    if r_index >= level:
        return 3
    return 4
def test(P1, P2, P3, age):
    """ this function may be used outside the module to calculate Ruffier index.
    It returns the finished result strings."""
    if age < 7:
        return txt_index + "0" + "\n" + txt_nodata
    else:
        ruff_index = ruffier_index(P1, P2, P3)
        result = txt_res[ruffier_result(ruff_index, neud_level(age))]
        res = txt_index + str(ruff_index) + '\n' + txt_workheart + result
        return res
