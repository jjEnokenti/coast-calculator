

<h1 align="center">API Расчета страхования в зависимости от груза и стоимости транспортировки</h1>

---

<h3 align="center">Стек</h3>
<p align="center">
<img src="https://img.shields.io/badge/Python-3.10-yellow?&logo=appveyor" alt="">
<img src="https://img.shields.io/badge/PostgreSQL-15.1-orange?logo=appveyor" alt="">
<img src="https://img.shields.io/badge/FastAPI-0.100.0-green?logo=appveyor" alt="">
<img src="https://img.shields.io/badge/Tortoise_orm-0.19.3-green?logo=appveyor" alt="">
<img src="https://img.shields.io/badge/Docker-blue?logo=appveyor" alt="">
<img src="https://img.shields.io/badge/Docker-compose-blue?logo=appveyor" alt="">
<img src="https://img.shields.io/badge/Uvicorn-0.23.0-green?logo=appveyor" alt="">
<img src="https://img.shields.io/badge/aerich-0.7.1-green?logo=appveyor" alt="">
<img src="https://img.shields.io/badge/pydantic-1.10.9-green?logo=appveyor" alt="">
</p>

---

<h3 align="center">Все доступные эндоинты можно посмотреть на странице swagger.</h3>

    0.0.0.0:8000/docs/

---

<h3 align="center">Доступные эндпоинты</h3>
<table>
  <thead>
    <tr>
      <th>Действие</th>
      <th>Метод запроса</th>
      <th>Эндпоинт</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Рассчитать стоимость страхования</td>
      <td>GET</td>
      <td>/calculate_insurance/</td>
    </tr>
    <tr>
      <td>Получить все ставки</td>
      <td>GET</td>
      <td>/rates/</td>
    </tr>
    <tr>
      <td>Загрузить данные по ставкам с помощью json строки</td>
      <td>POST</td>
      <td>/upload_tariff/</td>
    </tr>
    <tr>
      <td>Загрузить данные по ставкам с помощью json файла</td>
      <td>POST</td>
      <td>/upload_file_tariff/</td>
    </tr>
  </tbody>
</table>

---

<h3 align="center">Установка проекта</h3>

### 1. Склонируйте репозиторий
    git clone https://github.com/jjEnokenti/coast-calculator.git

### 2. Настройте окружение
#### 1. создайте файл .env по примеру .env.example

### 3. Можете запускать приложение
    make up
### 4. Для остановки контейнеров
    make down

---

<h2 align="center">ТЗ</h2>

<p>Реализовать REST API сервис по расчёту стоимости
страхования в зависимости от типа груза и объявленной стоимости (ОС).
Тариф должен загружаться из файла JSON или должен
принимать подобную JSON структуру</p>

Сервис должен посчитать стоимость
страхования для запроса используя
актуальный тариф.(Загружается через API)
* Сервис возвращает (объявленную стоимость * rate) в зависимости от
указанного в запросе типа груза и даты.
* Сервис должен разворачиваться внутри Docker.
* Сервис должен разрабатываться через GIT (Файл Readme с подробным описанием развертывания)
* Данные должны храниться в базе данных

Технологии, которые должны быть использованы при реализации тестового задания:
* FastApi - framework
* Tortoise ORM
* Postgresql, Mysql, Sqlite – любой на выбор
* Docker
* Docker-compose с докером для постгреса
