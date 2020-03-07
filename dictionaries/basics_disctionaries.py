alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

alien_1 = {'x_position': 0, 'y_position':25, 'speed': 'medium'}
print("Original x position: " + str(alien_1['x_position']))

if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_1['x_position'] = alien_1['x_position'] + x_increment
print("New alien position it's: " + str(alien_1['x_position']) + '.')
print(alien_1.items())

#for name in favorite_languages.keys() si puo solo scrive ...in favorite_languages
#perche il default e iterare le keys

#for name, language in favorite_languages itera sia le keys che i value
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()): #set sceglie solo el un unica volta evita ripetizioni
    print(language.title())
