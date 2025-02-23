
class multipleFunctions:
    def Subfields():
        print("Sub-fields in AI are:")
        sub_field_list = ['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing','Natural Language Processing']
        for field in sub_field_list:
            print(field)

    def oddEven():
        num = int(input("Enter a number:"))
        if num % 2 == 0:
            print(num ,"is Even number")
        else:
            print(num ,"is Odd number") 

    def Elegible():
        gend = input("Your Gender:")
        age = int(input("Your Age:"))
        if gend == 'Male':
            if age >= 21:
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        else:
            if age >= 18:
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")

    def percentage():
        subject1 = int(input("Subject1="))
        subject2 = int(input("Subject2="))
        subject3 = int(input("Subject3="))
        subject4 = int(input("Subject4="))
        subject5 = int(input("Subject5="))
        total = subject1 + subject2 + subject3 + subject4 + subject5
        print("Total : ",total)
        print("Percentage : ", (total / 500) * 100)

    def triangle():
        height = int(input("Height:"))
        breadth = int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ",(height*breadth)/2)
        
        height1 = int(input("Height1:"))
        height2 = int(input("Height2:"))
        breadth = int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth ")
        print("Area of Triangle: ",height1+height2+breadth)

    def BMI():
        bmi_ind = float(input("Enter the BMI Index:"))
        if bmi_ind < 18:
            print("Underweight")
        elif bmi_ind < 18.5:
            print("Thin for Height")
        elif bmi_ind < 24.9:
            print("Healthy weight")
        elif bmi_ind < 29.9:
            print("Overweight")
        else:
            print("Very Overweight")

