# Приложение для бронирования комнат в отеле
Требования:
- [x] Для комнат должны быть поля: номер/название, стоимость за сутки, количество
мест.
- [x] Пользователи должны уметь фильтровать и сортировать комнаты по цене, по
количеству мест.
- [x] Пользователи должны уметь искать свободные комнаты в заданном временном
интервале.
- [x] Пользователи должны уметь забронировать свободную комнату.
- [x] Суперюзер должен уметь добавлять/удалять/редактировать комнаты и
редактировать записи о бронях через админ панель Django.
- [x] Брони могут быть отменены как самим юзером, так и суперюзером.
- [x] Пользователи должны уметь регистрироваться и авторизовываться (логиниться).
- [x] Чтобы забронировать комнату пользователи должны быть авторизованными.
Просматривать комнаты можно без логина. Авторизованные пользователи должны
видеть свои брони.

Стек:
* Django;
* DRF;
* СУБД предпочтительно PostgreSQL, но не обязательно. Главное не SQLite;
* При необходимости можно добавлять другие библиотеки.

Приветствуется:
- [x] Автотесты;
- [x] Аннотации типов;
- [x] Линтер;
- [x] Автоформатирование кода;
- [x] Документация к API;
- [x] Инструкция по запуску приложения.
