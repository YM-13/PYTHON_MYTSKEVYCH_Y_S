class Test():
    pass

a = Test()

type("Test", (), {})
a = type("Test", (), {})
print(a)

b = a()
print(b)

def get_version():
    return 222

cls_dict = {}
cls_dict["version"] = get_version()
cls_dict["name"] = "name"
cls_dict["age"] = "age"

new_cls = type("test", (), cls_dict)
vars(new_cls)