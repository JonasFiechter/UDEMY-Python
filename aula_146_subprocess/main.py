import subprocess


if __name__ == '__main__':
    proc = subprocess.run(
        ['ping', 'google.com.br'],
        capture_output=True,
        text=True
    )

    saida = proc.stdout
    print(saida)