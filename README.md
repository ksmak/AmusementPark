                    Домашнее задание

Напишите приложение Flask, которое будет использовать Redis для
кэширования результатов запросов к API. Реализуйте логику
кэширования данных в Redis, чтобы уменьшить нагрузку на API и
повысить скорость отклика приложения.
Приложение на тематику «Парк аттракционов»

https://docs.redis.com/latest/rs/references/client_references/client_python/


flask db init                           - инициализация базы данных
flask db migrate -m "Initial migrate"   - начальная точка миграции (аналогично makemigrations в django)
flask db upgrade                        - изменение базы данных (аналогично migrate в django)
flask run                               - запуск приложения