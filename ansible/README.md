# ansible/

Автоматическая настройка VM `devops-vm` и деплой образа `ghcr.io/katshuuu/devops-ci-app` по полному SHA.

Запускать из каталога `ansible/` (на macOS/Linux/WSL; репозиторий — не на `/mnt/c`).

```bash
ansible-galaxy collection install -r requirements.yml

# первичный запуск (student, пароль)
ansible-playbook -i inventory/bootstrap.ini site.yml --ask-pass --ask-become-pass

# последующие запуски (devops, ключ ~/.ssh/devops_vm, без ввода пароля)
ansible-playbook site.yml

# read-only аудит
ansible-playbook verify.yml
```

Версия приложения меняется одной переменной: `group_vars/all.yml` → `app_tag`.
Пароли и закрытые ключи в репозиторий не добавляются.
