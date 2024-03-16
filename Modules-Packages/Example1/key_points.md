### Key points related to module import

1. Python does import on runtime unlike C++, where they import modules at the time of compilation.
2. Actually, python import the module it(module) is executed.
3. Actually if python has already imported a module then it stores in the case and whenever the same module is imported again, it takes from the cache and it doesn't need to run it again

4. So one python import module. It firstly looks in sys.module file and if module is not found there, it imports from the actual location of the module
5. `<module_nmae>.prefix` (eg. sys.prefix) Can be used to know the location of python in system.

6. `sys.path` gives the list of parts where python will look for modules.
```python
    ['/Users/amit/Drive-D/Code/Python/Advance Python/Modules-Packages/Example1', 
    '/Library/Frameworks/Python.framework/Versions/3.11/lib/python311.zip', 
    '/Library/Frameworks/Python.framework/Versions/3.11 lib/python3.11', 
    '/Library/Frameworks/Python.framework/Versions/3.11 lib/python3.11/lib-dynload', 
    '/Users/amit/Drive-D/Code/Python/Advance Python/.venv/lib/python3.11/site-packages'
    ]
```
7. So if we attend the module in the list, pattern can also import that module
8. Actually, python can also import modules from zip files.
9. If we import a module (say `module1`) now it is stored in the cache and it is also listed in the global space. So if we want to delete the module and we removed the module from global namespace using `del globals()['module']` And we want to again import the module1 this time it is not going to load the module from the memory, instead it is going to get from the cache because `del globals()['module']`, doesn't delete the module from the cache instead, it removes it from global spaces.