#5. Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити). Словник для
   роботи захардкодити свій.

student = {'id1':
   {'name': ['Artur'],
    'class': ['11-A'],
    'subjects': ['english, history, biology']
   },
 'id2':
  {'name': ['Andrew'],
    'class': ['9-A'],
    'subjects': ['english, history, biology']
   },
 'id3':
    {'name': ['Artur'],
    'class': ['11-A'],
    'subjects': ['english, history, biology']
   },
 'id4':
   {'name': ['Artem'],
    'class': ['11-B'],
    'subjects': ['english, history, biology']
   },
}
result = {}

for key,value in student.items():

    if value not in result.values():
        result[key] = value

print(result)
