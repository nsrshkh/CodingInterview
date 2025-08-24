class MyMeta(type):
    # 'mcs' is the metaclass itself (MyMeta)
    # 'name' is the name of the class to be created (e.g., 'MyClass')
    # 'bases' is a tuple of base classes (e.g., (object,))
    # 'attrs' is a dictionary of attributes and methods
    def __new__(mcs, name, bases, attrs):
        # Add a new attribute to the class
        attrs['created_by_metaclass'] = True
        # Call the parent's __new__ to create the class
        return super().__new__(mcs, name, bases, attrs)

class MyClass(metaclass=MyMeta):
    pass

# Now, MyClass has the new attribute
print(MyClass.created_by_metaclass)
# Output: True