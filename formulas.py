########## mortgage formulas
from kivy.resources import resource_add_path


def calc_monthly_cost(tax,house):
    if tax == "":
        return 0
    else:
        taxes = float(tax) / 100
        cost = (taxes * float(house)) / 12
        return cost

def calc_monthly_payment(house,down,interest,terms,tax):
    monthly_cost = calc_monthly_cost(tax,house)
    loan = float(house) * ((100 - float(down)) / 100)
    interest = (float(interest) / 12) / 100
    num_of_pay = float(terms) * 12
    monthly_c = (loan * (interest * (1+interest)**num_of_pay))/(((1+ interest)**num_of_pay) - 1)
    return round((monthly_c - monthly_cost),2)
    

############# interest formulas

def convert(compound):
    if compound == "Annually":
        return 1
    elif compound == "Quarterly":
        return 4
    elif compound == "Monthly":
        return 12

def compound_p(principal,interest,compound,term):
    total = float(principal)*((1+((float(interest)/100) /float(compound)))**(float(compound)*float(term)))
    return round(total,2)

def compound_f(monthlypay,interest,compound,term):
    p = 12 / float(compound)
    total = float(monthlypay) * p * (((1+((float(interest)/ 100)/float(compound)))**(float(compound)*float(term)) - 1) / (((float(interest)/100))/float(compound))) 
    return round(total,2)

def compound_interest(principal,interest,period,monthly,comp):
    compound = convert(comp)
    result = compound_p(principal,interest,compound,period) + \
        compound_f(monthly,interest,compound,period)
    return result

################ inflation formulas
def calculate_inflation(price,inflation,term):
    result = float(price)*((1+(float(inflation) / 100))**float(term))
    return round(result,2)



################ present val formula
def present_val(fv,interest,term):
    result = float(fv) * (1/((1+(float(interest)/100))**float(term)))
    return result
