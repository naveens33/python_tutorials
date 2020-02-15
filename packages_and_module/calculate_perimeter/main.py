'''
#from packages_and_module.calculate_perimeter.cal_perimeter import squ_perimeter, rec_perimeter
#from packages_and_module.calculate_perimeter import cal_perimeter
from packages_and_module.calculate_perimeter.cal_perimeter import *
if __name__=='__main__':
    print(squ_perimeter(4))
    print(rec_perimeter(3,5))
    #print(cal_perimeter.squ_perimeter(4))
    #print(cal_perimeter.rec_perimeter(3,5))
'''

#from packages_and_module.calculate_area.cal_area import CalArea
from module_example.calculate_area.cal_area import *

if __name__=='__main__':
    obj=CalArea()
    print(obj.sqa_area(5))
    