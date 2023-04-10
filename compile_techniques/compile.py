# In this file, I am going to test the funtion exec, compile and VARS in Garnet/compilerLib.py.
import inspect

if __name__ == "__main__":
    VARS = dict()
    filePath = "test.garnet"
    infile = open(filePath)

    # Now we import the library.py where print_ln has been defined.
    import library
    instr_classes = [
        t[1]
        for t in inspect.getmembers(library, inspect.isfunction)
        if t[1].__module__ == library.__name__
    ]
    print("instr_classes is: ", instr_classes)

    # Create the dictionary, when the key is called in the file, 
    # it will go to call its related values.(which should be a function/class) 
    for op in instr_classes:
                VARS[op.__name__] = op

    exec(compile(infile.readlines()[0], infile.name, "exec"), VARS)
    infile.close()

    # Now we add the classes cint

    infile = open(filePath)
    instr_classes += [
        t[1]
        for t in inspect.getmembers(library, inspect.isclass)
        if t[1].__module__ == library.__name__
    ]
    print("Now, the instr_classes is: ", instr_classes)
    for op in instr_classes:
                VARS[op.__name__] = op

    exec(compile(infile.read(), infile.name, "exec"), VARS)