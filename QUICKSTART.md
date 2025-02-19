#

для настройки страницы перейти по адресу `/adm` и указать логин, пароль.

в первую очередь следует загрузить нужные ассеты - минимально это icon.png (для отображения на вкладке браузера) и logo (для отображения на стартовом экране и навигационной панели). при необходимости загрузить остальные изображения (для раздела с услугами, для портфолио и т.д.).

минимально необходимо создать два раздела страницы - "стартовый экран" и "футер"; эти разделы обязательны, без них нельзя создать страницу. при необходимости - создать остальные разделы страницы ("услуги", "портфолио", "обо мне", "контакты" - они необязательны, любой из них можно исключить).

## разделы
у всех сущностей есть следующие параметры:
- "название" - как правило используется только в админке (если не сказано иное)
- "примечание" - вспомогательные данные только для внутреннего использования
- "описание" - вспомогательные данные; только для CEO - "страница", "ассеты"; отображение доп. данных - "портфолио", строки и блоки услуг; в остальных случаях не используется

### страница
основная сущность, включающая в себя остальные компоненты
- "описание" - тэг `meta` страницы, имеет значение для CEO
- "название страницы" - тэг `title` (отображается на вкладке браузера)
- "сделать активной" - отображать эту страницу при переходе на сайт (только одна страница может быть активной; если уже была активная страница - она будет деактивирована)
- "иконка (png)" - favicon
- "лого" - логотип для навигационной панели
- "стартовый экран" - то, что первым видит пользователь
- "промо"
- "показывать панель навигации" - чекбокс, включающий отображение навигационной панели
- "услуги"
- "портфолио"
- "обо мне"
- "контакты"
- "футер"

### ассет
- "описание" - пишется в тег `alt`, может влиять на CEO
- "файл" - собственно файл
- "тэг" - вспомогательная метка для облегчения поиска (например, все изображения для портфолио можно пометить соответствующей меткой и при заполнении портфолио можно будет отфильтровать нужные изображения)

### стартовый экран
- "лого"
- "паттерн" - изображение для заполнения фона
- "основной текст" - h1, поэтому влияет на CEO; поддерживает тэги html
- "дополнительный текст" - поддерживает тэги html

### услуги
раздел услуг собирается из блоков, которые в свою очередь собираются из отдельных строк

#### строки
- "название" - первая строка; поддерживает тэги html
- "описание" - дополнительные строки; поддерживает тэги html
- "fa-иконка" - иконка из 'font awesome'

#### блоки
каждый блок состоит из двух половин - на одной отображаются строки с данными, на другой изображение
- "название" - первая строка; поддерживает тэги html
- "описание" - доп. строка; поддерживает тэги html
- "изображение"
- "расположение изображения" - правая или левая половина
- "строки" - произвольное количество в произвольном порядке

### контакты
состоят из двух типов - ссылки (например, соц. сети) и доп. данные (например, адрес или график работы)

#### котактные данные
- "название" - первая строка; поддерживает тэги html
- "fa-иконка" - иконка из 'font awesome'
- "информация" - доп. данные; поддерживает тэги html

#### ссылки
- "fa-иконка" - иконка из 'font awesome'
- "ссылка"

в контактах можно указать произвольное количество данных и ссылок. можно настроить порядок их размещения. виджет карт можно взять, для примера, из яндекс карт.

### обо мне
- "сообщение" - поддерживает html
- "аватар"
- "паттерн"

### портфолио
- "примеры" - произвольное количество изображений в произвольном порядке

### футер
- "лого"
- "паттерн"
- "копирайт"

## превью
для того, чтобы иметь возможность визуально оценить новую страницу, не делая её активной (а соответствено и доступной всем), доступен адрес `/previews/<id>/`, где \<id\> - идентификатор страницы (можно найти в админке на вкладке "страницы"). например `/previews/1/`

данный функционал работает только для авторизованных пользователей с правами суперпользователя (с доступом в админку).
