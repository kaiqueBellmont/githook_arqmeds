import os
import click


@click.group()
def cli():
    pass


@cli.command()
def create_pre_commit():
    pre_commit_script = '"#!/bin/sh\npython3 -c "import script"'


    hooks_dir = os.path.join(".git", "hooks")
    pre_commit_path = os.path.join(hooks_dir, "pre-commit")

    # Verificar se o diretório .git/hooks existe
    if not os.path.exists(hooks_dir):
        os.makedirs(hooks_dir)

    # Criar o arquivo .git/hooks/pre-commit
    with open(pre_commit_path, "w") as file:
        file.write(pre_commit_script)

    # Dar permissão de execução ao arquivo
    os.chmod(pre_commit_path, 0o755)

    print("Hook pre-commit criado com sucesso!")


if __name__ == "__main__":
    cli()
