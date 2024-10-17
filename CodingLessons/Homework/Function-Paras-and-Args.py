def Math(Number_1,Number_2):
    if isinstance(Number_1, (int, float)) and isinstance(Number_2, (int, float)):
        result = Number_1 * Number_2
        print(f'The result of {Number_1} multiplied by {Number_2} is {result}')
    else:
        print('Error: Both arguments must be numbers')

Math(2,7)
Math(3,2)
Math(6,9)

#End 1
print()

def Movie(title, genre, year):
    print(f'Title : {title}\nGenre : {genre}\nYear : {year}')
Movie('Mutiny on the Bounty','Historical Adventure Drama','1962')

#End 2
print()

Index = 0
List = ['title', 'genre', 'year']
Movie1 = {
    'title': 'Mutiny on the Bounty',
    'genre': 'Historical Adventure Drama',
    'year': '1962'
}

def Movie2(movie_list):
    Index = 0
    for key in List:
        print(f'{List[Index]}: {movie_list[key]}')
        print('')
        Index += 1
Movie2(Movie1)