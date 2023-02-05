def main():
    ##################################################
    
    num_male = input("Number of males in class: ")
    num_female = input("Number of females in class: ")
    sum = int(num_male) + int(num_female) #int becasue input creates string by default
    percent_male = (int(num_male) / sum) * 100
    percent_female = (int(num_female) / sum) * 100
    
    
    
    print ("The total number of students:  \t \t {0:.0f} ".format(sum))
    print ("The number of males and females: \t {0:.0f}\t {1:.0f}\t" .format(float(num_male), float(num_female)))
    print (f"The percentage of males and females: \t {float(percent_male):.2f}%  {float(percent_female):.2f}%")
    # total student, two indents, {position 1: 0 decimal places}, .format(variable)
    # num of males and females, one indent, {position: 0 decimal places}, indent, next number, .fomrat float becasue int didn't work
    # f string "Typing, indent, {float(variable): 2 decimals}direct percent sign printed "%" next {}" [Simpler it seems. Easier to concantinate]

    ##################################################
    pass


if __name__ == '__main__':
    main()
