# 1 классы внутренноiклассы

def a(b):
    print(b)

a(12320)

class A:
    def __str__(self):
        return f'выполняю роль принта {self.name, self.key, self.age}'
        # pass
       #  pass
    def __init__(self, name, key, age):
        self.name = name
        self.key = key
        self.age = age

    def __len__(self):
        return len(self.name)

# экземпляр\ объект
p=A('Mike', 123, 123)
print(p)
print(len(p))


pon=11
print(type(pon))
print(p)

po='weret'


# 4 принципы ООП
# наследование
# полиморфизм
# абстракция
# инкасуляция - описывает сразу 2 действия, также дает защиту
# защиту 3 уровня

# import last6
# last6.__init__



class B(A):
    def __init__(self, name, key, age, old):
        super().__init__(name, key, age)
        self.old = old

    def none(self):
        print(self.name, 'ничего не умеет')

    def newB(self):
        print ('умею бегать')

I=B('d', 12,12, 12)
print (dir(I))
print(len(I))

class D(B):
   def none(self):
       super().none()
       A.none(self)

newD=D('Mile', 12,12,234)

newD.none()
# print(D.mro())

newD.none()
print(dir(newD))






##