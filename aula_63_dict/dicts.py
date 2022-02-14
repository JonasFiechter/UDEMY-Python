questions = {
    '1': {
        'question': 'how much is 2+2',
        'answer': {
            'a': '2',
            'b': '3',
            'c': '4',
        },
        'correct_a': 'c'
    },
    '2': {
        'question': 'how much is 4+2',
        'answer': {
            'a': '6',
            'b': '7',
            'c': '4',
        },
        'correct_a': 'a'
    },
    '3': {
        'question': 'how much is 4-2',
        'answer': {
            'a': '8',
            'b': '3',
            'c': '2',
        },
        'correct_a': 'c'
    }
}

for qk, qv in questions.items():
    print(f'{qk}: {qv["question"]}')
    for ak, av in qv['answer'].items():
        print(f'[{ak}]: {av}')

    print()
    answer_input = input('Place your answer: ')
    print()

    if answer_input == qv['correct_a']:
        print('correct')
    else:
        print('invalid')
    print()