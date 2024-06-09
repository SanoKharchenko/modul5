def est_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
    return

a = est_function()
b = inner_function()  #Нельзя вызвать отдель ту функцию которая внутри другой функции