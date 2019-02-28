# notes for beginner: (reference only)

# Write a Guess Number Game: guess a number from a random group, you only have 5 times to guess.

import random

result = random.randint(0, 99)
times = 5
print ('lets play a number game')
while times > 0:
    num = int(input(' please guess a number'))
    if num == result:
        print ("congratulation you found the number")
        break  # exist the program
    else:
        if num > result:
            print ("current number is bigger than result")
        else:
            print ("current number is smaller than result")
        times -= 1
        if times == 0:
            print ("bad luck that you did not find")


# deal with exceptions

try :
	<statement>
except Exception1 as e:
    <statements>
except (Exception2,Exception3) as e:    
    <statements>
except Exception4:
    <statements>
except:
    <statements>
else:
    <statements>
finally:
    <statements>

# the order is: try->except->else->finally


#str commom Methods

str.count(sub[,start[,end]]) # Return the number of non-overlapping occurrences of substring sub in the range [start, end].

str.find(sub[, start[, end]]) # Return the lowest index in the string where substring sub is found within the slice s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.

str.lower() # converted to lowercase

str.replace(old, new[, count]) # Return a copy of the string with all occurrences of substring old replaced by new.

str.strip([chars]) # Return a copy of the string with the leading and trailing characters removed. The chars argument is a string specifying the set of characters to be removed

str.title() # example 'Hello world'.title()  ==> 'Hello World'

str.upper()


str[i : j] #including the end, not including start 


class Test:
    def __init__(self):
        print('init a class')
    def test(self):
        print(self)

test=Test()
test.test()
#========output below ========
'''init a class
<__main__.Test object at 0x0000021E9915A4A8> '''

'''Note: 

1. class define className: with () for inherit 
2. _init_ : happen once at instantiation , for creating object use; However, can only one method for _init_
3. self: when instantiation try to use method, iternally it will pass a self parameter.   (very similar to this in Java)

class 定义 class className：，className后面可以带括号，也可以省略，带括号是为了继承，下面讲到。
__init__：这个方法会在类实例化的时候执行一次， 初始化代码可放在这里，也可以定义参数，在创建对象的时候传入，但是__init__方法只能有一个。
self：所有实例调用方法的时候，内部都会首先传入一个self参数，就是对应着方法的self（名字可以随意定，但是最好还是符合规范使用self），这个就相当于java类中的this关键字。
一个脚本中可以创建多个类，不过建议不要创建多个，当然若它们之间有很强的关联性也是可以的。
类是模块内的属性
　　其实我觉得Python对self的使用太不友好，应该学学java，最好是定义方法的时候不用指明并将self设置为关键字。
'''



#inherit" 

class Aniaml():
    def say(self):
        print ('aniaml say')

class dog(Aniaml):
    def say(self):
        print ("dog say")

#python can do mulitple inheritance； 


''' python method only have public and private,  privete method has two _   _ to identify 
Example: 

_init_
_del_
_repr_ : similar to toString in Java (convert) '''

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__ )


#output above: 

Employee.__doc__: Common base class for all employees
Employee.__name__: Employee
Employee.__module__: __main__
Employee.__bases__: (<class 'object'>,)
Employee.__dict__: {
   'displayCount': <function Employee.displayCount at 0x0160D2B8>, 
   '__module__': '__main__', '__doc__': 'Common base class for all employees', 
   'empCount': 2, '__init__': 
   <function Employee.__init__ at 0x0124F810>, 'displayEmployee': 
   <function Employee.displayEmployee at 0x0160D300>,
   '__weakref__': 
   <attribute '__weakref__' of 'Employee' objects>, '__dict__': 
   <attribute '__dict__' of 'Employee' objects>
}


'''
__dict__ − Dictionary containing the class's namespace.

__doc__ − Class documentation string or none, if undefined.

__name__ − Class name.

__module__ − Module name in which the class is defined. This attribute is "__main__" in interactive mode.

__bases__ − A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.


'''



Overriding Methods:

can always override your parent class methods.















