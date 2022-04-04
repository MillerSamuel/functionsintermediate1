x = [ [5,2,3], [15,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Bryant'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 30} ]


def iterateDictionary(list):
    for i in list:
        print(i)

iterateDictionary(students)

def iterateDictionary2(name,list):
        for i in list:
            print(i[name])

iterateDictionary2('last_name',students)

def printInfo(dict):
    for i in dict:
        print(len(dict[i]),i)
        for x in range(0,len(dict[i]),1):
            print(dict[i][x])

printInfo(sports_directory)