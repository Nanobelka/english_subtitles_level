# [English Movie Level Prediction](https://movie-level.streamlit.app/)
## Исследование и моделирование

Выполнена обработка входных данных и создан датасет для обучения модели.  
Создана baseline-модель.  
Созданы и сравнены несколько моделей.  
Исследовано влияние на качество модели ряда дополнительных признаков.  

### 1. [Подготовка словаря](https://nbviewer.jupyter.org/github/Nanobelka/english_subtitles_level/blob/main/ML/1_words.ipynb)  
Создан словарь, включающий слова из `"American_Oxford_3000_by_CEFR_level"` и `"American_Oxford_5000_by_CEFR_level"`.  
Для каждого слова указан его уровень.  

### 2. [Подготовка слов из субтитров](https://nbviewer.jupyter.org/github/Nanobelka/english_subtitles_level/blob/main/ML/2_subtitles.ipynb)  
Из субтитров удалена лишняя информация (служебные данные, знаки препинания и т. п.)  
Уровень приведен в соотетствие с классификации CEFR.  
Разработаны новые признаки для проверки их влияния на качество модели.  

### 3. [Baseline-модель](https://nbviewer.jupyter.org/github/Nanobelka/english_subtitles_level/blob/main/ML/3_baseline.ipynb)  
Для baseline-модели были сгенерированы тексты, состоящие из слов какого-либо определенного уровня.  
На этих текстах обучена baseline-модель. Эта модель не требует для обучения фильмы с оценками экспертов.  
Получены метрики для тестовой выборки (для реальных фильмов).  

### 4. [Создание модели](https://nbviewer.jupyter.org/github/Nanobelka/english_subtitles_level/blob/main/ML/4_model.ipynb)  
Выбрана метрика для оптимизации гиперпараметров модели.  
Построены пайплайны с использованием **TF-IDF**.  
В пайплайнах учена возможность обработки дополнительных числовых признаков.  
Построено несколько различных моделей.  
Разработана комплексная метрика для оценки модели.  
Выбрана лучшая модель.  
Сделана контрольная проверка модели на тестовой выборке.  
Модель сохранена для использования в [онлайн-приложении](https://movie-level.streamlit.app/).  

### 5. [Поиск кластеров и выбросов](https://nbviewer.jupyter.org/github/Nanobelka/english_subtitles_level/blob/main/ML/5_outliers.ipynb)  
Создан трансоформер данных, проецирующий текст субтитров в двумерное пространство принципиальных компонент.  
Преобразованные данные изображены на интерактивном графике.  
Проанализированы полученные кластеры.  
Отмечено отсутствие выбросов.  
В качестве резерва сделан статичный график без использования Plotly.  
[график "Clusters and Outliers detection"](https://github.com/Nanobelka/english_subtitles_level/blob/main/ML/movie_subtitles_projection.html)  
[график](https://Nanobelka.github.io/english_subtitles_level/blob/main/ML/movie_subtitles_projection.html)

<a href="https://Nanobelka.github.io/english_subtitles_level/index.html">Открыть файл в формате HTML</a>
