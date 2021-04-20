from MyMainPackage.some_main_script import report_main
from MyMainPackage.SubPackage import mysubscript
from mymodule import my_func

my_func() # Since it's imported directly the function --> It's not necessary to indicate the sumbmodule or package

report_main() # Since it's imported directly the function --> It's not necessary to indicate the sumbmodule or package

mysubscript.sub_report()  # Since it's not imported directly the function --> It's necessary to indicate the sumbmodule or package
