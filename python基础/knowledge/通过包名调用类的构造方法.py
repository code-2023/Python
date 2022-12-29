import packages

"""
包名其实指向了__init__.py(即包的特殊模块）！！！
所以要想通过包名调用[常用类的构造方法]和[常用的普通方法]，你就必须在__init__.py中导入相应的类和方法！
"""
# 通过包名learn调用Module模块中的Animal类的构造方法，实际上,这就意味着[创建了对象]
animal = packages.Animal("Cat", "雌性", 3)
animal.get_sex()
print("构造方法的返回值类型是%s" % (type(animal)))
# 同理，通过包名learn调用Module模块的普通方法
packages.func()
