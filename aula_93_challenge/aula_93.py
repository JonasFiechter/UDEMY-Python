"""
Faça uma lista de tarefas com as seguintes ações:
    adicionar tarefas
    listar tarefas
    opção de desfazer(a cada vez que chamarmos, desfaz a ultima ação)
    opção de refazer(a cada vez que chamarmos, refaz a última ação)
"""


def add_to_tasklist():
    entry = input('Input a task: ')
    task_list.append(entry)
    print('Done.')


def delete_from_tasklist():
    entry = input('Input a task to remove: ')
    if entry in task_list:
        for n, t in enumerate(task_list):
            if t == task_list[n]:
                task_list.pop(n)
                print('Done.')
    else:
        print('Invalid option')


def undo():
    pass


task_list = []
redo_list = []


def main():
    run = True
    input('Welcome to your tasklist\n'
          'to continue press "ENTER"')
    while run:
        entry = input('Input a command: "ADD", "DELETE", "UNDO", "REDO", "SHOW" or "EXIT"').upper()

        if entry == 'ADD':
            add_to_tasklist()
        elif entry == 'DELETE':
            delete_from_tasklist()
        elif entry == 'SHOW':
            print(task_list)
        elif entry == 'UNDO':
            continue
        elif entry == 'REDO':
            continue
        elif entry == 'EXIT':
            break
        else:
            print('Invalid option')


if __name__ == '__main__':
    main()

exit()
