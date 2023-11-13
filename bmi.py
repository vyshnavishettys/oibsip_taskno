height = (input('height in meters'))
weight = (input('weight in kgs'))
height= float(height)
weight= float(weight)



def bmi(weight,height):
    
    bmi=weight/ (height**2)
    if bmi<18.5:
        return 'underweight',bmi
    if bmi>18.5 and bmi<24.9:
        return 'normal weight',bmi
    if bmi>25.0 and bmi<29.9:
        return 'overweight',bmi
    if bmi>30.0:
        return 'obese',bmi
    
quote,bmi=bmi(weight,height)
print('your bmi is {} and you are {}'.format(bmi, quote))