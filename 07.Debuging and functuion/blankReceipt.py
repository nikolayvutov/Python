def line():
    print('------------------------------')

def header():
    print('CASH RECEIPT')
    line()

def print_body():
    print('Charged to____________________')
    print('Received by___________________')

def footer():
    line()
    print('© SoftUni')

def document():
    header()
    print_body()
    footer()

document()